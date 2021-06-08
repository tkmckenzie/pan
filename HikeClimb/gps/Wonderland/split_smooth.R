library(dplyr)
library(kmlShape)
library(rgdal)

setwd("~/git/pan/HikeClimb/gps/Wonderland")

# Read in data and organize
ogr = readOGR("TheWonderlandTrail.gpx", layer="track_points")
df = as.data.frame(ogr) %>%
  distinct(coords.x1, coords.x2, .keep_all = TRUE)

if (length(unique(df$track_fid)) > 1 | length(unique(df$track_seg_id)) > 1) stop("Script not set up to handle more than one unique track/segment.")

coords = df %>%
  select(starts_with("coords."))

# Down-select points using RDP
coords.reduced = DouglasPeuckerNbPoints(coords$coords.x1, coords$coords.x2, 10000) %>%
  rename(coords.x1 = x, coords.x2 = y)

df.reduced = df %>%
  inner_join(coords.reduced, by = c("coords.x1", "coords.x2")) %>%
  mutate(track_seg_point_id = 1:n())

# Reconstitute and save reduced track
coords.new = df.reduced %>%
  select(starts_with("coords."))
data.new = df.reduced %>%
  select(!starts_with("coords."))

# Split up track into smaller chunks and save
max.track.size = 500

coords.new = 