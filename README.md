# CoronaBR

Dados e scripts para extrair a série histórica da pandemia COVID-19 no Brasil, de acordo com o Ministério da Saúde.

## Sobre os dados

No arquivo [corona_brasil.csv](https://github.com/belisards/coronabr/blob/master/dados/corona_brasil.csv), você encontra a série histórica dos casos de COVID-19 segundo o Ministério da Saúde, desde de 30 janeiro de 2020. Saiba mais sobre a metodologia de extração e compilação dos dados abaixo.

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


## Sobre a coleta dos dados

O projeto foi iniciado em meados de março, disponibilizando um script e a série histórica dos casos de coronavírus (COVID-19). Os dados não eram mostrados diretamente ao público, mas estavam disponíveis no servidor da Plataforma Integrada de Vigilância em Saúde (IVIS). Através da antiga interface - hoje já fora do ar - e do [site atual sobre os casos de coronavírus](https://covid.saude.gov.br/) só é possível disponibilizar números totais. Ao contrário da interface antiga, a atual sequer oferece o detalhamento de óbitos por estado ou opção de download dos dados em CSV.

Entre o dia 18/03/2020 e dia 26/03/2020, os dados foram atualizados unicamente por meio de tabelas disponíveis nos [comunicados no blog do Ministério da Saúde](https://github.com/belisards/coronabr/blob/master/dados/auxiliares/link_minsaude.csv) e, até o dia 25/03, a inserção foi feita manualmente, contando com uma verificação em pares para checagem. 

O script disponibilizado hoje automatiza a extração dos dados destes boletins - e não da plataforma, uma vez que ali não encontramos os dados completos e formatos tabulares. O script também concilia estes dados com a série histórica disponibilizada anteriormente.

Caso tenha alguma dúvida ou perceba alguma inconsistência, entre em contato abrindo uma "Issue" neste repositório do Github. Sinta-se à vontade para contribuir com a melhoria do código ou desenvolvimento de novas funcionalidades por meio de Pull Requests.

## A fazer

* Automatizar a extração dos dados identificando o link do dia na [planilha adequada](https://github.com/belisards/coronabr/blob/master/dados/auxiliares/link_minsaude.csv

* Automatizar a execução do script e commit do CSV atualizado


### Licença dos dados
A base de dados `corona-br` é disponibilizada sob a licença Open Database License: [http://opendatacommons.org/licenses/odbl/1.0/](http://opendatacommons.org/licenses/odbl/1.0/). 


## Outros projetos

### Projetos de raspagem em R

* [Pacote R para extrair as informações do IVIS](https://liibre.github.io/coronabr/articles/coronabr.html), por Sara Mortara e Andrea Sánchez-Tapia.

* Script para extrair os dados do IVIS em [R, por Júlio Trecenti](https://gist.github.com/jtrecenti/9ed617e060c2b01cfe9cce32577bf9b5)

### Outras bases de dados
* Lista colaborativa no [fórum Dados Abertos](https://dadosabertos.social/t/dados-sobre-a-pandemia-do-novo-coronavirus/267);

* Painel e projeções do [Observatório COVID-19 BR](https://covid19br.github.io/)

* O [Brasil.IO](https://brasil.io/dataset/covid19/boletim) está consolidando uma base de dados com os boletins informativos sobre COVID-19 no Brasil.

* Kaggle Corona-Virus-Brazil: o mesmo dataset da plataforma IVIS encontra-se disponível neste [repositório do Kaggle](https://www.kaggle.com/unanimad/corona-virus-brazil).

* Para um levantamento realizado manualmente de casos em nível municipal, confira este projeto de [Wesley Cota](https://labs.wesleycota.com/sarscov2/br/) ou a iniciativa colaborativa [Mapa do Corona Virus](mapadocoronavirus.com).
