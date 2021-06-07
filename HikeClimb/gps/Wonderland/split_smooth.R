library(dplyr)
library(rgdal)

setwd("~/git/pan/HikeClimb/gps/Wonderland")

ogr = readOGR("TheWonderlandTrail.gpx", layer="track_points")
df = as.data.frame(ogr)

coords = df %>%
  select(starts_with("coords."))
data = df %>%
  select(!starts_with("coords."))
