library(dplyr)
library(ggplot2)

setwd("~/git/pan/HikeClimb/pro_data")

df = read.csv("pro_data.csv", stringsAsFactors = FALSE)

df$Product = sapply(df$Size, function(s) paste(head(strsplit(s, " ")[[1]], -1), collapse = " "))
df$Size = sapply(df$Size, function(s) paste(tail(strsplit(s, " ")[[1]], 1), collapse = " "))

df = df %>% 
  filter(Generation == "Current") %>%
  arrange(Brand, Product, Lower.mm)

test.df = df %>% filter(Product == "Camalot")
ggplot(df, aes(xmin = Lower.in, xmax = Upper.in, y = Size)) +
  geom_errorbarh() +
  xlab("Working Range (in)") +
  facet_wrap(~ Product, scales = "free_y")
ggsave("active_sizes.pdf", width = 10, height = 10)
