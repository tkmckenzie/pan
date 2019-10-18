rm(list = ls())

area.intersect = function(r, d){
  integrand = function(phi){
    return((r - (d - r) / cos(phi))^2)
  }
  theta = acos(d / (2 * r))
  
  integrate.result = integrate(integrand, -theta, theta)
  if (integrate.result$message != "OK") stop(paste0("Integration failed with message ", integrate.result$message))
  
  return(integrate.result$value)
}

optimal.d = function(r){
  area.circle = pi * r^2
  uniroot.result = uniroot(function(d) area.circle - 2 * area.intersect(r, d), c(r, 2 * r))
  return(uniroot.result$root)
}

r = 5
optimal.d(r) / r

A.I = area.intersect(r, optimal.d(r))
A.C = pi * r^2

(A.C - A.I) - A.I
