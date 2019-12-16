library(ggplot2)
library(rstan)

setwd("~/git/pan/Baba")

rm(list = ls())

# Read in data
df = read.csv("data.csv")

# Some plotting
{
  # Area
  # (1) Strong relationship to Flow, best described by log-log transformation
  qplot(Area, Flow, data = df) + scale_y_log10() + scale_x_log10()
}
{
  # Elevation related variables
  # (1) Elevation and Basin.Relief are positively related but vary independently
  # (2) Neither variable seems strongly related to Flow
  qplot(Elevation, Basin.Relief, data = df)
  
  qplot(Elevation, Flow, data = df) + scale_y_log10()
  qplot(Basin.Relief, Flow, data = df) + scale_y_log10()
}
{
  # Slope related variables
  # (1) Slope.30 and Basin.Slope are strongly related; positive relationships to MCS, but not as strong
  # (2) Flow only appears to be strongly related to MCS
  plot(df[,c("Slope.30", "Basin.Slope", "MCS")])
  
  qplot(Slope.30, Flow, data = df) + scale_y_log10()
  qplot(Basin.Slope, Flow, data = df) + scale_y_log10()
  qplot(MCS, Flow, data = df) + scale_y_log10()
}
{
  # Forest area
  # (1) Negative relationship to Flow, best described by log-log transformation
  qplot(Forest.Area, Flow, data = df) + scale_y_log10() + scale_x_log10()
}
{
  # Annual precipitation
  # (1) Not much apparent relationship
  qplot(Annual.Precipitation, Flow, data = df) + scale_y_log10() + scale_x_log10()
}
{
  # Dependency between independent variables
  qplot(Area, Forest.Area, data = df) + scale_y_log10() + scale_x_log10()
  qplot(Area, Annual.Precipitation, data = df) + scale_y_log10() + scale_x_log10()
}

# Linear models
{
  # Kitchen sink model
  m = lm(log(Flow) ~ log(Area) + Elevation + Basin.Relief + Slope.30 + Basin.Slope + MCS + log(Forest.Area) + Annual.Precipitation, df)
  summary(m)
}
{
  # Model based on plots
  # Looks good overall; residuals are normal, etc.
  m = lm(log(Flow) ~ log(Area) + log(Forest.Area) + Annual.Precipitation, df)
  summary(m)
  
  qqnorm(m$residuals)
  qqline(m$residuals)
  
  shapiro.test(m$residuals)
}

# PCA regression
{
  # Kitchen sink
  # Only need a few components
  pca = prcomp(~ log(Area) + Elevation + Basin.Relief + Slope.30 + Basin.Slope + MCS + log(Forest.Area) + Annual.Precipitation, df)
  
  m = lm(log(df$Flow) ~ pca$x[,1:3])
  summary(m)
}

# Bayesian linear regression
{
  burn.iter = 1000
  sample.iter = 10000
  X = cbind(1, log(df$Area), log(df$Forest.Area), df$Annual.Precipitation)
  y = log(df$Flow)
  
  stan.data = list(N = nrow(X), k = ncol(X),
                   X = X, y = y,
                   beta_prior_sd = rep(10, ncol(X)),
                   sigma_prior_scale = 10)
  stan.fit = stan("linear.stan", data = stan.data,
                  chains = 1, warmup = burn.iter, iter = burn.iter + sample.iter)
  traceplot(stan.fit)
  stan.extract = extract(stan.fit)
  
  # Pretty similar to classical regression results, as expected
  apply(stan.extract$beta, 2, mean)
  apply(stan.extract$beta, 2, function(col) mean(col > 0))
}
