rm(list = ls())

#####
#Brute force
x = union(seq(3, 999, by = 3), seq(5, 999, by = 5))
sum(x)

#####
sum.N = function(N){
  #sum_{i=1}^N
  return(N * (N + 1) / 2)
}

num.mult.3 = floor(999 / 3)
num.mult.5 = floor(999 / 5)
num.mult.3.5 = floor(999 / 15)

3 * sum.N(num.mult.3) + 5 * sum.N(num.mult.5) - 3 * 5 * sum.N(num.mult.3.5)
