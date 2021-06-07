library(dplyr)
library(ggplot2)
library(tidyquant)

setwd("~/git/pan/HikeClimb/mp_pull")
rm(list = ls())

area.df = read.csv("area_data.csv", stringsAsFactors = FALSE)
route.df = read.csv("route_data.csv", stringsAsFactors = FALSE) %>%
  mutate(share_date = as.Date(share_date))
hierarchy.df = read.csv("hierarchy_data.csv", stringsAsFactors = FALSE) %>%
  mutate(source.type = ifelse(source %in% area.df$id, "area", "route"),
         target.type = ifelse(target %in% area.df$id, "area", "route"))

##################################################
# Count of routes by area
target.areas = hierarchy.df %>%
  filter(target.type == "area") %>%
  pull(target) %>%
  unique()
source.areas = hierarchy.df %>%
  filter(source.type == "area") %>%
  pull(source) %>%
  unique()
no.route.areas = setdiff(target.areas, source.areas)
  
route.count.df = hierarchy.df %>%
  group_by(source) %>%
  filter(target.type == "route") %>%
  summarize(count = n(), .groups = "drop") %>%
  rbind(data.frame(source = no.route.areas, count = 0)) %>%
  arrange(count, source)

##################################################
# Areas with recent routes
recent.route.df = route.df %>%
  filter(share_date >= as.Date("2021-01-01"))
recent.area.df = hierarchy.df %>%
  filter(target %in% recent.route.df$id) %>%
  group_by(source) %>%
  summarize(count = n(), .groups = "drop") %>%
  arrange(desc(count))

date.count.df = route.df %>%
  mutate(boulder = grepl("^Boulder", type)) %>%
  group_by(share_date, boulder) %>%
  summarize(count = n(), .groups = "drop") %>%
  right_join(expand.grid(share_date = seq(min(route.df$share_date), max(route.df$share_date), by = 1), boulder = c(TRUE, FALSE)),
             by = c("share_date", "boulder")) %>%
  mutate(count = replace(count, is.na(count), 0)) %>%
  rename(date = share_date) %>%
  arrange(date) %>%
  filter(date >= as.Date("2016-01-01"))
ggplot(date.count.df, aes(date, count)) +
  geom_ma(aes(color = boulder), n = 28) +
  theme_bw() +
  theme(legend.position = "top")
ggplot(date.count.df, aes(date, count)) +
  geom_smooth(aes(color = boulder), alpha = 0, method = "loess", span = 0.1) +
  theme_bw() +
  theme(legend.position = "top")
