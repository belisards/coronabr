#!/usr/bin/env python
# coding: utf-8

# In[1]:


import wget
import pandas as pd
import json
import datetime
from pandas.io.json import json_normalize


# In[4]:


# Baixa o arquivo JS
url = 'http://plataforma.saude.gov.br/novocoronavirus/resources/scripts/'
arquivo = 'database.js'
wget.download(url + arquivo, arquivo)


# In[6]:


# Converte Js para Json
base_js = open(arquivo, "rt")
base_json = open("database.json", "wt")

for line in base_js:
	base_json.write(line.replace('var database=', ''))

base_js.close()
base_json.close()


# In[18]:


# Exporta o dataframe e insere nome dos estados
df = json.load(open('database.json'))
df = json_normalize(data=df['brazil'], record_path='values',meta=['date','time'])
indice = pd.read_csv('indice.csv')
df = pd.merge(df, indice, on='uid', how='left')


# In[19]:


# Exporta a base em CSV com a data da execução no nome do arquivo
agora = str(datetime.date.today()).replace(" ", "").replace(":", "-").replace(".", "-")
arquivo = 'dados/coronabr_' + agora + '.csv'
df.to_csv(arquivo)

