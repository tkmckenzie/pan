library(numbers)

rm(list = ls())

divisors = 500
max.N = 2e4

sum.divisors = function(n){
  if (n == 1) return(1)
  if (isPrime(n)) return(2)
  
  prime.factors = primeFactors(n)
  return(sum(unique(unlist(sapply(1:length(prime.factors), function(i) unique(apply(combn(prime.factors, i), 2, prod)))))) - n + 1)
}

m = matrix(NA, nrow = 2)
for (a in 1:10000){
  d.a = sum.divisors(a)
  d.b = sum.divisors(d.a)
  
  if ((a == d.b) & (a != d.a)){
    m = cbind(m, c(a, d.a))
  }
}

sum(m, na.rm = TRUE) / 2
