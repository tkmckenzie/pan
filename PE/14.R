rm(list = ls())

n.range = 1:(1e6-1)

collatz = function(n){
  if (n %% 2 == 0){
    return(n / 2)
  } else{
    return(3 * n + 1)
  }
}
collatz.seq = function(n){
  n.seq = n
  i = 1
  while (n.seq[i] > 1){
    n.seq[i + 1] = collatz(n.seq[i])
    i = i + 1
  }
  
  return(n.seq)
}
collatz.length = function(n){
  n.current = n
  i = 1
  while (n.current > 1){
    n.current = collatz(n.current)
    i = i + 1
  }
  return(i)
}

seq.lengths = sapply(1:(1e6-1), collatz.length)
n.range[which.max(seq.lengths)]
