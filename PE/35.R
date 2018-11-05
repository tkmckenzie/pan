rm(list = ls())

max.N = 1e6

n.to.array = function(n){
  return(strsplit(as.character(n), "")[[1]])
}
array.to.n = function(a){
  return(as.numeric(paste0(a, collapse = "")))
}
generate.rotations = function(n){
  n.array = n.to.array(n)
  array.length = length(n.array)
  rotations = array.to.n(n.array)
  for (i in 2:array.length){
    n.array = c(n.array[-1], n.array[1])
    rotations[i] = array.to.n(n.array)
  }
  return(unique(rotations))
}
has.mult.2 = function(n){
  n.array = as.numeric(n.to.array(n))
  if (any(n.array %% 2 == 0)){
    return(TRUE)
  } else{
    return(FALSE)
  }
}

all.primes = Primes(10, max.N)
all.primes = all.primes[!sapply(all.primes, has.mult.2)]
circular.primes = Primes(10)

while(length(all.primes) > 0){
  prime = all.primes[1]
  rotations = generate.rotations(prime)
  if (all(rotations %in% all.primes)){
    circular.primes = c(circular.primes, rotations)
  }
  all.primes = setdiff(all.primes, rotations)
  # print(prime)
}

length(circular.primes)
