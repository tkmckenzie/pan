rm(list = ls())

num.to.string = function(n){
  if (n < 20){
    string = switch(as.character(n),
                    "1" = "one",
                    "2" = "two",
                    "3" = "three",
                    "4" = "four",
                    "5" = "five",
                    "6" = "six",
                    "7" = "seven",
                    "8" = "eight",
                    "9" = "nine",
                    "10" = "ten",
                    "11" = "eleven",
                    "12" = "twelve",
                    "13" = "thirteen",
                    "14" = "fourteen",
                    "15" = "fifteen",
                    "16" = "sixteen",
                    "17" = "seventeen",
                    "18" = "eighteen",
                    "19" = "nineteen")
  } else if (n < 100){
    div = floor(n / 10)
    string = switch(as.character(div),
                    "2" = "twenty",
                    "3" = "thirty",
                    "4" = "forty",
                    "5" = "fifty",
                    "6" = "sixty",
                    "7" = "seventy",
                    "8" = "eighty",
                    "9" = "ninety")
    rem = n - 10 * div
    if (rem > 0) string = paste0(string, "-", num.to.string(rem))
  } else if (n < 1000){
    div = floor(n / 100)
    rem = n - 100 * div
    if (rem > 0){
      string = paste0(num.to.string(div), " hundred and ", num.to.string(rem))
    } else{
      string = paste0(num.to.string(div), " hundred")
    }
  } else{
    #n = 1000
    return("one thousand")
  }
  return(string)
}

strings = unlist(sapply(1:1000, num.to.string))
strings = gsub("[\\s \\-]", "", strings, perl = TRUE)

sum(nchar(strings))
