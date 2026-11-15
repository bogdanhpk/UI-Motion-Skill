#!/usr/bin/env python3
"""Validate the distributable skill without running any bundled demo code."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote

import yaml

REPOSITORY = "https://github.com/bogdanhpk/UI-Motion-Skill"
SEMVER = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"


def validate(root, tag=None):
    root = root.resolve()
    skill = root / "ui-motion"
    errors = []
    for path in root.rglob("*"):
        if ".git" in path.parts or ".venv" in path.parts:
            continue
        if path.is_symlink():
            errors.append(f"Symbolic links are not allowed in the package: {path.relative_to(root)}")
    version_path = root / "VERSION"
    version = version_path.read_text().strip() if version_path.is_file() else ""
    if not re.fullmatch(SEMVER, version):
        errors.append("VERSION must contain a stable X.Y.Z version")
    if tag is not None and tag != f"v{version}":
        errors.append(f"Release tag {tag!r} does not match VERSION {version!r}")
    for relative in ["SKILL.md", "agents/openai.yaml"]:
        if not (skill / relative).is_file():
            errors.append(f"Missing ui-motion/{relative}")
    if errors:
        return errors
    entrypoints = sorted(path.relative_to(skill).as_posix() for path in skill.rglob("SKILL.md"))
    if entrypoints != ["SKILL.md"]:
        errors.append(f"Expected one skill entrypoint, found {entrypoints}")
    content = (skill / "SKILL.md").read_text()
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
    if not match:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        try:
            metadata = yaml.safe_load(match.group(1))
            if not isinstance(metadata, dict):
                raise ValueError("Frontmatter must be a mapping")
            if metadata.get("name") != "ui-motion":
                errors.append("Skill name must be ui-motion")
            description = metadata.get("description")
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                errors.append("A nonempty description of at most 1024 characters is required")
            extra = metadata.get("metadata", {})
            if not isinstance(extra, dict):
                raise ValueError("metadata must be a mapping")
            if extra.get("version") != version:
                errors.append("metadata.version must match VERSION")
            if extra.get("repository") != REPOSITORY:
                errors.append("metadata.repository must point to the official repository")
        except (yaml.YAMLError, ValueError) as error:
            errors.append(f"Invalid frontmatter: {error}")
    try:
        agent = yaml.safe_load((skill / "agents/openai.yaml").read_text())
        interface = agent.get("interface", {}) if isinstance(agent, dict) else {}
        if not isinstance(interface, dict) or not interface.get("display_name"):
            errors.append("agents/openai.yaml must include interface.display_name")
    except yaml.YAMLError as error:
        errors.append(f"Invalid agent metadata: {error}")
    checked = 0
    for path in sorted(skill.rglob("*.md")):
        text = re.sub(r"(?ms)^```.*?^```[^\n]*\n?", "", path.read_text())
        for link in re.findall(r"\]\(([^\n)]+)\)", text):
            link = link.strip().split(' "', 1)[0].strip("<>")
            if re.match(r"^[a-zA-Z][\w+.-]*:", link) or link.startswith("#"):
                continue
            relative = unquote(link.split("#", 1)[0])
            if not relative:
                continue
            target = (path.parent / relative).resolve()
            checked += 1
            if not target.is_relative_to(skill.resolve()) or not target.exists():
                errors.append(f"Broken or external local link in {path.relative_to(root)}: {link}")
    if not errors:
        print(f"ui-motion {version}: valid; {checked} local links; one skill entrypoint")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--tag", help="Require a release tag matching VERSION")
    args = parser.parse_args()
    try:
        errors = validate(args.root, args.tag)
    except (OSError, UnicodeError) as error:
        errors = [str(error)]
    for error in errors:
        print(error, file=sys.stderr)
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
