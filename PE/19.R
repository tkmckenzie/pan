rm(list = ls())

num.days = function(date){
  year = date$year
  month = as.character(date$month)
  if (month == "2"){
    if ((year %% 4 == 0) & (!(year %% 100 == 0) | (year %% 400 == 0))){
      return(29)
    } else{
      return(28)
    }
  } else{
    return(switch(month,
                  "1" = 31,
                  "3" = 31,
                  "4" = 30,
                  "5" = 31,
                  "6" = 30,
                  "7" = 31,
                  "8" = 31,
                  "9" = 30,
                  "10" = 31,
                  "11" = 30,
                  "12" = 31))
  }
}
resolve.date = function(date){
  rem.days = date$day - num.days(date)
  rem.months = date$month - 12
  if (rem.months > 0){
    date$year = date$year + 1
    date$month = rem.months
    return(resolve.date(date))
  } else if (rem.days > 0){
    date$month = date$month + 1
    date$day = rem.days
    return(resolve.date(date))
  } else{
    return(date)
  }
}

date = list(month = 12, day = 31, year = 1899) #First Sunday
date.list = list()
count = 0
while (date$year < 2001){
  date$day = date$day + 7
  date = resolve.date(date)
  
  if (date$day == 1 & date$year >= 1901){
    date.list[[count]] = date
    count = count + 1
  }
}

count
