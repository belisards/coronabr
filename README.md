# Dados sobre o coronavírus no Brasil

Este script baixa os dados com a série histórica do Ministério de Saúde das informações relativas ao coronavírus no Brasil. Isto é feito
acessando os dados da [Plataforma Integrada de Vigilância em Saúde (IVIS)](http://plataforma.saude.gov.br/novocoronavirus/) deste órgão. Os dados disponibilizados com formato `.js` são transformados para `.json` e então convertidos em um CSV. 

Para facilitar a interpretação dos dados, é adicionada uma coluna, baseada no arquivo `indice.csv`, com a sigla da UF correspondente às `uid` assinaladas no banco original.

O arquivo é exportado com a data de execução do script. 

Os dados abertos em CSV podem ser acessados diretamente pasta `dados`. Ele é composto das colunas abaixo.

* uid = Número de identificação da UF
* suspects
* refuses
* confirmado
* deads
* local
* cases
* comments
* broadcast = Transmissão comunitária
* date = Data de registro dos dados
* uf = coluna adicionada pelo script, com a sigla da UF


## Observações
Há um registro de 1 caso na coluna "refuses" na data 18/02/2020, sem estado (uid) atribuído.