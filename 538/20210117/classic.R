library(combinat)

setwd("~/git/pan/538/20210117")
rm(list = ls())

# Possible 3 single-digit factorizations are as follows:
# 294: {6, 7, 7}
# 216: {4, 6, 9}, {6, 6, 6}
# 135: {3, 5, 9}
# 98: {2, 7, 7}
# 112: {4, 4, 7}, {2, 7, 8}
# 84: {3, 4, 7}
# 245: {5, 7, 7}
# 40: {2, 4, 5}
# There are only X ways to permute the table given these factorizations, so a 
# brute force method can be used. The correct table permutation is
# 

iteration.count = 0
table.rows = list(list(c(6, 7, 7)),
                  list(c(4, 6, 9), c(6, 6, 6)),
                  list(c(3, 5, 9)),
                  list(c(2, 7, 7)),
                  list(c(4, 4, 7), c(2, 7, 8)),
                  list(c(3, 4, 7)),
                  list(c(5, 7, 7)),
                  list(c(2, 4, 5)))

row.targets = c(294, 216, 135, 98, 112, 84, 245, 40)
col.targets = c(8890560, 156800, 55556)

perm.3 = permn(1:3)

table.entries = matrix(nrow = length(table.rows), ncol = 3)

row.num = 2
possible.factorization = table.rows[[row.num]][[1]]
for (row.num in 1:length(table.rows)){
  for (possible.factorization in table.rows[[row.num]]){
    for (permutation in perm.3){
      table.entries[row.num,] = possible.factorization[permuatation]
    }
  }
}
