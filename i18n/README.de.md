# GitHub-Lizenzleitfaden

> **Sprachen:** [English](../README.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Español](README.es.md) · Deutsch · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [Português (Brasil)](README.pt-BR.md)
>
> Ein praxisorientierter Überblick über die 13 in diesem Leitfaden behandelten Lizenzvorlagen. Die Auswahl von GitHub kann sich ändern. Prüfe vor der Entscheidung die [aktuelle GitHub-Dokumentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) und den vollständigen Lizenztext.

> **Hinweis:** Dieser Leitfaden dient ausschließlich der Information und ist keine Rechtsberatung. Die Pflichten hängen vom genauen Lizenztext, der Verbindung und Verbreitung der Software sowie vom anwendbaren Recht ab. Wenn die Wahl rechtliche oder geschäftliche Folgen hat, wende dich an eine qualifizierte Rechtsberatung.

## Kurzvergleich

Alle nachfolgend aufgeführten Lizenzen gestatten die kommerzielle Nutzung, sofern ihre Bedingungen eingehalten werden. Die Tabelle ist eine allgemeine Zusammenfassung und ersetzt nicht die Lektüre des Lizenztexts. Das Fehlen einer ausdrücklichen Patentlizenz entscheidet für sich allein nicht darüber, ob andere Patentrechte gelten können.

| Lizenz (SPDX-Kennung) | Lizenzfamilie | Wichtigste Pflicht (vereinfacht) | Ausdrückliche Patentlizenz |
| :--- | :--- | :--- | :---: |
| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`) | Verzicht auf Rechte / Gemeinfreiheit | Keine urheberrechtlichen Bedingungen, soweit der Verzicht wirksam ist; gesetzliche Grenzen können gelten. | Nein |
| [The Unlicense](https://unlicense.org/) (`Unlicense`) | Verzicht auf Rechte / Gemeinfreiheit | Keine urheberrechtlichen Bedingungen, soweit die Widmung wirksam ist; gesetzliche Grenzen können gelten. | Nein |
| [MIT License](https://opensource.org/license/mit) (`MIT`) | Permissiv | Urheberrechtsvermerk und Lizenztext in Kopien oder wesentlichen Teilen beibehalten. | Nicht ausdrücklich |
| [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`) | Permissiv | Vorgeschriebene Hinweise in Quelltext-Distributionen beibehalten; für reine Objektcode-Distributionen gilt eine Ausnahme. | Nicht ausdrücklich |
| [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`) | Permissiv | Urheberrechtsvermerk, Bedingungen und Haftungsausschluss in Quell- und Binärdistributionen beibehalten. | Nicht ausdrücklich |
| [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`) | Permissiv | Anforderungen von BSD-2-Clause sowie Verbot einer nicht genehmigten Werbung mit Namen der Mitwirkenden. | Nicht ausdrücklich |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`) | Permissiv | Hinweise beibehalten, geänderte Dateien kennzeichnen und gegebenenfalls erforderliche `NOTICE`-Angaben übernehmen. | Ja |
| [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`) | Schwacher Copyleft | Bei der Weitergabe abgedeckter Software den Quelltext geänderter MPL-Dateien unter der MPL bereitstellen. | Ja |
| [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`) | Schwacher Copyleft | Für das abgedeckte Programm und Beiträge gilt EPL-2.0; für andere Teile können andere Bedingungen gelten. | Ja |
| [GNU LGPL v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`) | Schwacher Copyleft | Änderungen an der Bibliothek weitergeben und bei kombinierten Werken das erneute Verknüpfen oder Ersetzen ermöglichen. | Nicht ausdrücklich |
| [GNU GPL v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`) | Starker Copyleft | Bei der Weitergabe eines abgedeckten Werks dessen Quelltext unter GPL-2.0 bereitstellen; der Umfang hängt von der Verbindung der Komponenten ab. | Nicht ausdrücklich |
| [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`) | Starker Copyleft | Die Quelltextpflichten der GPL gelten für abgedeckte Werke; zusätzliche Bestimmungen betreffen Patente und bestimmte gesperrte Geräte. | Ja |
| [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`) | Netzwerk-Copyleft | Zusätzlich zu GPL-Bedingungen muss Nutzern einer geänderten Version, die über ein Netzwerk damit interagieren, der zugehörige Quelltext angeboten werden. | Ja |

## Lizenzüberblick

### Widmungen zur Gemeinfreiheit

#### [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`)
CC0 soll weltweit auf Urheber- und verwandte Rechte verzichten und enthält eine Ersatzlizenz für Fälle, in denen ein solcher Verzicht rechtlich unwirksam ist. Der Text verzichtet nicht auf Patent- oder Markenrechte. CC0 kann für Datensätze, Medien, Dokumentation oder kleine Codebeispiele geeignet sein, wenn eine möglichst freie Weiternutzung ohne Namensnennung gewünscht ist. Wenn eine ausdrückliche Patentlizenz wichtig ist, ist CC0 möglicherweise nicht passend.

#### [The Unlicense](https://unlicense.org/) (`Unlicense`)
The Unlicense verbindet eine Widmung zur Gemeinfreiheit mit einer Ersatzgenehmigung. Sie ist kurz und auf Software ausgerichtet, enthält aber keine ausdrückliche Patentlizenz. Prüfe, ob ihre Formulierungen und die Wirkung einer Gemeinfreiheitswidmung in den relevanten Rechtsordnungen geeignet sind.

### Permissive Lizenzen

#### [MIT License](https://opensource.org/license/mit) (`MIT`)
Eine kurze permissive Lizenz, die Nutzung, Änderung, Weitergabe, Unterlizenzierung und Verkauf des Codes erlaubt. In Kopien oder wesentlichen Teilen müssen der Urheberrechtsvermerk und der Lizenztext erhalten bleiben. Eine ausdrückliche Patentlizenz enthält der Text nicht.

#### [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`)
Eine permissive Lizenz, die häufig für Bibliotheken verwendet wird. Die Hinweis-Pflichten gelten im Allgemeinen für Quelltextkopien und abgeleitete Werke; für Distributionen, die ausschließlich aus maschinenausführbarem Objektcode bestehen, gibt es eine Ausnahme. Die genauen Bedingungen stehen im Lizenztext. Eine ausdrückliche Patentlizenz enthält sie nicht.

#### [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`)
Erlaubt die Weitergabe und Nutzung in Quell- und Binärform, mit oder ohne Änderungen. In beiden Fällen müssen Urheberrechtsvermerk, Bedingungen und Haftungsausschluss beibehalten werden.

#### [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`)
Enthält die Bedingungen von BSD-2-Clause und ergänzt eine Nicht-Unterstützungsklausel: Namen von Urhebern oder Mitwirkenden dürfen ohne vorherige Genehmigung nicht zur Unterstützung oder Bewerbung eines abgeleiteten Produkts verwendet werden.

#### [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`)
Eine permissive Lizenz mit ausdrücklicher Patentlizenz und einer Klausel, die die Patentlizenz bei bestimmten Patentklagen beendet. Außerdem müssen vorgeschriebene Hinweise erhalten, geänderte Dateien gekennzeichnet und gegebenenfalls `NOTICE`-Inhalte übernommen werden.

### Lizenzen mit schwachem Copyleft

#### [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`)
MPL-2.0 wendet Copyleft auf Dateiebene an. Bei der Weitergabe abgedeckter Software muss der Quelltext der MPL-Dateien einschließlich ihrer Änderungen unter der MPL verfügbar sein. Ein größeres Werk darf separat lizenzierte Dateien enthalten, sofern die Bedingungen der MPL eingehalten werden.

#### [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`)
EPL-2.0 ist eine unternehmensfreundliche Lizenz mit schwachem Copyleft und ausdrücklicher Patentlizenz. Sie gilt für abgedeckte Beiträge und abgeleitete Werke; für getrennte Teile eines größeren Werks können andere Bedingungen gelten, wenn die Anforderungen der EPL erfüllt sind. Prüfe vor der Verbindung von Code die Definitionen und Weitergabebedingungen.

#### [GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`)
LGPL-2.1 ist für Bibliotheken gedacht. Bei Einhaltung ihrer Bedingungen kann eine LGPL-Bibliothek zusammen mit einer proprietären Anwendung genutzt werden. Änderungen an der abgedeckten Bibliothek bleiben unter der LGPL; bei der Weitergabe eines kombinierten Werks müssen Empfänger die Bibliothek ändern oder ersetzen können. Statisches Verknüpfen kann zusätzliche Schritte erfordern.

### Starker und Netzwerk-Copyleft

#### [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`)
Wird ein von GPL-2.0 abgedecktes Werk weitergegeben, müssen sein Quelltext und die GPL-Rechte bereitgestellt werden. Ob eine Verbindung von Programmen abgedeckt ist, hängt von den Umständen und der Lizenz ab; die Ablage im selben Repository entscheidet dies nicht allein. GPL-2.0 enthält keine ausdrückliche Patentlizenz und keine Installationsinformationen, wie sie GPL-3.0 für bestimmte Fälle vorsieht.

#### [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`)
GPL-3.0 sieht starken Copyleft für abgedeckte Werke vor und enthält eine ausdrückliche Patentlizenz. Sie behandelt außerdem bestimmte Gerätesperren und Einschränkungen, die verhindern, dass Nutzer ihre Lizenzrechte ausüben. Die Pflichten gelten nach Maßgabe des Lizenztexts und nicht automatisch für jedes separate Programm, das daneben verwendet wird.

#### [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`)
AGPL-3.0 basiert auf GPL-3.0 und ergänzt eine Bedingung für die Netzwerknutzung. Ermöglicht eine geänderte Version eines abgedeckten Programms die Interaktion über ein Netzwerk, muss den Nutzern der entsprechende Quelltext angeboten werden. Dies gilt für abgedeckte Software und ist keine pauschale Regel für jeden Dienst oder jede Abhängigkeit.

## Eine Lizenz auswählen

- **Möglichst freie Weiternutzung mit wenigen Bedingungen:** CC0 oder The Unlicense erwägen und zuvor die Wirkung der Widmung sowie die Patentbedingungen prüfen.
- **Einfache permissive Bedingungen:** MIT ist knapp; BSD-2-Clause und BSD-3-Clause beschreiben Weitergabebedingungen ausdrücklich. BSD-3-Clause regelt zusätzlich die Verwendung zur Unterstützung oder Bewerbung.
- **Ausdrückliche Patentlizenz benötigt:** Apache-2.0 erwägen. Auch MPL-2.0, EPL-2.0 und GPL-3.0 enthalten Patentbestimmungen, haben jedoch unterschiedliche Copyleft-Bereiche.
- **Änderungen an Bibliotheken oder abgedeckten Dateien offenlegen, ein größeres proprietäres Werk aber ermöglichen:** LGPL-2.1, MPL-2.0 und EPL-2.0 vergleichen; ihre Grenzen und Pflichten unterscheiden sich.
- **Quelltext für weitergegebene abgedeckte Werke verlangen:** GPL-2.0 oder GPL-3.0 prüfen. Für die jeweilige Netzwerknutzung AGPL-3.0 prüfen.
- **Bei reinen Objektcode-Distributionen keine Hinweise mitführen:** Die konkrete Ausnahme in BSL-1.0 prüfen.

Diese Punkte sind eine erste Orientierung und keine Rechtsberatung. Lies den vollständigen Lizenztext und prüfe die Kompatibilität mit Code aus anderen Projekten.

## Weiterführende Informationen

- [GitHub: Ein Repository lizenzieren](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [SPDX-Lizenzliste](https://spdx.org/licenses/)
- Vollständige Lizenztexte über die obigen Links

## Mitwirken

Die englische Version ist die Ausgangsfassung. Hinweise zur Dokumentation und Übersetzung findest du in [CONTRIBUTING.md](../CONTRIBUTING.md); alle Übersetzungen sind im [i18n-Index](README.md) aufgeführt.

## Lizenz der Inhalte

Dieser Leitfaden und seine Übersetzungen sind unter [CC0 1.0](../LICENSE) der Gemeinfreiheit gewidmet. Die verlinkten Lizenztexte gehören ihren jeweiligen Rechteinhabern und werden hier nicht neu lizenziert.
