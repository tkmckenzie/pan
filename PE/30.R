rm(list = ls())

n.range = 2:1e6

digit.pow = function(n, pow){
  return(sum(as.numeric(strsplit(as.character(n), "")[[1]])^pow))
}
is.power.sum = function(n, pow){
  if (n == digit.pow(n, pow)){
    return(TRUE)
  } else{
    return(FALSE)
  }
}

power.sums = n.range[sapply(n.range, is.power.sum, pow = 5)]
sum(power.sums)