import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('harness_config', ROOT/'scripts/harness_config.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HarnessConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT/'examples/assistant-harness/config.example.json').read_text())
        self.locator = 'https://github.com/example/knowledge/blob/main/systems/harness.json'

    def test_valid_read_only_profile(self):
        self.assertEqual(module.validate(self.config), [])
        self.assertFalse(any(self.config['permissions'][x] for x in ('project_updates','knowledge_updates','document_organization','calendar_record_confirmed_commitments')))

    def test_invalid_and_confusable_permission_values(self):
        for value in ('true', 1, None, [], {}):
            with self.subTest(value=value):
                candidate = copy.deepcopy(self.config)
                candidate['permissions']['knowledge_updates'] = value
                self.assertTrue(module.validate(candidate))

    def test_preserves_protected_actions_and_account_boundary(self):
        for modify in (lambda x: x['permissions']['requires_explicit_approval'].remove('send_email'),
                       lambda x: x['accounts'].update(personal_google_access=True),
                       lambda x: x['transport'].update(mode='browser_fallback')):
            candidate = copy.deepcopy(self.config)
            modify(candidate)
            self.assertTrue(module.validate(candidate))

    def test_rejects_unknown_version_invalid_timezone_and_unpinned_source(self):
        for section,key,value in ((None,'schema_version',True),(None,'timezone','PST'),('deployment','ref','main')):
            candidate = copy.deepcopy(self.config)
            (candidate[section] if section else candidate)[key] = value
            self.assertTrue(module.validate(candidate))

    def test_rejects_credential_urls_and_secret_fields(self):
        for value in ('http://trello.com/b/example','https://user:secret@trello.com/b/example','https://trello.com/b/example?token=secret'):
            candidate = copy.deepcopy(self.config)
            candidate['sources']['projects']['url'] = value
            self.assertTrue(module.validate(candidate))
        candidate = copy.deepcopy(self.config)
        candidate['accounts']['access_token'] = 'dummy'
        self.assertTrue(module.validate(candidate))

    def test_rejects_duplicate_registration_and_escaping_policy(self):
        candidate = copy.deepcopy(self.config)
        candidate['task_registry'] = [{'id':'one'},{'id':'one'}]
        self.assertTrue(module.validate(candidate))
        candidate = copy.deepcopy(self.config)
        candidate['policies']['knowledge_rules']['path'] = '../other/AGENTS.md'
        self.assertTrue(module.validate(candidate))

    def test_renders_pinned_prompt_with_correct_workflow_and_failure_policy(self):
        for role,skill,mode in (('daily','outer-harness','daily'),('completion-watch','outer-harness','completion-watch'),('knowledge','outer-harness','knowledge')):
            prompt = module.render(self.config,self.locator,role)
            self.assertIn('$'+skill,prompt)
            self.assertIn(self.locator,prompt)
            self.assertIn('ref '+self.config['deployment']['ref'],prompt)
            self.assertIn('do not advance progress',prompt)
            self.assertIn('Do not create replacement jobs',prompt)
            if mode:
                self.assertIn('mode='+mode,prompt)

    def test_rejects_wrong_private_repository_and_event_task_shortcut(self):
        for locator in ('https://github.com/other/knowledge/blob/main/harness.json','https://github.com/example/knowledge/blob/main/harness.json?token=x','file:///tmp/config.json'):
            with self.assertRaises(ValueError):
                module.render(self.config,locator,'knowledge')
        with self.assertRaises(KeyError):
            module.render(self.config,self.locator,'email-event')

    def test_cli_fails_without_locator_and_keeps_source_unchanged(self):
        path = ROOT/'examples/assistant-harness/config.example.json'
        before = path.read_bytes()
        result = subprocess.run([sys.executable,str(ROOT/'scripts/harness_config.py'),str(path),'--render','daily'],capture_output=True,text=True)
        self.assertEqual(result.returncode,1)
        self.assertIn('--locator is required',result.stderr)
        self.assertEqual(path.read_bytes(),before)


if __name__ == '__main__':
    unittest.main()
