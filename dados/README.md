# Sobre a coleta dos dados

O projeto foi iniciado em meados de março, disponibilizando um script e a série histórica dos casos de coronavírus (COVID-19). Os dados não eram mostrados diretamente ao público, mas estavam disponíveis no servidor da Plataforma Integrada de Vigilância em Saúde (IVIS). Através da antiga interface - hoje já fora do ar - e do site atual sobre os casos de coronavírus só é possível disponibilizar números totais. Ao contrário da interface antiga, a atual sequer oferece o detalhamento de óbitos por estado ou opção de download dos dados em CSV.

Entre o dia 18/03/2020 e dia 26/03/2020, os dados foram atualizados unicamente por meio de tabelas disponíveis nos comunicados no blog do Ministério da Saúde e, até o dia 25/03, a inserção foi feita manualmente, contando com uma verificação em pares para checagem.

O script disponibilizado hoje automatiza a extração dos dados destes boletins - e não da plataforma, uma vez que ali não encontramos os dados completos e formatos tabulares. O script também concilia estes dados com a série histórica disponibilizada anteriormente.

Caso tenha alguma dúvida ou perceba alguma inconsistência, entre em contato abrindo uma "Issue" neste repositório do Github.

O arquivo `corona_brasil_old.csv` está atualizado até o dia 29 de março. Para facilitar o a compreensão dos dados, ele foi [divido em dois](https://gist.github.com/belisards/411021a18ccd13ea0ed900882bbab65b), refletindo assim a mudança na metodologia de disponibilização dos dados adotada pelo Ministério da Saúde: o primeiro (serie_ivis) traz a série histórica da Plataforma IVIS até o dia 18 de março e o segundo (corona_br.csv) traz a série histórica completa e atualizada de casos confirmados e óbitos.

## serie_ivis
A tabela é baseada no formato originalmente adotado pelo Ministério da Saúde para armazenas os dados da COVID-19 na Plataforma Integrada de Vigilância em Saúde. Atualmente, porém, o órgão disponibiliza apenas números de óbitos e casos confirmados. 

* uid = Número de identificação da UF 
* date = Data de registro dos dados (%yyyy-%mm-%dd)
* time = Hora do registro dos dados  (%hh:%mm)
* suspects = Casos suspeitos
* refuses = Descartados
* cases = Casos confirmados
* comments = Comentário sobre os dados adicionados na Plataforma IVIS (Ex: "Transmissão comunitária no município do Rio de Janeiro" ou "1 Portador assintomático")
* broadcast = Identificador para transmissão comunitária?
* deaths = Mortes/Óbitos
* uf = Coluna com a sigla da UF, adicionada pela primeira versão do script de extração.

Exisitam três variáveis também disponibilizadas no arquivo JSON (confirmado, local, deads), que foram descartadas pois estarem vazias. O registro pode ser conferido no histórico do git. 

## Registros duplicados

O arquivo JSON disponibilizado continha registros duplicados. Estes foram identificados (vide o CSV correspondente) e removidos.