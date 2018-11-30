library(ggplot2)

rm(list = ls())

num.children = 1
effort.list = list(function(t) 1 / t)
birth.times = c(0)
while (num.children < 1000){
  birth.times[num.children + 1] = uniroot(function(t) sum(sapply(effort.list, function(f) f(t + birth.times[num.children]))) - 1, c(0, 1000))$root + birth.times[num.children]
  num.children = num.children + 1
  effort.list[[num.children]] = function(t) 1 / (t - birth.times[num.children])
}

num.children.df = data.frame(num.children = 1:num.children, t = birth.times)
birth.diff.df = data.frame(child = 2:num.children, diff = diff(birth.times))

ggplot(num.children.df, aes(t, num.children)) + geom_point()
ggplot(birth.diff.df, aes(child, diff)) + geom_point()
