rm(list = ls())

denominator.range = 2:999

decimal.expansion = function(numerator, denominator){
  #Returns expansion beyond decimal place
  #numerator < denominator
  remainders = numerator * 10
  digits = c(0)
  i = 1
  recurrent = FALSE
  recurrence.length = 0
  while (remainders[i] > 0){
    digits[i+1] = floor(remainders[i] / denominator)
    remainders[i+1] = (remainders[i] - digits[i+1] * denominator) * 10
    
    i = i + 1
    
    if (any(apply(rbind(digits, remainders)[,-i,drop = FALSE], 2, function(v) all(v == c(digits[i], remainders[i]))))){
      recurrent = TRUE
      recurrence.length = i - which(apply(rbind(digits, remainders)[,-i], 2, function(v) all(v == c(digits[i], remainders[i]))))
      digits = digits[-i]
      break
    }
  }
  
  return(list(expansion = digits[-1], recurrent = recurrent, recurrence.length = recurrence.length))
}

recurrence.lengths = sapply(denominator.range, function(denominator) decimal.expansion(1, denominator)$recurrence.length)
denominator.range[which.max(recurrence.lengths)]
