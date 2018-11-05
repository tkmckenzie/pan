rm(list = ls())

a.range = 2:100
b.range = 2:100

nums = c()
for (b in b.range){
  nums = union(nums, a.range^b)
}

length(nums)
