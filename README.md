Dados de monitoramento da pandemia COVID-19 no Brasil, fornecidos pelo
Ministério da Saúde no site
[http://plataforma.saude.gov.br/novocoronavirus/](http://plataforma.saude.gov.br/novocoronavirus/).

# Extrator de dados históricos do coronavírus no Brasil

O script (Python/Jupyter Notebook) baixa os dados com a série histórica do Ministério de Saúde das informações relativas ao coronavírus no Brasil. Isto é feito
acessando os dados da [Plataforma Integrada de Vigilância em Saúde (IVIS)](http://plataforma.saude.gov.br/novocoronavirus/) deste órgão. Através da interface do site disponibilizada ao usuário, só é possível ter acesso aos dados do dia atual.

Os dados são armazenados dentro de um arquivo JavaScript (`.js`). O script os transforma para `.json` e então converte em um CSV. 

Para facilitar a interpretação dos dados, é adicionada uma coluna, baseada no arquivo `indice.csv`, com a sigla da UF correspondente ao campo identificador (`uid`) assinalado no banco original.

O arquivo é exportado no formato CSV, com a data de execução do script. 

**Atenção**: Todos os dados relativos aos casos são extraídos do site do Ministério da Saúde. Não nos responsabilizamos por eventuais erros e inconsistências. Sempre confira e cheque seus dados, através do [site da IVIS]() ou caches do [Web Archive](https://web.archive.org/web/*/http://plataforma.saude.gov.br/novocoronavirus/#COVID-19-brazil).

## Dados abertos
Os dados em formato aberto podem ser acessados [na pasta `dados`](https://github.com/belisards/coronabr/tree/master/dados). 

### Licença dos dados
A base de dados `corona-br` é disponibilizada sob a licença Open Database License: [http://opendatacommons.org/licenses/odbl/1.0/](http://opendatacommons.org/licenses/odbl/1.0/). 

### Validação dos dados
[![goodtables.io](https://goodtables.io/badge/github/belisards/coronabr.svg)](https://goodtables.io/github/belisards/coronabr)

É possível realizar a validação contínua dos dados extraídos através do [Goodtables](https://goodtables.io/github/belisards/coronabr). No dia 16 de março, por exemplo, existiam 15 registros duplicados.

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
* broadcast = ?
* date = Data de registro dos dados (%dd/%mm/%yyyy)
* time = Hora do registro dos dados  (%hh:%mm)
* uf = Coluna adicionada pelo script, com a sigla da UF


## Instalando as dependências 

Dentro da pasta do projeto, crie um abiente virtual com o comando

```
python3 -m venv env
```

Ative o ambiente virtual:

```
source env/bin/activate
```

Instale as dependências no seu ambiente Python usando o comando

```
pip install -r scripts/IVIScraper/requirements.txt
```

Só é necessário fazer isso uma única vez, exceto se o arquivo
`requirements.txt` for alterado.

### Incluindo o ambiente virtual no Jupyter

Com o ambiente virtual ativo (veja os passos acima), instale o pacote `ipykernel`:

```
pip install -U ipykernel
```

Em seguida, instale o seu ambiente virtual no Jupyter:

```
python3 -m ipykernel install --user --name=coronabr
```

Ao abrir o caderno Jupyter, selecione no canto superior direito o ambiente
"`coronabr`". Isso só é necessário fazer uma única vez pois, ao salvar o
caderno, o Jupyter se lembra de qual foi o ambiente utilizado.

## Outros projetos

### Projetos em R

* [Pacote R para extrair as informações do IVIS](https://liibre.github.io/coronabr/articles/coronabr.html), por Sara Mortara e Andrea Sánchez-Tapia.

* Script para extrair os dados do IVIS em [R, por Júlio Trecenti](https://gist.github.com/jtrecenti/9ed617e060c2b01cfe9cce32577bf9b5)

### Outras bases de dados

* Kaggle Corona-Virus-Brazil: o mesmo dataset da plataforma IVIS encontra-se disponível neste [repositório do Kaggle](https://www.kaggle.com/unanimad/corona-virus-brazil).

* Para um levantamento realizado manualmente de casos em nível municipal, confira este projeto de [Wesley Cota](https://labs.wesleycota.com/sarscov2/br/) ou a iniciativa colaborativa [Mapa do Corona Virus](mapadocoronavirus.com).

