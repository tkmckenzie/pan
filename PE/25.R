rm(list = ls())

start = 55

phi = (1 + sqrt(5)) / 2

fibonacci = function(n){
  return((phi^n - (-phi)^(-n)) / (2 * phi - 1))
}

carry = function(int.array, base = 10){
  if (length(int.array) > 1){
    for (i in 1:(length(int.array) - 1)){
      if (int.array[i] >= base){
        mult.factor = floor(int.array[i] / base)
        int.array[i + 1] = int.array[i + 1] + mult.factor
        int.array[i] = int.array[i] %% base
      }
    }
  }
  if (int.array[length(int.array)] >= base){
    int.array.length = length(int.array)
    mult.factor = floor(int.array[int.array.length] / base)
    int.array[int.array.length + 1] = mult.factor
    int.array[int.array.length] = int.array[int.array.length] %% base
    return(carry(int.array))
  } else{
    return(int.array)
  }
}
as.int.array = function(n){
  return(rev(as.numeric(strsplit(as.character(n), "")[[1]])))
}
as.int = function(int.array){
  return(as.numeric(paste0(rev(as.character(int.array)), collapse = "")))
}
'%+%' = function(int.array.1, int.array.2){
  int.array.1.length = length(int.array.1)
  int.array.2.length = length(int.array.2)
  
  if (int.array.1.length < int.array.2.length){
    int.array.1 = c(int.array.1, rep(0, int.array.2.length - int.array.1.length))
  } else if (int.array.2.length < int.array.1.length){
    int.array.2 = c(int.array.2, rep(0, int.array.1.length - int.array.2.length))
  }
  
  return(carry(int.array.1 + int.array.2))
}

fib.1 = as.int.array(fibonacci(start))
fib.2 = as.int.array(fibonacci(start + 1))

index = start + 1
while (length(fib.2) < 1000){
  fib.new = fib.1 %+% fib.2
  fib.1 = fib.2
  fib.2 = fib.new
  
  index = index + 1
  # print(length(fib.2))
}

index
