# Código baseado no script 'ler_dados_covid_msaude.R' de Júlio Trecenti
# https://gist.github.com/jtrecenti/9ed617e060c2b01cfe9cce32577bf9b5

# Aqui, adiciono um índice para incorporar a sigla das UFs
indice <- read.csv("../../dados/auxiliares/indice.csv")

library(magrittr)

dados <- "http://plataforma.saude.gov.br/novocoronavirus/resources/scripts/database.js" %>%
  readr::read_file() %>%
  stringr::str_remove("var database=") %>%
  jsonlite::fromJSON() %>%
  purrr::pluck("brazil") %>%
  dplyr::mutate(values = purrr::map(values, dplyr::mutate_all, as.character)) %>%
  tidyr::unnest(values) %>%
  dplyr::mutate(date = lubridate::dmy(date)) %>%
  merge(x=.,y=indice,by="uid")

write.csv(dados, file = "../../dados/corona_brasil.csv")
