rm(list = ls())

max.dim = 1001
dim.seq = seq(3, max.dim, by = 2)
upper.right.corner = dim.seq^2

all.corners = c(1, sapply(1:length(dim.seq), function(i) upper.right.corner[i] - (0:3) * (dim.seq[i] - 1)))

sum(all.corners)
