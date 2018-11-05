rm(list = ls())

max.N = 1e6

n.to.array = function(n){
  return(strsplit(as.character(n), "")[[1]])
}
array.to.n = function(a){
  return(as.numeric(paste0(a, collapse = "")))
}
generate.truncations = function(n){
  n.array = n.to.array(n)
  array.length = length(n.array)
  left.truncation = sapply(1:(array.length - 1), function(i) array.to.n(n.array[-(1:i)]))
  right.truncation =  sapply(1:(array.length - 1), function(i) array.to.n(n.array[-((array.length - i + 1):array.length)]))
  return(c(n, union(left.truncation, right.truncation)))
}
not.valid = function(n){
  n.array = as.numeric(n.to.array(n))
  array.length = length(n.array)
  if (any((n.array[-1] %% 2 == 0))){
    return(TRUE)
  } else if (n.array[1] %% 2 == 0 & n.array[1] != 2){
    return(TRUE)
  } else if (any(c(n.array[1], n.array[array.length]) == 1)){
    return(TRUE)
  } else{
    return(FALSE)
  }
}
is.valid = function(n){
  truncations = generate.truncations(n)
  if (all(isPrime(truncations))){
    return(TRUE)
  } else{
    return(FALSE)
  }
}

all.primes = Primes(10, max.N)
all.primes = all.primes[!sapply(all.primes, not.valid)]

valid.primes = c()
for (prime in all.primes){
  if (is.valid(prime)){
    valid.primes = c(valid.primes, prime)
  }
}

sum(valid.primes)
