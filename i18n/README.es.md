# Guía de licencias de GitHub

> **Idiomas:** [English](../README.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · Español · [Deutsch](README.de.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [Português (Brasil)](README.pt-BR.md)
>
> Una guía práctica de las 13 plantillas de licencia cubiertas aquí. La lista de plantillas de GitHub puede cambiar; antes de elegir, consulta la [documentación vigente de GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) y el texto completo de la licencia.

> **Aviso:** Esta guía tiene fines educativos y no constituye asesoramiento jurídico. Las obligaciones dependen del texto exacto de la licencia, de cómo se combine y distribuya el software y de la legislación aplicable. Si la elección tiene consecuencias jurídicas o comerciales, consulta a un profesional cualificado.

## Comparación rápida

Todas las licencias siguientes permiten el uso comercial si se cumplen sus condiciones. La tabla es un resumen general, no sustituye la lectura de la licencia. La ausencia de una concesión expresa de patentes no determina por sí sola si pueden aplicarse otros derechos de patente.

| Licencia (identificador SPDX) | Familia | Obligación principal (simplificada) | Concesión expresa de patentes |
| :--- | :--- | :--- | :---: |
| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`) | Dedicación al dominio público | No impone condiciones de copyright cuando la renuncia es efectiva; pueden aplicarse límites legales. | No |
| [The Unlicense](https://unlicense.org/) (`Unlicense`) | Dedicación al dominio público | No impone condiciones de copyright cuando la dedicación es efectiva; pueden aplicarse límites legales. | No |
| [MIT License](https://opensource.org/license/mit) (`MIT`) | Permisiva | Conserva el aviso de copyright y el texto de permiso en las copias o partes sustanciales. | No expresa |
| [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`) | Permisiva | Conserva los avisos exigidos en las distribuciones de código fuente; hay una excepción para distribuciones solo en código objeto ejecutable. | No expresa |
| [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`) | Permisiva | Conserva el aviso de copyright, las condiciones y la exención de responsabilidad en distribuciones fuente y binarias. | No expresa |
| [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`) | Permisiva | Requisitos de BSD-2-Clause y prohibición de promocionar productos con los nombres de los colaboradores sin permiso. | No expresa |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`) | Permisiva | Conserva los avisos, identifica los archivos modificados e incluye el material `NOTICE` cuando corresponda. | Sí |
| [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`) | Copyleft débil | Al distribuir software cubierto, pon a disposición de sus destinatarios el código fuente de los archivos MPL modificados bajo la MPL. | Sí |
| [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`) | Copyleft débil | El programa y las contribuciones cubiertos están sujetos a EPL-2.0; otras partes pueden tener términos distintos. | Sí |
| [GNU LGPL v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`) | Copyleft débil | Comparte los cambios a la biblioteca y permite volver a enlazarla o sustituirla en una obra combinada. | No expresa |
| [GNU GPL v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`) | Copyleft fuerte | Al distribuir una obra cubierta, proporciona su fuente bajo GPL-2.0; el alcance depende de cómo se combine el código. | No expresa |
| [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`) | Copyleft fuerte | Las obligaciones de proporcionar el código fuente se aplican a las obras cubiertas; incluye disposiciones adicionales sobre patentes y ciertos dispositivos bloqueados. | Sí |
| [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`) | Copyleft de red | Además de las condiciones de GPL, ofrece el código fuente correspondiente a quienes interactúan por red con una versión modificada. | Sí |

## Resumen de las licencias

### Dedicaciones al dominio público

#### [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`)
CC0 intenta renunciar mundialmente a los derechos de autor y derechos conexos, e incluye una licencia alternativa cuando la renuncia no es jurídicamente efectiva. Su texto no renuncia a derechos de patentes ni de marcas. Puede servir para conjuntos de datos, medios, documentación o fragmentos pequeños cuando se busca una reutilización amplia sin atribución; quizá no sea adecuada si se necesita una concesión expresa de patentes.

#### [The Unlicense](https://unlicense.org/) (`Unlicense`)
The Unlicense combina una dedicación al dominio público con una autorización alternativa. Es breve y está pensada para software, pero no concede expresamente derechos de patente. Comprueba si su redacción y los efectos de la dedicación son adecuados en las jurisdicciones pertinentes.

### Licencias permisivas

#### [MIT License](https://opensource.org/license/mit) (`MIT`)
Una licencia permisiva y breve que permite usar, modificar, distribuir, sublicenciar y vender el código. Las copias o partes sustanciales deben conservar el aviso de copyright y el texto de permiso. No contiene una concesión expresa de patentes.

#### [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`)
Una licencia permisiva utilizada a menudo para bibliotecas. Sus requisitos de avisos suelen aplicarse a las copias fuente y a las obras derivadas; existe una excepción para las distribuciones compuestas únicamente por código objeto ejecutable. Consulta el texto para conocer las condiciones exactas. No contiene una concesión expresa de patentes.

#### [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`)
Permite redistribuir y usar el software en forma de código fuente o binario, con o sin modificaciones. En ambos casos hay que conservar el aviso de copyright, las condiciones y la exención de responsabilidad.

#### [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`)
Incluye las condiciones de BSD-2-Clause y añade una cláusula de no respaldo: no se pueden usar los nombres de autores o colaboradores para respaldar o promocionar un producto derivado sin autorización previa.

#### [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`)
Licencia permisiva con concesión expresa de patentes y una disposición que puede extinguirla si se inicia cierto litigio de patentes. También exige conservar los avisos indicados, marcar los archivos modificados e incluir el contenido de `NOTICE` cuando corresponda.

### Licencias de copyleft débil

#### [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`)
MPL-2.0 aplica copyleft a nivel de archivo. Al distribuir software cubierto, el código fuente de los archivos bajo MPL —incluidas sus modificaciones— debe estar disponible bajo la MPL. Una obra más amplia puede incluir archivos con licencias distintas si se respetan las condiciones de la MPL.

#### [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`)
EPL-2.0 es una licencia de copyleft débil, favorable a la actividad empresarial y con concesión expresa de patentes. Rige las contribuciones y obras derivadas cubiertas; otras partes de una obra mayor pueden tener términos distintos si se cumplen sus requisitos. Antes de combinar código, revisa sus definiciones y condiciones de distribución.

#### [GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`)
LGPL-2.1 está pensada para bibliotecas. Permite usar una biblioteca junto con una aplicación propietaria si se cumplen sus condiciones. Los cambios a la biblioteca cubierta siguen sujetos a LGPL, y quien distribuya una obra combinada debe permitir que los destinatarios modifiquen o sustituyan la biblioteca; el enlace estático puede exigir pasos adicionales.

### Copyleft fuerte y de red

#### [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`)
Al distribuir una obra cubierta por GPL-2.0, hay que proporcionar su código fuente y los derechos previstos por GPL. Que una combinación de programas quede cubierta depende de los hechos y de la licencia; estar en el mismo repositorio no lo determina por sí solo. GPL-2.0 no contiene una concesión expresa de patentes ni los requisitos de información de instalación introducidos por GPL-3.0.

#### [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`)
GPL-3.0 establece copyleft fuerte para las obras cubiertas e incluye una concesión expresa de patentes. También aborda ciertas formas de bloqueo de dispositivos y restricciones que impiden ejercer los derechos otorgados por la licencia. Sus obligaciones se aplican según el texto de la licencia, no automáticamente a cualquier programa independiente que se use junto al código.

#### [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`)
AGPL-3.0 se basa en GPL-3.0 y añade una condición para el uso a través de una red. Si una versión modificada de un programa cubierto permite la interacción remota por red, debe ofrecerse a esos usuarios el código fuente correspondiente. La condición se aplica al software cubierto y no es una regla general para cualquier servicio o dependencia.

## Cómo elegir una licencia

- **Buscas una reutilización amplia con pocas condiciones:** considera CC0 o The Unlicense, tras comprobar sus efectos y sus términos sobre patentes.
- **Quieres condiciones permisivas sencillas:** MIT es concisa; BSD-2-Clause y BSD-3-Clause detallan condiciones de redistribución, y BSD-3-Clause también regula el respaldo o la promoción.
- **Necesitas una concesión expresa de patentes:** considera Apache-2.0; MPL-2.0, EPL-2.0 y GPL-3.0 también contienen disposiciones de patentes, pero con distintos alcances de copyleft.
- **Quieres compartir cambios a una biblioteca o archivos cubiertos y permitir una obra propietaria más amplia:** compara LGPL-2.1, MPL-2.0 y EPL-2.0; sus límites y obligaciones son distintos.
- **Quieres exigir el código fuente de obras cubiertas distribuidas:** revisa GPL-2.0 o GPL-3.0. Para determinados usos en red, revisa AGPL-3.0.
- **Quieres evitar avisos en distribuciones que solo contengan código objeto:** revisa la excepción específica de BSL-1.0.

Estos puntos son una orientación inicial, no una recomendación jurídica. Lee el texto completo y comprueba la compatibilidad con el código de otros proyectos.

## Más información

- [GitHub: Licenciar un repositorio](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [Lista de licencias SPDX](https://spdx.org/licenses/)
- Los textos completos enlazados en esta guía

## Contribuir

La versión en inglés es la fuente. Consulta [CONTRIBUTING.md](../CONTRIBUTING.md) para conocer las pautas de documentación y traducción, o visita el [índice de traducciones](README.md).

## Licencia del contenido

Esta guía y sus traducciones se dedican al dominio público bajo [CC0 1.0](../LICENSE). Los textos de las licencias enlazadas pertenecen a sus respectivos titulares y no se relicencian aquí.
