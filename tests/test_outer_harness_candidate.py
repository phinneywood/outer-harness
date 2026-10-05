"""Static source and offline migration checks, not model-behavior evaluations."""
import copy
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("preservation", ROOT / "scripts/check_task_preservation.py")
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)
SKILL = ROOT / "skills/outer-harness"


def snapshot():
    return dict(id="test-task", title="Test review", prompt="Old reviewed instructions",
                schedule="BEGIN:VEVENT\nRRULE:FREQ=DAILY\nEND:VEVENT", default_timezone="UTC",
                timing_mode="exact_schedule", is_enabled=True, runtime="work",
                conversation_id="test-conversation", notifications_enabled=False, email_enabled=False)


class PreservationTests(unittest.TestCase):
    def test_prompt_only_change(self):
        old = snapshot(); new = dict(old, prompt="Reviewed replacement")
        self.assertEqual(GUARD.check(old, new, new["prompt"]), [])

    def test_each_protected_field(self):
        for key in GUARD.REQUIRED:
            if key == "prompt": continue
            with self.subTest(key=key):
                old = snapshot(); new = copy.deepcopy(old)
                new[key] = not old[key] if type(old[key]) is bool else old[key] + " changed"
                self.assertTrue(GUARD.check(old, new, new["prompt"]))

    def test_missing_runtime_blocks(self):
        old = snapshot(); del old["runtime"]
        self.assertIn("before: missing runtime", GUARD.check(old, snapshot(), snapshot()["prompt"]))

    def test_missing_binding_blocks(self):
        old = snapshot(); del old["conversation_id"]
        self.assertTrue(GUARD.check(old, old, old["prompt"]))

    def test_event_requires_full_evidence(self):
        old = snapshot(); old["schedule"] = "BEGIN:VEVENT\nX-UNSCHEDULED:1\nEND:VEVENT"
        self.assertTrue(GUARD.check(old, old, old["prompt"]))

    def test_event_prompt_only(self):
        old = snapshot(); old.update(event_trigger={"type": "new_message", "filters": []},
                                     event_trigger_complete=True)
        new = dict(old, prompt="Reviewed event instructions")
        self.assertEqual(GUARD.check(old, new, new["prompt"], event=True), [])

    def test_changed_event_filters(self):
        old = snapshot(); old.update(event_trigger={"type": "new_message", "filters": []},
                                     event_trigger_complete=True)
        new = copy.deepcopy(old); new["event_trigger"]["filters"] = ["new filter"]
        self.assertTrue(GUARD.check(old, new, new["prompt"], event=True))

    def test_unknown_field_loss_blocks(self):
        old = snapshot(); old["host_scope"] = "existing scope"
        self.assertTrue(GUARD.check(old, snapshot(), old["prompt"]))

    def test_wrong_prompt_blocks(self):
        self.assertTrue(GUARD.check(snapshot(), snapshot(), "Different approved text"))

    def test_execution_timestamps_not_settings(self):
        old = snapshot(); new = dict(old, last_run_time="later", updated_at="later")
        self.assertEqual(GUARD.check(old, new, old["prompt"]), [])

    def test_false_string_not_permission(self):
        old = snapshot(); old["is_enabled"] = "false"
        self.assertTrue(GUARD.check(old, old, old["prompt"]))

    def test_guard_does_not_mutate(self):
        old = snapshot(); saved = copy.deepcopy(old)
        GUARD.check(old, old, old["prompt"])
        self.assertEqual(old, saved)


class SourceTests(unittest.TestCase):
    def test_frontmatter_and_size(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\nname: outer-harness\n"))
        self.assertLess(len(text.splitlines()), 100)
        self.assertLess(len(text.split()), 1000)

    def test_all_core_references_resolve(self):
        text = (SKILL / "SKILL.md").read_text()
        targets = set(re.findall(r"\]\((references/[^)]+)\)", text))
        self.assertEqual(len(targets), 5)
        for target in targets:
            self.assertTrue((SKILL / target).is_file(), target)

    def test_references_have_no_nested_file_dependencies(self):
        for path in (SKILL / "references").glob("*.md"):
            self.assertFalse(re.search(r"\]\((?!https?://)[^)]+\)", path.read_text()), path.name)

    def test_profile_starts_read_only(self):
        text = (ROOT / "examples/outer-harness/setup.example.md").read_text()
        self.assertIn("No routine maintenance authorized yet", text)
        self.assertIn("Schedules: none approved", text)
        self.assertIn("not configured or authorized", text)

    def test_required_safety_contracts_present(self):
        expectations = {
            "projects.md": ["one final brief", "message ID, not thread", "No relevant candidate", "read changed records back"],
            "knowledge.md": ["conditionally claim", "not rerun that day", "every intended write", "readback"],
            "scheduled-tasks.md": ["conversation binding", "full event triggers", "independent execution", "Specialty workflows"],
            "configuration.md": ["schema_version: 1", "sources.delivery", "Unknown or absent permissions", "one authoritative"],
            "onboarding.md": ["one or two", "read-only", "explicit approval", "not installation"],
        }
        for filename, phrases in expectations.items():
            text = (SKILL / "references" / filename).read_text()
            for phrase in phrases:
                self.assertIn(phrase, text, filename)


if __name__ == "__main__":
    unittest.main()
