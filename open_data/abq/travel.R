library(dplyr)
library(ggplot2)

rm(list = ls())
setwd("~/git/pan/open_data/abq")

df = read.csv("travel.csv")

df = df %>%
  mutate(Total.Difference = Actual.Total - Estimated.Total,
         Percent.Total.Difference = 100 * Total.Difference / Estimated.Total)

df.dept = df %>%
  group_by(Department...Division) %>%
  summarize(Actual.Total = mean(Actual.Total),
            Percent.Total.Difference = mean(Percent.Total.Difference),
            count = n()) %>%
  filter(Department...Division != "")
ggplot(df.dept, aes(Actual.Total, Percent.Total.Difference)) +
  geom_point(aes(size = count, color = Department...Division)) + 
  theme_bw() +
  theme(legend.position = "top")
ggplot(df %>% filter(Department...Division != ""), aes(Actual.Total, Percent.Total.Difference)) +
  geom_point(aes(color = Department...Division)) + 
  geom_abline(slope = 0.1, intercept = -100) +
  xlim(0, 5000) +
  ylim(NA, 200) +
  theme_bw() +
  theme(legend.position = "top")
df.dept = df.dept %>%
  mutate(Percent.Total.Difference.max = -100 + 0.1 * Actual.Total)

df.person = df %>%
  group_by(Traveler.Name) %>%
  summarize(Actual.Total = mean(Actual.Total),
            Avg.Total.Difference = mean(Total.Difference),
            Total.Difference = sum(Total.Difference),
            Percent.Total.Difference = mean(Percent.Total.Difference),
            count = n())
df.person %>% arrange(-Total.Difference) %>% filter(count > 1)
df.person %>% arrange(-Avg.Total.Difference) %>% filter(count > 1)
df.person %>% arrange(-Percent.Total.Difference) %>% filter(count > 1)
