library(numbers)

rm(list = ls())

divisors = 500
max.N = 2e4

num.divisors = function(n){
  if (n == 1) return(1)
  if (isPrime(n)) return(2)
  
  prime.factors = primeFactors(n)
  return(length(unique(unlist(sapply(1:length(prime.factors), function(i) unique(apply(combn(prime.factors, i), 2, prod)))))) + 1)
}

triangular.numbers = cumsum(1:max.N)
triangular.divisors = sapply(triangular.numbers, num.divisors)

triangular.numbers[which(triangular.divisors > divisors)[1]]
