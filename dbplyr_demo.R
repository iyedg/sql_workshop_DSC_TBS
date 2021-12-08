library(dplyr, warn.conflicts = FALSE)
library(here)
library(ggplot2)

con <- DBI::dbConnect(RSQLite::SQLite(), 
        dbname = here("data", "municipal_performance.sqlite3"))

municipalities <- con %>% tbl("municipalities")
governorates <- con %>% tbl("municipalities")
evaluations <- con %>% tbl("evaluations")
criteria <- con %>% tbl("criteria")

evaluations %>% 
  select(score, municipality_id, criterion_id, year) %>% 
  inner_join(municipalities) %>% 
  inner_join(governorates) %>% 
  filter(municipality_id %in% c(1111, 1112),
         year == 2018,
         criterion_id %in% c(10, 11, 12)) %>% 
  select(name_fr, score, criterion_id) %>% 
  ggplot(aes(x = name_fr, y = score, fill = as.factor(criterion_id))) +
  geom_col() +
  facet_wrap(~criterion_id)
  

municipalities %>% top_n(20) %>% show_query()

DBI::dbGetQuery(con, "select * from municipalities;")
