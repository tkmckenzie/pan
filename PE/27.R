library(numbers)

rm(list = ls())

b.seq = Primes(1, 1000) #b must be prime since n = 0 must be prime

is.prime = function(n){
  if (n < 1){
    return(FALSE)
  } else{
    return(isPrime(n))
  }
}
f = function(n, a, b) return(n^2 + a * n + b)
num.primes = function(a, b){
  n = 0
  while (is.prime(f(n, a, b))){
    n = n + 1
  }
  return(n)
}

max.a.b = c()
max.num.primes = 0
for (b in b.seq){
  for (a in -1000:1000){
    num.primes.current = num.primes(a, b)
    if (num.primes.current > max.num.primes){
      max.num.primes = num.primes.current
      max.a.b = c(a, b)
    }
  }
}

prod(max.a.b)
