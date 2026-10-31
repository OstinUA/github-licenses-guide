# Contributing

Thanks for helping improve the GitHub Licenses Guide. Contributions may include corrections, clearer explanations, link fixes, and translations.

## Documentation source

- The root [`README.md`](README.md) is the English source of truth.
- Translations are maintained in [`i18n/`](i18n/README.md).
- Keep the 13 licenses, their order, SPDX identifiers, and official license links consistent across every language.
- Preserve the meaning and scope of legal summaries. Avoid absolute claims such as “this always makes the whole project open source”; obligations depend on the license text and how a work is used or distributed.
- Keep the educational disclaimer. This guide is not legal advice, and a translation must not imply that it is an official translation of a license.
- When changing a summary, check the full license text and update every translation that describes the affected point.

## Adding or updating a translation

1. Translate the current root `README.md`; do not translate SPDX identifiers, code, or official license names.
2. Add or update `i18n/README.<locale>.md`, using a BCP 47 locale suffix where appropriate (for example, `README.pt-BR.md`).
3. Update the language selector in the root README and every translated guide.
4. Add the language to `i18n/README.md` and to the expected locale list in `scripts/check_docs.py`.
5. Check that local links work and all 13 SPDX identifiers remain present.

Translations are welcome even if they are initially machine-assisted, but they should be reviewed for accuracy and natural phrasing before being described as complete.

## Checks

The repository has a dependency-free Markdown check. Run it from the repository root:

```sh
python3 scripts/check_docs.py
```

The check verifies local Markdown links, the translation inventory, language-selector links, and license identifier coverage. Please run it before opening a pull request.
