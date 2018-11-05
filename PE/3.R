rm(list = ls())

n = 600851475143
n = 814

prime.factors = function(n){
  upper.limit = floor(sqrt(n))
  lower.nums = 2:upper.limit
  lower.factors = c()
  while (length(lower.nums) > 0){
    i = lower.nums[1]
    if (n %% i == 0){
      lower.factors = c(lower.factors, i)
    }
    lower.nums = setdiff(lower.nums, seq(i, upper.limit, by = i))
  }
}
