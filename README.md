Dados de monitoramento da pandemia COVID-19 no Brasil, fornecidos pelo
Ministério da Saúde no site
[http://plataforma.saude.gov.br/novocoronavirus/](http://plataforma.saude.gov.br/novocoronavirus/).

[![goodtables.io](https://goodtables.io/badge/github/belisards/coronabr.svg)](https://goodtables.io/github/belisards/coronabr)

# Extrator de dados históricos do coronavírus no Brasil

O script (Python/Jupyter Notebook) baixa os dados com a série histórica do Ministério de Saúde das informações relativas ao coronavírus no Brasil. Isto é feito
acessando os dados da [Plataforma Integrada de Vigilância em Saúde (IVIS)](http://plataforma.saude.gov.br/novocoronavirus/) deste órgão. Através da interface do site disponibilizada ao usuário, só é possível ter acesso aos dados do dia atual.

Os dados são armazenados dentro de um arquivo JavaScript (`.js`). O script os transforma para `.json` e então converte em um CSV. 

Para facilitar a interpretação dos dados, é adicionada uma coluna, baseada no arquivo `indice.csv`, com a sigla da UF correspondente ao campo identificador (`uid`) assinalado no banco original.

O arquivo é exportado no formato CSV, com a data de execução do script. 

## Dados abertos
Os dados abertos podem ser acessados [na pasta `dados`](https://github.com/belisards/coronabr/tree/master/dados). 

### Colunas
O CSV é composto das colunas abaixo:

* uid = Número de identificação da UF
* suspects = Casos suspeitos
* refuses = Descartados
* confirmado = A coluna não é utilizada até o momento
* deads = Mortes
* local = Aparentemente, não é utilizada. Vide as observações.
* cases = Casos confirmados
* comments = Comentário sobre os dados (Ex: "Transmissão comunitária no município do Rio de Janeiro" ou "1 Portador assintomático")
* broadcast = Transmissão comunitária (True/False)
* date = Data de registro dos dados (%dd/%mm/%yyyy)
* time = Hora do registro dos dados  (%hh:%mm)
* uf = Coluna adicionada pelo script, com a sigla da UF

