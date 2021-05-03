library(dplyr)

setwd("~/git/pan/HikeClimb/mp_pull")
rm(list = ls())

area.df = read.csv("area_data.csv", stringsAsFactors = FALSE)
route.df = read.csv("route_data.csv", stringsAsFactors = FALSE)
hierarchy.df = read.csv("hierarchy_data.csv", stringsAsFactors = FALSE)

# Count of routes by area

route.count.df = hierarchy.df %>%
  mutate(source.type = ifelse(source %in% area.df$id, "area", "route"),
         target.type = ifelse(target %in% area.df$id, "area", "route")) %>%
  group_by(source) %>%
  filter(target.type == "route") %>%
  summarize(count = n(), .groups = "drop") %>%
  rbind(data.frame(source = no.route.areas))
