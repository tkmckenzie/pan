library(numbers)

rm(list = ls())

max.N = 28123

sum.divisors = function(n){
  if (n == 1) return(1)
  if (isPrime(n)) return(2)
  
  prime.factors = primeFactors(n)
  return(sum(unique(unlist(sapply(1:length(prime.factors), function(i) unique(apply(combn(prime.factors, i), 2, prod)))))) - n + 1)
}
is.abundant = function(n){
  if (sum.divisors(n) > n){
    return(TRUE)
  }
  else{
    return(FALSE)
  }
}

abundant.nums = (1:max.N)[sapply(1:max.N, is.abundant)]
m = cbind(combn(abundant.nums, 2), matrix(abundant.nums, nrow = 2, ncol = length(abundant.nums), byrow = TRUE))
sum(setdiff(1:max.N, unique(colSums(m))))
