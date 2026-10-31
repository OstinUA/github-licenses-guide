# Guia de licenças do GitHub

> **Idiomas:** [English](../README.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · Português (Brasil)
>
> Uma visão prática dos 13 modelos de licença abordados neste guia. A lista de modelos do GitHub pode mudar; antes de escolher, consulte a [documentação atual do GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) e o texto integral da licença.

> **Aviso:** este guia é apenas informativo e não constitui aconselhamento jurídico. As obrigações dependem do texto exato da licença, de como o software é combinado e distribuído e da legislação aplicável. Se a escolha tiver consequências jurídicas ou comerciais, procure um profissional qualificado.

## Comparação rápida

Todas as licenças abaixo permitem uso comercial, desde que seus termos sejam cumpridos. A tabela é um resumo geral e não substitui a leitura da licença. A ausência de uma concessão expressa de patente, por si só, não determina se outros direitos de patente podem ser aplicáveis.

| Licença (identificador SPDX) | Categoria | Principal obrigação (resumida) | Concessão expressa de patente |
| :--- | :--- | :--- | :---: |
| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`) | Dedicação ao domínio público | Não há condições de direitos autorais onde a renúncia for válida; podem existir limites legais. | Não |
| [The Unlicense](https://unlicense.org/) (`Unlicense`) | Dedicação ao domínio público | Não há condições de direitos autorais onde a dedicação for válida; podem existir limites legais. | Não |
| [MIT License](https://opensource.org/license/mit) (`MIT`) | Permissiva | Mantenha o aviso de direitos autorais e o texto da licença nas cópias ou partes substanciais. | Não expressa |
| [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`) | Permissiva | Mantenha os avisos exigidos nas distribuições de código-fonte; há uma exceção para distribuições somente de código-objeto executável. | Não expressa |
| [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`) | Permissiva | Mantenha o aviso de direitos autorais, as condições e a isenção de responsabilidade nas distribuições de código-fonte e binárias. | Não expressa |
| [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`) | Permissiva | Requisitos da BSD-2-Clause e proibição de endosso não autorizado usando os nomes dos colaboradores. | Não expressa |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`) | Permissiva | Preserve os avisos, identifique os arquivos alterados e inclua o material `NOTICE` exigido, quando aplicável. | Sim |
| [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`) | Copyleft fraco | Ao distribuir software abrangido, forneça aos destinatários sob a MPL o código-fonte dos arquivos MPL modificados. | Sim |
| [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`) | Copyleft fraco | O programa e as contribuições abrangidos estão sujeitos à EPL-2.0; outras partes podem ter termos diferentes. | Sim |
| [GNU LGPL v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`) | Copyleft fraco | Compartilhe alterações na biblioteca e permita sua religação ou substituição em uma obra combinada. | Não expressa |
| [GNU GPL v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`) | Copyleft forte | Ao distribuir uma obra abrangida, forneça seu código-fonte sob a GPL-2.0; o alcance depende de como o código é combinado. | Não expressa |
| [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`) | Copyleft forte | As obrigações de código-fonte da GPL se aplicam às obras abrangidas; há regras adicionais sobre patentes e determinados dispositivos bloqueados. | Sim |
| [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`) | Copyleft de rede | Além dos termos da GPL, ofereça o código-fonte correspondente aos usuários que interagem pela rede com uma versão modificada. | Sim |

## Resumo das licenças

### Dedicações ao domínio público

#### [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0-1.0`)
A CC0 busca renunciar mundialmente aos direitos autorais e direitos conexos e prevê uma licença alternativa quando a renúncia não for juridicamente válida. Seu texto não renuncia a direitos de patente nem de marca. Pode ser adequada para conjuntos de dados, mídia, documentação ou pequenos trechos de código quando se pretende permitir ampla reutilização sem atribuição; pode não ser apropriada quando uma concessão expressa de patente for importante.

#### [The Unlicense](https://unlicense.org/) (`Unlicense`)
A Unlicense combina uma dedicação ao domínio público com uma autorização alternativa. É curta e voltada a software, mas não concede expressamente direitos de patente. Verifique se sua redação e os efeitos jurídicos da dedicação são adequados às jurisdições relevantes.

### Licenças permissivas

#### [MIT License](https://opensource.org/license/mit) (`MIT`)
Uma licença permissiva e concisa que permite usar, modificar, distribuir, sublicenciar e vender o código. Cópias ou partes substanciais devem manter o aviso de direitos autorais e o texto da licença. O texto não inclui concessão expressa de patente.

#### [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt) (`BSL-1.0`)
Uma licença permissiva frequentemente usada para bibliotecas. Em geral, os requisitos de avisos se aplicam a cópias do código-fonte e obras derivadas; há uma exceção para distribuições constituídas apenas por código-objeto executável por máquina. Consulte o texto para conhecer as condições exatas. Não há concessão expressa de patente.

#### [BSD 2-Clause](https://opensource.org/license/bsd-2-clause) (`BSD-2-Clause`)
Permite redistribuir e usar o software nas formas de código-fonte e binária, com ou sem modificações. Em ambos os casos, é necessário manter o aviso de direitos autorais, as condições e a isenção de responsabilidade.

#### [BSD 3-Clause](https://opensource.org/license/bsd-3-clause) (`BSD-3-Clause`)
Inclui as condições da BSD-2-Clause e acrescenta uma cláusula de não endosso: os nomes dos autores ou colaboradores não podem ser usados para endossar ou promover um produto derivado sem autorização prévia.

#### [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`Apache-2.0`)
Uma licença permissiva com concessão expressa de patente e uma cláusula que pode encerrar essa concessão em determinadas ações judiciais de patente. Também exige preservar os avisos especificados, identificar arquivos modificados e incluir o conteúdo do `NOTICE`, quando aplicável.

### Licenças de copyleft fraco

#### [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) (`MPL-2.0`)
A MPL-2.0 aplica copyleft no nível do arquivo. Ao distribuir software abrangido, o código-fonte dos arquivos sob MPL — inclusive suas modificações — deve ser disponibilizado sob a MPL. Uma obra maior pode incluir arquivos licenciados separadamente sob outros termos, desde que as condições da MPL sejam cumpridas.

#### [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) (`EPL-2.0`)
A EPL-2.0 é uma licença de copyleft fraco, favorável a empresas e com concessão expressa de patente. Ela rege contribuições e obras derivadas abrangidas; outras partes de uma obra maior podem ter termos diferentes se os requisitos da EPL forem atendidos. Antes de combinar código, verifique as definições e condições de distribuição.

#### [GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) (`LGPL-2.1-only`)
A LGPL-2.1 foi criada para bibliotecas. Se seus termos forem cumpridos, uma biblioteca LGPL pode ser usada com um aplicativo proprietário. Alterações na biblioteca abrangida continuam sob a LGPL; quem distribui uma obra combinada deve permitir que os destinatários modifiquem ou substituam a biblioteca. A ligação estática pode exigir etapas adicionais.

### Copyleft forte e de rede

#### [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) (`GPL-2.0-only`)
Ao distribuir uma obra abrangida pela GPL-2.0, é necessário fornecer seu código-fonte e os direitos previstos pela GPL. Saber se uma combinação de programas está abrangida depende dos fatos e da licença; estar no mesmo repositório não determina isso por si só. A GPL-2.0 não contém concessão expressa de patente nem os requisitos de informações de instalação previstos pela GPL-3.0.

#### [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) (`GPL-3.0-only`)
A GPL-3.0 estabelece copyleft forte para obras abrangidas e inclui concessão expressa de patente. Também trata de determinadas formas de bloqueio de dispositivos e de restrições que impedem os usuários de exercer os direitos concedidos pela licença. As obrigações se aplicam conforme descritas no texto, não automaticamente a todo programa separado utilizado em conjunto.

#### [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html) (`AGPL-3.0-only`)
A AGPL-3.0 é baseada na GPL-3.0 e acrescenta uma condição de uso em rede. Se uma versão modificada de um programa abrangido permitir interação remota pela rede, o código-fonte correspondente deve ser oferecido a esses usuários. A condição se aplica ao software abrangido e não é uma regra geral para todo serviço ou dependência.

## Como escolher uma licença

- **Você quer permitir ampla reutilização com poucas condições:** considere CC0 ou The Unlicense, depois de verificar os efeitos da dedicação e os termos de patente.
- **Você quer termos permissivos simples:** a MIT é concisa; BSD-2-Clause e BSD-3-Clause descrevem claramente as condições de redistribuição, e a BSD-3-Clause também trata de endosso e promoção.
- **Você precisa de concessão expressa de patente:** considere Apache-2.0; MPL-2.0, EPL-2.0 e GPL-3.0 também incluem disposições sobre patentes, mas têm alcances de copyleft diferentes.
- **Você quer compartilhar alterações em uma biblioteca ou arquivos abrangidos, mas permitir uma obra proprietária maior:** compare LGPL-2.1, MPL-2.0 e EPL-2.0; seus limites e obrigações diferem.
- **Você quer exigir o código-fonte de obras abrangidas distribuídas:** avalie GPL-2.0 ou GPL-3.0. Para determinados usos em rede, avalie AGPL-3.0.
- **Você quer evitar avisos em distribuições somente de código-objeto:** confira a exceção específica da BSL-1.0.

Esses pontos são apenas uma orientação inicial, não uma recomendação jurídica. Leia o texto integral e verifique a compatibilidade com o código de outros projetos.

## Para saber mais

- [GitHub: Licenciar um repositório](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [Lista de licenças SPDX](https://spdx.org/licenses/)
- Textos integrais das licenças nos links acima

## Como contribuir

A versão em inglês é a fonte. Consulte [CONTRIBUTING.md](../CONTRIBUTING.md) para as diretrizes de documentação e tradução ou acesse o [índice de traduções](README.md).

## Licença do conteúdo

Este guia e suas traduções são dedicados ao domínio público sob [CC0 1.0](../LICENSE). Os textos das licenças mencionadas pertencem aos respectivos titulares e não são relicenciados aqui.
