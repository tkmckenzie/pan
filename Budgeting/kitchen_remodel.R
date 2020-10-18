library(ggplot2)

rm(list = ls())

balance.current = 42281.39 + 11296.46
date.current = as.Date("2020-10-18") # Whatever date above balance is current as of

paycheck = function(date){
  last.paydate = as.Date("2020-10-01")
  if (as.numeric(date - last.paydate) %% 14 == 0){
    return(2480 * 2)
  } else{
    return(0)
  }
}
existing.credit.card = function(date){
  # As of 2020/10/05
  payment = switch(as.character(date),
                   "2020-10-20" = 1278.14, # SLFCU card existing charges + any new charges between 2020/10/05 and 2020/10/20 (leaving latter as zero and putting all to new Citi charges)
                   0)
  return(payment)
}
projected.credit.card = function(date){
  # This should include all non-utility purchases; e.g., groceries, fun, other purchases
  # Should include all Citi charges after 2020/09/18 and all SLFCU charges after 2020/10/20
  payment = switch(as.character(date),
                   "2020-11-15" = 687.14, # Citi card ending 2020/10/18
                   "2020-12-15" = 1000, # Citi card ending 2020/11/18
                   "2020-11-20" = 0, # SLFCU card ending 2020/11/20
                   "2020-12-20" = 0, # SLFCU card ending 2020/12/20
                   0)
  return(payment)
}
mortgage = function(date){
  payment = switch(as.character(date),
                   "2020-11-01" = 2656,
                   "2020-12-01" = 2656,
                   "2021-01-01" = 2656,
                   0)
  return(payment)
}
water.bill = function(date){
  payment = switch(as.character(date),
                   "2020-10-24" = 300,
                   "2020-11-24" = 200,
                   "2020-12-24" = 100,
                   0)
  return(payment)
}
electric.bill = function(date){
  payment = switch(as.character(date),
                   "2020-11-12" = 100,
                   "2020-12-12" = 100,
                   0)
  return(payment)
}
gas.bill = function(date){
  payment = switch(as.character(date),
                   "2020-11-13" = 50,
                   "2020-12-13" = 100,
                   0)
  return(payment)
}
verizon.bill = function(date){
  payment = switch(as.character(date),
                   "2020-10-28" = 234,
                   "2020-11-28" = 234,
                   "2020-12-28" = 234,
                   0)
  return(payment)
}
comcast.bill = function(date){
  payment = switch(as.character(date),
                   "2020-10-14" = 90,
                   "2020-11-14" = 90,
                   "2020-12-14" = 90,
                   0)
  return(payment)
}
remodel.bill = function(date){
  payment = switch(as.character(date),
                   "2020-10-23" = 15187.96,
                   "2020-10-30" = 6472.73,
                   "2020-11-06" = 1618.18 + 17000,
                   0)
  return(payment)
}

# Calculating running balance
balance = balance.current
date = date.current
end.date = as.Date("2021-01-15")

balance.history = balance
date.history = date

while (date < end.date){
  new.balance = balance +
    paycheck(date) - 
    existing.credit.card(date) -
    projected.credit.card(date) -
    mortgage(date) - 
    water.bill(date) -
    electric.bill(date) -
    gas.bill(date) -
    verizon.bill(date) -
    comcast.bill(date) -
    remodel.bill(date)
  new.date = date + 1
  
  balance.history = c(balance.history, new.balance)
  date.history = c(date.history, new.date)
  
  balance = new.balance
  date = new.date
}

plot.df = data.frame(date = date.history, balance = balance.history)
ggplot(plot.df, aes(date, balance)) + 
  geom_line() +
  geom_area(alpha = 0.25) +
  geom_hline(yintercept = 0, color = "red") +
  geom_hline(yintercept = 5000, color = "orange") +
  geom_hline(yintercept = 20000, color = "purple") +
  geom_vline(xintercept = as.Date("2020-11-18"), color = "dark green") +
  annotate(geom = "text",
           label = paste0("Min. balance of $", min(balance.history), "\non ", date.history[which.min(balance.history)]),
           x = max(date.history), y = Inf, hjust = 1, vjust = 1.5) +
  theme_bw()
