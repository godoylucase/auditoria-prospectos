#!/usr/bin/env python3
"""Verify, package, and install the repository's portable agent skills."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import sys
import tempfile
import uuid
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "skills"
SKILL_NAMES = (
    "auditoria-web-prospectos",
    "venta-con-criterio",
    "prospeccion-con-evidencia",
)
COMPONENT_NAMES = (*SKILL_NAMES, "shared")
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass(frozen=True)
class Platform:
    project_parts: tuple[str, ...]
    user_parts: tuple[str, ...]


PLATFORMS = {
    "codex": Platform((".codex", "skills"), (".codex", "skills")),
    "claude": Platform((".claude", "skills"), (".claude", "skills")),
    "opencode": Platform(
        (".opencode", "skills"), (".config", "opencode", "skills")
    ),
}


class SkillError(RuntimeError):
    """Raised when the canonical bundle is invalid or an install is unsafe."""


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        raise SkillError(f"Missing YAML frontmatter: {skill_file}")

    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.startswith((" ", "\t")):
            continue
        key, separator, value = raw_line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def iter_component_files(component: Path):
    for path in sorted(component.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            yield path


def verify_source() -> list[str]:
    messages: list[str] = []
    for skill_name in SKILL_NAMES:
        skill_dir = SOURCE_ROOT / skill_name
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            raise SkillError(f"Missing skill entrypoint: {skill_file}")
        metadata = parse_frontmatter(skill_file)
        if metadata.get("name") != skill_name:
            raise SkillError(
                f"Skill name {metadata.get('name')!r} does not match {skill_name!r}"
            )
        if not NAME_PATTERN.fullmatch(skill_name):
            raise SkillError(f"Invalid portable skill name: {skill_name}")
        description = metadata.get("description", "")
        if not 1 <= len(description) <= 1024:
            raise SkillError(
                f"Description must contain 1-1024 characters: {skill_file}"
            )
        messages.append(f"valid skill: {skill_name}")

    shared_contract = SOURCE_ROOT / "shared" / "auditoria-a-venta.md"
    if not shared_contract.is_file():
        raise SkillError(f"Missing shared contract: {shared_contract}")

    for component_name in COMPONENT_NAMES:
        component = SOURCE_ROOT / component_name
        if not component.is_dir() or not any(iter_component_files(component)):
            raise SkillError(f"Empty component: {component}")

    for skill_name in ("auditoria-web-prospectos", "venta-con-criterio"):
        text = (SOURCE_ROOT / skill_name / "SKILL.md").read_text(encoding="utf-8")
        if "../shared/auditoria-a-venta.md" not in text:
            raise SkillError(f"{skill_name} does not reference the shared contract")

    return messages


def selected_platforms(name: str) -> list[str]:
    return list(PLATFORMS) if name == "all" else [name]


def archive_prefix(platform_name: str) -> PurePosixPath:
    return PurePosixPath(*PLATFORMS[platform_name].project_parts)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_archive(platform_name: str, output_dir: Path) -> Path:
    verify_source()
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"auditoria-prospectos-{platform_name}.zip"
    prefix = archive_prefix(platform_name)

    with tempfile.NamedTemporaryFile(
        prefix=f".{destination.name}.", suffix=".tmp", dir=output_dir, delete=False
    ) as temp_file:
        temp_path = Path(temp_file.name)

    try:
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for component_name in COMPONENT_NAMES:
                component = SOURCE_ROOT / component_name
                for source_file in iter_component_files(component):
                    relative = source_file.relative_to(SOURCE_ROOT)
                    archive_path = prefix / PurePosixPath(relative.as_posix())
                    info = zipfile.ZipInfo(str(archive_path), (1980, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, source_file.read_bytes())
        os.replace(temp_path, destination)
    finally:
        temp_path.unlink(missing_ok=True)

    return destination


def directories_equal(left: Path, right: Path) -> bool:
    left_files = {
        path.relative_to(left): sha256(path) for path in iter_component_files(left)
    }
    right_files = {
        path.relative_to(right): sha256(path) for path in iter_component_files(right)
    }
    return left_files == right_files


def install_root(platform_name: str, scope: str, target: Path | None) -> Path:
    platform = PLATFORMS[platform_name]
    if scope == "user":
        if target is not None:
            raise SkillError("--target is only valid with --scope project")
        return Path.home().joinpath(*platform.user_parts)

    project_root = (target or Path.cwd()).expanduser().resolve()
    if not project_root.is_dir():
        raise SkillError(f"Project target is not a directory: {project_root}")
    return project_root.joinpath(*platform.project_parts)


def backup_path(destination: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = destination.with_name(f".{destination.name}.backup-{stamp}")
    if not candidate.exists():
        return candidate
    return destination.with_name(f".{destination.name}.backup-{stamp}-{uuid.uuid4().hex[:8]}")


def install_component(source: Path, destination: Path, force: bool, dry_run: bool) -> str:
    if destination.exists():
        if not destination.is_dir():
            raise SkillError(f"Install destination is not a directory: {destination}")
        if directories_equal(source, destination):
            return f"unchanged: {destination}"
        if not force:
            raise SkillError(
                f"Refusing to replace a different installation: {destination}. "
                "Review it and rerun with --force."
            )

    if dry_run:
        action = "replace" if destination.exists() else "install"
        return f"would {action}: {destination}"

    destination.parent.mkdir(parents=True, exist_ok=True)
    staged = destination.parent / f".{destination.name}.tmp-{uuid.uuid4().hex}"
    shutil.copytree(source, staged)
    try:
        if destination.exists():
            destination.rename(backup_path(destination))
        staged.rename(destination)
    finally:
        if staged.exists():
            shutil.rmtree(staged)
    return f"installed: {destination}"


def preflight_install(
    platform_name: str, scope: str, target: Path | None, force: bool
) -> list[tuple[Path, Path]]:
    operations: list[tuple[Path, Path]] = []
    for selected in selected_platforms(platform_name):
        root = install_root(selected, scope, target)
        for component_name in COMPONENT_NAMES:
            source = SOURCE_ROOT / component_name
            destination = root / component_name
            if destination.exists():
                if not destination.is_dir():
                    raise SkillError(
                        f"Install destination is not a directory: {destination}"
                    )
                if not directories_equal(source, destination) and not force:
                    raise SkillError(
                        f"Refusing to replace a different installation: {destination}. "
                        "Review it and rerun with --force."
                    )
            operations.append((source, destination))
    return operations


def install(
    platform_name: str,
    scope: str,
    target: Path | None,
    force: bool,
    dry_run: bool,
) -> list[str]:
    verify_source()
    messages: list[str] = []
    for source, destination in preflight_install(
        platform_name, scope=scope, target=target, force=force
    ):
        messages.append(
            install_component(
                source,
                destination,
                force=force,
                dry_run=dry_run,
            )
        )
    return messages


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage the portable prospecting skills for Codex, Claude Code, and OpenCode."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("verify", help="validate the canonical skill bundle")

    package_parser = subparsers.add_parser(
        "package", help="build project-scoped ZIP packages"
    )
    package_parser.add_argument("platform", choices=[*PLATFORMS, "all"])
    package_parser.add_argument("--output", type=Path, default=REPO_ROOT / "dist")

    install_parser = subparsers.add_parser(
        "install", help="install skills for one platform or all platforms"
    )
    install_parser.add_argument("platform", choices=[*PLATFORMS, "all"])
    install_parser.add_argument("--scope", choices=["project", "user"], default="project")
    install_parser.add_argument("--target", type=Path)
    install_parser.add_argument("--force", action="store_true")
    install_parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "verify":
            for message in verify_source():
                print(message)
            print("valid shared contract: shared/auditoria-a-venta.md")
            return 0

        if args.command == "package":
            for platform_name in selected_platforms(args.platform):
                archive = build_archive(platform_name, args.output.resolve())
                print(f"packaged: {archive} sha256={sha256(archive)}")
            return 0

        for message in install(
            args.platform,
            scope=args.scope,
            target=args.target,
            force=args.force,
            dry_run=args.dry_run,
        ):
            print(message)
        return 0
    except SkillError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
