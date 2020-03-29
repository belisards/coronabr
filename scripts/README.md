# Extrator de dados históricos do coronavírus no Brasil

Atualmente, o notebook faz a extração da tabela disponibilizada diariamente pelo Ministério da Saúde. A inserção no arquivo `links.csv` e o notebook faz a coleta, limpeza e adequação à série histórica.

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
