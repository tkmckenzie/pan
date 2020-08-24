library(gganimate)
library(ggplot2)

rm(list = ls())

df = data.frame(theta = seq(0, 20 * pi, length.out = 5000))
df$y = sin(df$theta)
df$t = 1:nrow(df)

ggplot(df, aes(theta, y)) +
  geom_path() +
  transition_time(t) +
  ease_aes("linear") +
  shadow_mark() +
  coord_polar() +
  theme_void()
