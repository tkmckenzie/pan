setwd("~/code/PE")

rm(list = ls())

names = unlist(read.csv("names.txt", stringsAsFactors = FALSE, header = FALSE, na.strings = c())[1,])
names = sort(names)

name = names[1]

score.name = function(name){
  return(sum(sapply(strsplit(name, "")[[1]], function(s) which(LETTERS == s))))
}

sum(sapply(1:length(names), function(i) i * score.name(names[i])))
