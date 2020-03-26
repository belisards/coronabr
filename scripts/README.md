# Extrator de dados históricos do coronavírus no Brasil

## Como funciona

### Script em Python
Os dados são armazenados dentro de um arquivo JavaScript (`.js`). O script os transforma para `.json` e então converte em um CSV. 

Para facilitar a interpretação dos dados, é adicionada uma coluna, baseada no arquivo `indice.csv`, com a sigla da UF correspondente ao campo identificador (`uid`) assinalado no banco original.

O arquivo é exportado no formato CSV, com a data de execução do script. 

**Atenção**: Todos os dados relativos aos casos são extraídos do site do Ministério da Saúde. Não nos responsabilizamos por eventuais erros e inconsistências. Sempre confira e cheque seus dados, através do [site da IVIS]() ou caches do [Web Archive](https://web.archive.org/web/*/http://plataforma.saude.gov.br/novocoronavirus/#COVID-19-brazil).

## Executando o script em Python

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
