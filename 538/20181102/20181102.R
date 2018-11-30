rm(list = ls())

#Assumptions:
# * Theorists can only challenge whole elections (or groups of whole elections)
#   at a time.
#     * For example, they could not challenge a specific seat.

#Q1: No cheating probabilities
p = 0.5
pbinom(49, 100, 1 - p)
pbinom(40, 100, 1 - p)

#Q2: Bias needed for supermajority
#Probability for 50% chance of supermajority
sigmoid = function(x) 1 / (1 + exp(-x))

target.prob = 0.5
f = function(p.untransformed) pbinom(40, 100, 1 - sigmoid(p.untransformed)) - target.prob

uniroot.result = uniroot(f, lower = -1e3, upper = 1e3)
p = sigmoid(uniroot.result$root)
p

#How many times in a row can this be don before Theorists have 99% evidence of bias
#This has to be done in expectation, since evidence (election results) are a r.v.
#Model is as follows:
# c_t ~ Binomial(100, p)
# e_t = pbinom(sum({c_s}_{s=1}^t, 100 * t, 0.5)
#Equivalently (b/c of independence):
# c_t ~ Binomial(100 * t, p)
# e_t = pbinom(c_t, 100 * t, 0.5)
#Simulating first:
n = 1e6
t = 3
c.t = rbinom(n, 100 * t, p)
mean(pbinom(c.t, 100 * t, 0.5))

#Q3: Maximize 