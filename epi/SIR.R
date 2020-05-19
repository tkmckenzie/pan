library(deSolve)
library(ggplot2)

setwd("~/git/pan/epi")
rm(list = ls())

# SIR model:
# dS / dt = -alpha * S * I
# dI / dt = alpha * S * I - beta * I
# dR / dt = beta * I

# Parameters
alpha = 0.05
beta = 0.01
I.0 = 0.01

# Setting up model
parameters = c(alpha = alpha, beta = beta)
state = c(S = 1 - I.0, I = I.0, R = 0)

model = function(t, state, parameters){
  with(as.list(c(state, parameters)),{
    dS = -alpha * S * I
    dI = alpha * S * I - beta * I
    dR = beta * I
    
    return(list(c(dS, dI, dR)))
  })
}

times = seq(0, 1000, length.out = 500)

# Solving model
out = ode(y = state, times = times, func = model, parms = parameters)

# Plot results
df = data.frame(t = rep(out[,1], times = 3),
                y = c(out[,2:4]),
                variable = rep(c("S", "I", "R"), each = nrow(out)))

ggplot(df, aes(t, y)) +
  geom_line(aes(color = variable)) +
  theme_bw() +
  theme(legend.position = "top")
