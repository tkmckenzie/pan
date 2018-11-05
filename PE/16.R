rm(list = ls())

n = 2^1000

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

int.array = 1
for (i in 1:1000){
  int.array = carry(int.array * 2)
}

int.array = rev(int.array)

sum(int.array)