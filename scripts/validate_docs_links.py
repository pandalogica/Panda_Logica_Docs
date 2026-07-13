#!/usr/bin/env python3
"""Validate relative links and images in Panda_Logica_Docs Markdown sources."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def resolve_local(path: Path, target: str) -> Path:
    file_part = unquote(target.split("#", 1)[0].strip())
    return (path.parent / file_part).resolve()


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return errors

    for match in LINK_RE.finditer(text):
        target = match.group(2).strip().split()[0].strip("<>")
        if is_external(target) or target.startswith("/"):
            continue
        file_part = target.split("#", 1)[0]
        if not file_part:
            continue
        resolved = resolve_local(path, target)
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link target '{target}'")
        elif resolved.suffix.lower() == ".md" and resolved.stat().st_size == 0:
            errors.append(f"{path.relative_to(ROOT)}: link to empty stub '{target}'")

    for match in IMAGE_RE.finditer(text):
        target = match.group(2).strip().split()[0].strip("<>")
        if is_external(target):
            continue
        resolved = resolve_local(path, target)
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing image '{target}'")
        alt = match.group(1).strip()
        if not alt:
            errors.append(f"{path.relative_to(ROOT)}: image missing alt text ({target})")

    return errors


def main() -> int:
    if not DOCS_ROOT.exists():
        print(f"Docs root not found: {DOCS_ROOT}", file=sys.stderr)
        return 2

    errors: list[str] = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        errors.extend(check_file(path))

    if errors:
        print(f"Found {len(errors)} documentation link/image issue(s):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Documentation links and images OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
