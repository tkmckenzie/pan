rm(list = ls())

max.N = 1000

a.b.range = 1:max.N

a.b = combn(a.b.range, 2)

a.b.sums = apply(a.b, 2, function(v) sum(v^2))
a.b.c = rbind(a.b, sqrt(sums))

a.b.c.sums = apply(a.b.c, 2, sum)

prod(a.b.c[,which(a.b.c.sums == 1000)])
