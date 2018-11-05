library(multicool)

rm(list = ls())

x = 0:9
n = 0

iterate = function(x){
  first.char.index = tail(which(sapply(1:(length(x) - 1), function(i) x[i] < x[i + 1])), 1)
  first.char = x[first.char.index]
  
  x.subset = x[-(1:first.char.index)]
  second.char = min(x.subset[x.subset > first.char])
  second.char.index = which(x == second.char)
  
  x[first.char.index] = second.char
  x[second.char.index] = first.char
  
  x[-(1:first.char.index)] = sort(x[-(1:first.char.index)])
  
  return(x)
}

i = 1
while(i < 1e6){
  x = iterate(x)
  i = i + 1
}

paste0(x, collapse = "")
