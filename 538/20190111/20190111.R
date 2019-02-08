library(expm)

rm(list = ls())

setwd("~/git/pan/538/20190111")

#Read and print matrix with expressions
P = as.matrix(read.table("transition.probabilities.csv", sep = ","))
print(P)
P = P[-1,-1]

#Set values of parameters
p.A = 0.05
p.B = 0.075
p.C = 0.1

num.days = 1825

#Replace expressions with values
P = matrix(sapply(P, function(s) eval(parse(text = s))), nrow = nrow(P))
init = matrix(c(1, rep(0, nrow(P) - 1)), nrow = 1)

#Compute state distribution after 1825 days
v = init %*% (P %^% num.days)
v

#Probability of success
1 - tail(c(v), 1)