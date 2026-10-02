import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "manage_skills.py"
COMPONENTS = {
    "auditoria-web-prospectos",
    "venta-con-criterio",
    "prospeccion-con-evidencia",
    "shared",
}
PLATFORM_ROOTS = {
    "codex": Path(".codex/skills"),
    "claude": Path(".claude/skills"),
    "opencode": Path(".opencode/skills"),
}


def run_cli(*args: str, cwd: Path | None = None):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=cwd or REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class ManageSkillsTests(unittest.TestCase):
    def test_verify_canonical_bundle(self):
        result = run_cli("verify")
        self.assertEqual(result.returncode, 0, result.stderr)
        for skill in COMPONENTS - {"shared"}:
            self.assertIn(f"valid skill: {skill}", result.stdout)

    def test_builds_one_project_scoped_archive_per_platform(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "first"
            repeated_output = Path(temporary) / "second"
            result = run_cli("package", "all", "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stderr)
            repeated = run_cli(
                "package", "all", "--output", str(repeated_output)
            )
            self.assertEqual(repeated.returncode, 0, repeated.stderr)

            for platform, root in PLATFORM_ROOTS.items():
                archive_path = output / f"auditoria-prospectos-{platform}.zip"
                self.assertTrue(archive_path.is_file())
                self.assertEqual(
                    archive_path.read_bytes(),
                    (repeated_output / archive_path.name).read_bytes(),
                )
                with zipfile.ZipFile(archive_path) as archive:
                    names = set(archive.namelist())
                for skill in COMPONENTS - {"shared"}:
                    expected = (root / skill / "SKILL.md").as_posix()
                    self.assertIn(expected, names)
                self.assertIn(
                    (root / "shared" / "auditoria-a-venta.md").as_posix(), names
                )
                self.assertFalse(any("auditorias/" in name for name in names))

    def test_installs_all_platforms_into_a_project(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = run_cli(
                "install", "all", "--scope", "project", "--target", str(target)
            )
            self.assertEqual(result.returncode, 0, result.stderr)

            for root in PLATFORM_ROOTS.values():
                for skill in COMPONENTS - {"shared"}:
                    self.assertTrue((target / root / skill / "SKILL.md").is_file())
                self.assertTrue(
                    (target / root / "shared" / "auditoria-a-venta.md").is_file()
                )

            repeated = run_cli(
                "install", "all", "--scope", "project", "--target", str(target)
            )
            self.assertEqual(repeated.returncode, 0, repeated.stderr)
            self.assertIn("unchanged:", repeated.stdout)

    def test_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            result = run_cli(
                "install",
                "all",
                "--scope",
                "project",
                "--target",
                str(target),
                "--dry-run",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("would install:", result.stdout)
            self.assertFalse((target / ".codex").exists())
            self.assertFalse((target / ".claude").exists())
            self.assertFalse((target / ".opencode").exists())

    def test_refuses_to_replace_different_install_without_force(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            destination = target / ".codex/skills/auditoria-web-prospectos"
            destination.mkdir(parents=True)
            (destination / "SKILL.md").write_text("different", encoding="utf-8")

            result = run_cli(
                "install", "codex", "--scope", "project", "--target", str(target)
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("Refusing to replace", result.stderr)
            self.assertEqual(
                (destination / "SKILL.md").read_text(encoding="utf-8"), "different"
            )

    def test_conflict_preflight_does_not_leave_a_partial_install(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            conflict = target / ".codex/skills/venta-con-criterio"
            conflict.mkdir(parents=True)
            (conflict / "SKILL.md").write_text("different", encoding="utf-8")

            result = run_cli(
                "install", "codex", "--scope", "project", "--target", str(target)
            )
            self.assertEqual(result.returncode, 2)
            self.assertFalse(
                (target / ".codex/skills/auditoria-web-prospectos").exists()
            )
            self.assertEqual(
                (conflict / "SKILL.md").read_text(encoding="utf-8"), "different"
            )

    def test_force_keeps_a_backup(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            destination = target / ".claude/skills/venta-con-criterio"
            destination.mkdir(parents=True)
            (destination / "SKILL.md").write_text("different", encoding="utf-8")

            result = run_cli(
                "install",
                "claude",
                "--scope",
                "project",
                "--target",
                str(target),
                "--force",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            backups = list(destination.parent.glob(".venta-con-criterio.backup-*"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(
                (backups[0] / "SKILL.md").read_text(encoding="utf-8"), "different"
            )
            installed = (destination / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("name: venta-con-criterio", installed)


if __name__ == "__main__":
    unittest.main()
