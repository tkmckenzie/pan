library(FRACTION)

rm(list = ls())

# extended.euclidean = function(a, b){
#   s = 0
#   old.s = 1
#   t = 1
#   old.t = 0
#   r = b
#   old.r = a
#   
#   while (r != 0){
#     quotient = floor(old.r / r)
#     
#     prov.r = r
#     r = old.r - quotient * prov.r
#     old.r = prov.r
#     
#     prov.s = s
#     s = old.s - quotient * prov.s
#     old.s = prov.s
#     
#     prov.t = t
#     t = old.t - quotient * prov.t
#     old.t = prov.t
#   }
#   return(c(old.s, old.t))
# }
extended.euclidean = function(a, b){
  s = 0
  old.s = 1
  r = b
  old.r = a
  
  while (r != 0){
    quotient = floor(old.r / r)
    
    prov.r = r
    r = old.r - quotient * prov.r
    old.r = prov.r
    
    prov.s = s
    s = old.s - quotient * prov.s
    old.s = prov.s
  }
  if (b != 0){
    bezout.t = (old.r - old.s * a) / b
  } else{
    bezout.t = 0
  }
  
  return(c(old.s, bezout.t))
}

##################################################
a = 538
b = 19

base.solution = extended.euclidean(a, b)
d = gcd(a, b)

n = base.solution[1]
m = base.solution[2]

c = 9665
lower.bound = -n * c / abs(b)
upper.bound = m * c / abs(a)

if (ceiling(lower.bound) > floor(upper.bound)){
  k = c()
  print("No solutions")
} else{
  k = seq(ceiling(lower.bound), floor(upper.bound), by = 1)
  print(paste0(length(k), " solution(s)"))
}

cbind(n * c / d + b * k / d, m * c / d - a * k / d)

##################################################
# Looking for c s.t. upper.bound(c) - lower.bound(c) > 1
c.max = 1 / (m / abs(a) + n / abs(b))

c = ceiling(c.max)
solution.found = FALSE
while (!solution.found){
  lower.bound = -n * c / abs(b)
  upper.bound = m * c / abs(a)
  
  if (ceiling(lower.bound) > floor(upper.bound)){
    solution = c
    solution.found = TRUE
  } else{
    c = c - 1
  }
}

solution
