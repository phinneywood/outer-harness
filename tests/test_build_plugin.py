import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_plugin', ROOT / 'scripts/build_plugin.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
SKILLS = ['harness-audit', 'outer-harness']


class PluginArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for source in ('LICENSE', 'plugins/assistant-harness', *(f'skills/{s}' for s in SKILLS)):
            src, dst = ROOT / source, self.root / source
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        self.root_patch = patch.object(builder, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.addCleanup(self.temp.cleanup)

    def build(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return builder.build('assistant-harness', SKILLS, self.root / 'dist')

    def test_archive_has_license_exact_reviewed_files_and_matching_source_bytes(self):
        reviewed = json.loads((self.root / 'plugins/assistant-harness/package-files.json').read_text())
        with ZipFile(self.build()) as archive:
            self.assertEqual(set(archive.namelist()), {'plugin.json', *reviewed})
            self.assertEqual(archive.read('LICENSE'), (self.root / 'LICENSE').read_bytes())
            for name in reviewed:
                self.assertEqual(archive.read(name), (self.root / name).read_bytes())
            self.assertEqual(json.loads(archive.read('plugin.json'))['version'], '2.0.0')

    def test_unreviewed_private_file_does_not_enter_archive(self):
        (self.root / 'skills/outer-harness/private-config.json').write_text('{"not_for_distribution": true}')
        with ZipFile(self.build()) as archive:
            self.assertNotIn('skills/outer-harness/private-config.json', archive.namelist())

    def test_rejects_symlink_to_unreviewed_content(self):
        source = self.root / 'skills/outer-harness/SKILL.md'
        source.unlink()
        source.symlink_to(self.root / 'LICENSE')
        with self.assertRaisesRegex(ValueError, 'symlink'):
            self.build()

    def test_rejects_path_escape_and_omitted_license(self):
        file_list = self.root / 'plugins/assistant-harness/package-files.json'
        original = json.loads(file_list.read_text())
        for candidate in ([p for p in original if p != 'LICENSE'], [*original, '../private.txt']):
            with self.subTest(candidate=candidate):
                file_list.write_text(json.dumps(candidate))
                with self.assertRaises(ValueError):
                    self.build()

    def test_rejects_manifest_symlink(self):
        manifest = self.root / "plugins/assistant-harness/plugin.json"
        copied = self.root / "manifest-copy.json"
        copied.write_bytes(manifest.read_bytes())
        manifest.unlink()
        manifest.symlink_to(copied)
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.build()

    def test_rejects_reserved_archive_name_collision(self):
        reviewed = self.root / "plugins/assistant-harness/package-files.json"
        (self.root / "plugin.json").write_text("{}")
        reviewed.write_text(json.dumps([*json.loads(reviewed.read_text()), "plugin.json"]))
        with self.assertRaisesRegex(ValueError, "collide"):
            self.build()

    def test_same_sources_produce_identical_archive_bytes(self):
        first = self.build().read_bytes()
        self.assertEqual(first, self.build().read_bytes())

    def test_requested_skills_cannot_bypass_reviewed_package_scope(self):
        with self.assertRaisesRegex(ValueError, 'match the reviewed'):
            builder.build('assistant-harness', ['assistant-harness'], self.root / 'dist')


if __name__ == '__main__':
    unittest.main()
