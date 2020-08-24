library(dplyr)
library(gganimate)
library(ggplot2)
library(scales)
library(usmap)

setwd("~/git/pan/TSP")
rm(list = ls())

# Reading map data
map.df = map_data("state")

# Creating path data
shortest.path.df = read.csv("shortest_path.csv")
coord.df = read.csv("state_centroids.csv")

shortest.path.df = shortest.path.df %>%
  left_join(coord.df, by = "name") %>%
  rename(lat = latitude, long = longitude) %>%
  mutate(step = 1:n())

# Plotting
ggplot(map.df, aes(long, lat)) +
  geom_polygon(aes(group = group), fill = "white", color = "black") +
  geom_path(data = shortest.path.df, aes(color = step)) +
  scale_color_gradient(low = muted("blue"), high = muted("red")) +
  coord_map("sinusoidal") +
  theme_void() +
  theme(legend.position = "none")
