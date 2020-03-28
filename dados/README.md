# Sobre a coleta dos dados

O projeto foi iniciado em meados de março, disponibilizando um script e a série histórica dos casos de coronavírus (COVID-19). Os dados não eram mostrados diretamente ao público, mas estavam disponíveis no servidor da Plataforma Integrada de Vigilância em Saúde (IVIS). Através da antiga interface - hoje já fora do ar - e do site atual sobre os casos de coronavírus só é possível disponibilizar números totais. Ao contrário da interface antiga, a atual sequer oferece o detalhamento de óbitos por estado ou opção de download dos dados em CSV.

Entre o dia 18/03/2020 e dia 26/03/2020, os dados foram atualizados unicamente por meio de tabelas disponíveis nos comunicados no blog do Ministério da Saúde e, até o dia 25/03, a inserção foi feita manualmente, contando com uma verificação em pares para checagem.

O script disponibilizado hoje automatiza a extração dos dados destes boletins - e não da plataforma, uma vez que ali não encontramos os dados completos e formatos tabulares. O script também concilia estes dados com a série histórica disponibilizada anteriormente.

Caso tenha alguma dúvida ou perceba alguma inconsistência, entre em contato abrindo uma "Issue" neste repositório do Github. Sinta-se à vontade para contribuir com a melhoria do código ou desenvolvimento de novas funcionalidades por meio de Pull Requests.
