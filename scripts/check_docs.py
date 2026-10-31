#!/usr/bin/env python3
"""Validate local Markdown links and translation coverage without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TRANSLATIONS = {
    "README.de.md",
    "README.es.md",
    "README.fr.md",
    "README.pt-BR.md",
    "README.ru.md",
    "README.uk.md",
    "README.zh-CN.md",
}
LICENSE_IDS = (
    "CC0-1.0",
    "Unlicense",
    "MIT",
    "BSL-1.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "Apache-2.0",
    "MPL-2.0",
    "EPL-2.0",
    "LGPL-2.1-only",
    "GPL-2.0-only",
    "GPL-3.0-only",
    "AGPL-3.0-only",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def local_link_targets(markdown_file: Path) -> list[Path]:
    """Return resolved targets for relative Markdown links in a document."""
    text = markdown_file.read_text(encoding="utf-8")
    targets: list[Path] = []

    for match in LINK_RE.finditer(text):
        destination = match.group(1).strip()
        if destination.startswith("<") and ">" in destination:
            destination = destination[1 : destination.index(">")]
        else:
            destination = destination.split(maxsplit=1)[0]

        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue

        target = (markdown_file.parent / unquote(parsed.path)).resolve()
        targets.append(target)

    return targets


def main() -> int:
    errors: list[str] = []
    translation_dir = ROOT / "i18n"
    actual_translations = {
        path.name for path in translation_dir.glob("README.*.md")
    }

    if actual_translations != EXPECTED_TRANSLATIONS:
        missing = sorted(EXPECTED_TRANSLATIONS - actual_translations)
        unexpected = sorted(actual_translations - EXPECTED_TRANSLATIONS)
        if missing:
            errors.append(f"Missing translation files: {', '.join(missing)}")
        if unexpected:
            errors.append(f"Unexpected translation files: {', '.join(unexpected)}")

    markdown_files = sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )
    for markdown_file in markdown_files:
        for target in local_link_targets(markdown_file):
            relative_source = markdown_file.relative_to(ROOT)
            try:
                relative_target = target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative_source}: local link escapes the repository: {target}")
                continue
            if not target.exists():
                errors.append(f"{relative_source}: broken local link to {relative_target}")

    translation_files = [translation_dir / name for name in sorted(EXPECTED_TRANSLATIONS)]
    coverage_files = [ROOT / "README.md", *translation_files]
    for document in coverage_files:
        if not document.is_file():
            continue
        text = document.read_text(encoding="utf-8")
        missing_ids = [license_id for license_id in LICENSE_IDS if license_id not in text]
        if missing_ids:
            errors.append(
                f"{document.relative_to(ROOT)}: missing SPDX identifiers: "
                + ", ".join(missing_ids)
            )

    index_file = translation_dir / "README.md"
    if index_file.is_file():
        linked_targets = set(local_link_targets(index_file))
        if (ROOT / "README.md").resolve() not in linked_targets:
            errors.append("i18n/README.md: English source is not listed")
        for translation in translation_files:
            if translation.resolve() not in linked_targets:
                errors.append(
                    f"i18n/README.md: translation is not listed: {translation.name}"
                )

    selector_documents = [ROOT / "README.md", *translation_files]
    expected_selector_targets = {translation.resolve() for translation in translation_files}
    for document in selector_documents:
        if not document.is_file():
            continue
        linked_targets = set(local_link_targets(document))
        english_source = (ROOT / "README.md").resolve()
        if document.resolve() != english_source and english_source not in linked_targets:
            errors.append(
                f"{document.relative_to(ROOT)}: language selector is missing the English source"
            )
        required_targets = set(expected_selector_targets)
        if document.resolve() in required_targets:
            # The current language is displayed as plain text, not a self-link.
            required_targets.remove(document.resolve())
        missing_targets = required_targets - linked_targets
        if missing_targets:
            missing_names = ", ".join(sorted(path.name for path in missing_targets))
            errors.append(
                f"{document.relative_to(ROOT)}: language selector is missing {missing_names}"
            )

    if errors:
        print("Documentation checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Documentation checks passed: {len(markdown_files)} Markdown files, "
        f"{len(translation_files)} translations, {len(LICENSE_IDS)} license identifiers."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
