rm(list = ls())

x.init = 10
N = 100

x = c(x.init, rep(NA, N - 1))
for (i in 2:N){
  x[i] = (3 / x[i-1] + x[i-1]) / 2
}
