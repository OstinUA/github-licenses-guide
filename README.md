# GitHub Licenses Guide

> **Languages:** English · [Русский](i18n/README.ru.md) · [Українська](i18n/README.uk.md) · [Español](i18n/README.es.md) · [Deutsch](i18n/README.de.md) · [Français](i18n/README.fr.md) · [简体中文](i18n/README.zh-CN.md) · [Português (Brasil)](i18n/README.pt-BR.md)
>
> A practical overview of the 13 license templates covered by this guide. GitHub's available templates can change; check the [current GitHub documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) and the full license text before choosing one.

> **Disclaimer:** This guide is for education only and is not legal advice. Obligations depend on the exact license text, how software is combined and distributed, and applicable law. If the choice has legal or business consequences, consult a qualified lawyer.

## At a glance

All of the licenses below permit commercial use, provided their terms are followed. The table is a high-level summary, not a substitute for reading the license. “No explicit patent grant” does not, by itself, determine whether other patent rights may apply.

| License (SPDX identifier) | Family | Main compliance point (simplified) | Explicit patent grant |
| :--- | :--- | :--- | :---: |
| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`) | Public-domain dedication | No copyright conditions where the waiver is effective; legal limits may apply. | No |
| [The Unlicense](https://unlicense.org/) (`Unlicense`) | Public-domain dedication | No copyright conditions where the dedication is effective; legal limits may apply. | No |
| [MIT License](https://opensource.org/license/mit) (`MIT`) | Permissive | Include the copyright and permission notice in copies or substantial portions. | No express grant |
| [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`) | Permissive | Preserve required notices in source distributions; object-code-only distributions are excepted. | No express grant |
| [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`) | Permissive | Retain the copyright notice, conditions, and disclaimer in source and binary distributions. | No express grant |
| [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`) | Permissive | BSD-2-Clause requirements, plus no unauthorized endorsement using contributor names. | No express grant |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`) | Permissive | Preserve notices, identify changed files, and include any required `NOTICE` material. | Yes |
| [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`) | Weak copyleft | When distributing covered software, make source for modified MPL-covered files available under the MPL. | Yes |
| [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`) | Weak copyleft | The covered program and contributions are subject to EPL-2.0 terms; other parts may use different terms. | Yes |
| [GNU LGPL v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`) | Weak copyleft | Share changes to the library and meet the relinking or replacement requirements for combined works. | No express grant |
| [GNU GPL v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`) | Strong copyleft | When distributing a covered work, provide its source under GPL-2.0; coverage depends on the work and how it is combined. | No express grant |
| [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`) | Strong copyleft | GPL source-sharing requirements apply to covered works; additional terms address patents and certain locked-down devices. | Yes |
| [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`) | Network copyleft | In addition to GPL-style terms, users interacting remotely with a modified version must be offered its corresponding source. | Yes |

## License summaries

### Public-domain-style dedications

#### [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`)
CC0 attempts to waive copyright and related rights worldwide, with a fallback license where a waiver is not legally effective. Its text does not waive patent or trademark rights. It can suit datasets, media, documentation, or small snippets when broad reuse without attribution is intended; it may not be appropriate when an express patent grant is important.

#### [The Unlicense](https://unlicense.org/) (`Unlicense`)
The Unlicense combines a public-domain dedication with a fallback permission. It is short and software-focused, but it does not provide an express patent grant. Consider whether its wording and the effect of a public-domain dedication work in the relevant jurisdictions.

### Permissive licenses

#### [MIT License](https://opensource.org/license/mit) (`MIT`)
A short, permissive license that allows use, modification, distribution, sublicensing, and sale. Copies or substantial portions must retain the copyright and permission notice. The text has no express patent grant.

#### [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`)
A permissive license often used for libraries. Its notice requirements generally apply to source copies and derivative works; the license has an exception for distributions consisting solely of machine-executable object code. Read the license text for the exact conditions. It has no express patent grant.

#### [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`)
A permissive license allowing redistribution and use in source and binary forms, with or without modification. Both forms must retain the copyright notice, conditions, and disclaimer.

#### [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`)
Includes the BSD-2-Clause conditions and adds a non-endorsement clause: contributors' names cannot be used to endorse or promote a derived product without prior permission.

#### [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`)
A permissive license with an express patent license and a patent-litigation termination provision. It also requires preserving specified notices, marking modified files, and carrying forward `NOTICE` content when applicable.

### Weak-copyleft licenses

#### [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`)
MPL-2.0 uses file-level copyleft. When distributing covered software, source for MPL-covered files—including modifications to those files—must be made available under the MPL. A larger work can include separately licensed files, subject to the license's conditions.

#### [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`)
EPL-2.0 is a business-friendly weak-copyleft license with an express patent grant. The license governs covered contributions and derivative works; separate parts of a larger work may use other terms when the EPL's requirements are met. Review its definitions and distribution conditions before combining code.

#### [GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`)
LGPL-2.1 is designed for libraries. It allows use with a proprietary application when its conditions are followed. Changes to the LGPL-covered library remain under the LGPL, and distributors of a combined work must meet requirements that let recipients modify or replace the library; static linking can require extra steps.

### Strong and network copyleft

#### [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`)
GPL-2.0 requires source and GPL permissions when a covered work is distributed. Whether a combination forms a covered work depends on the facts and the license; simply being in the same repository does not settle that question. GPL-2.0 has no express patent grant and does not include GPL-3.0's installation-information provisions.

#### [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`)
GPL-3.0 has strong copyleft for covered works and adds an express patent license. It also addresses certain forms of device lock-down and restrictions that interfere with users' exercise of license rights. Its obligations apply as described in the license, not automatically to every separate program used alongside it.

#### [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`)
AGPL-3.0 is based on GPL-3.0 and adds a network-use condition. When a modified version is used to provide remote interaction over a network, users interacting with it must be offered the corresponding source. The requirement applies to covered software and should not be read as a blanket rule for every service or dependency.

## Choosing a license

- **Broad reuse with minimal conditions:** consider CC0 or The Unlicense, after checking how their dedication and patent terms fit your needs.
- **Simple permissive terms:** MIT is concise; BSD-2-Clause and BSD-3-Clause add clear redistribution conditions, with BSD-3-Clause also addressing endorsement.
- **An express patent grant:** consider Apache-2.0; MPL-2.0, EPL-2.0, and GPL-3.0 also include patent provisions, each with a different copyleft scope.
- **Share changes to a library or covered files while allowing a larger proprietary work:** compare LGPL-2.1, MPL-2.0, and EPL-2.0—their boundaries and obligations differ.
- **Require source for covered distributed works:** review GPL-2.0 or GPL-3.0. For qualifying network use, review AGPL-3.0.
- **Need to avoid carrying notices in object-code-only distributions:** review the specific exception in BSL-1.0.

These are starting points, not legal recommendations. Read the full terms, including compatibility requirements for code from other projects.

## Further reading

- [GitHub: Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [SPDX License List](https://spdx.org/licenses/)
- The full text of each license linked above

## Contributing

English is the source version. See [CONTRIBUTING.md](CONTRIBUTING.md) for documentation and translation guidelines, or visit the [translation index](i18n/README.md).

## Content license

The guide and its translations are dedicated to the public domain under [CC0 1.0](LICENSE). The license texts linked in this guide belong to their respective authors and are not relicensed here.
