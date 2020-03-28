# CoronaBR
[![goodtables.io](https://goodtables.io/badge/github/belisards/coronabr.svg)](https://goodtables.io/github/belisards/coronabr)

Dados e scripts para extrair a série histórica da pandemia COVID-19 no Brasil, de acordo com o Ministério da Saúde.

## Sobre os dados

No arquivo [corona_brasil.csv](https://github.com/belisards/coronabr/blob/master/dados/corona_brasil.csv), você encontra a série histórica dos casos de COVID-19 segundo o Ministério da Saúde, desde de 30 janeiro de 2020. Saiba mais sobre a [metodologia de extração e compilação dos dados abaixo](https://github.com/belisards/coronabr/tree/master/dados).

## Como interpretar os dados?

A tabela é baseada no formato originalmente adotado pelo Ministério da Saúde para armazenas os dados da COVID-19 na Plataforma Integrada de Vigilância em Saúde. Atualmente, porém, o órgão disponibiliza apenas números de óbitos e casos confirmados. 

* uid = Número de identificação da UF adotado pela Plataforma IVIS. 
* suspects = Casos suspeitos
* refuses = Descartados
* confirmado = A coluna parece nunca ter sido utilizada.
* deads = Mortes/Óbitos
* local = A coluna parece nunca ter sido utilizada.
* cases = Casos confirmados
* comments = Comentário sobre os dados adicionados na Plataforma IVIS (Ex: "Transmissão comunitária no município do Rio de Janeiro" ou "1 Portador assintomático")
* broadcast = Coluna não identificada.
* date = Data de registro dos dados (%dd/%mm/%yyyy)
* time = Hora do registro dos dados  (%hh:%mm), quando eram atualizados na Plataforma IVIS
* uf = Coluna com a sigla da UF

### Licença dos dados
A base de dados `corona-br` é disponibilizada sob a licença Open Database License: [http://opendatacommons.org/licenses/odbl/1.0/](http://opendatacommons.org/licenses/odbl/1.0/). 


## Outros projetos

* Lista colaborativa no [fórum Dados Abertos](https://dadosabertos.social/t/dados-sobre-a-pandemia-do-novo-coronavirus/267);

* Painel e projeções do [Observatório COVID-19 BR](https://covid19br.github.io/)

* O [Brasil.IO](https://brasil.io/dataset/covid19/boletim) está consolidando uma base de dados com os boletins informativos sobre COVID-19 no Brasil.

* Kaggle Corona-Virus-Brazil: o mesmo dataset da plataforma IVIS encontra-se disponível neste [repositório do Kaggle](https://www.kaggle.com/unanimad/corona-virus-brazil).

* Para um levantamento realizado manualmente de casos em nível municipal, confira este projeto de [Wesley Cota](https://labs.wesleycota.com/sarscov2/br/) ou a iniciativa colaborativa [Mapa do Corona Virus](mapadocoronavirus.com).
