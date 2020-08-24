rm(list = ls())

abo.base.types = c("A", "B", "O")
rh.base.types = c("-", "+")

abo.types = unique(apply(expand.grid(abo.base.types, abo.base.types), 1, function(v) paste0(sort(v), collapse = "")))
rh.types = unique(apply(expand.grid(rh.base.types, rh.base.types), 1, function(v) paste0(sort(v), collapse = "")))

num.abo.types = length(abo.types)
num.rh.types = length(rh.types)

# Initialize state vector
type.dist = rep(1 / (num.abo.types * num.rh.types), num.abo.types * num.rh.types)
names(type.dist) = apply(expand.grid(abo.types, rh.types), 1, paste0, collapse = "")

# Transition function
parent.1.type = "AB-+"
parent.2.type = "AO--"
state = type.dist

transition.abo = function(parent.1.abo, parent.2.abo){
  possible.types = apply(expand.grid(strsplit(parent.1.abo, "")[[1]], strsplit(parent.2.abo, "")[[1]]), 1, function(v) paste0(sort(v), collapse = ""))
  num.possible.types = length(possible.types)
  
  out = rep(1 / num.possible.types, num.possible.types)
  names(out) = possible.types
  
  return(out)
}
transition.rh = function(parent.1.rh, parent.2.rh){
  possible.types = apply(expand.grid(strsplit(parent.1.rh, "")[[1]], strsplit(parent.2.rh, "")[[1]]), 1, function(v) paste0(sort(v), collapse = ""))
  num.possible.types = length(possible.types)

  out = rep(1 / num.possible.types, num.possible.types)
  names(out) = possible.types
  
  return(out)
}
transition.type = function(parent.1.type, parent.2.type){
  parent.1.abo = substr(parent.1.type, 1, 2)
  parent.1.rh = substr(parent.1.type, 3, 4)
  
  parent.2.abo = substr(parent.2.type, 1, 2)
  parent.2.rh = substr(parent.2.type, 3, 4)
  
  abo.new = transition.abo(parent.1.abo, parent.2.abo)
  rh.new = transition.rh(parent.1.rh, parent.2.rh)
  
  out = apply(expand.grid(abo.new, rh.new), 1, prod)
  names(out) = apply(expand.grid(names(abo.new), names(rh.new)), 1, paste0, collapse = "")
  
  return(out)
}
transition = function(state){
  parent.combinations = expand.grid(names(state), names(state), stringsAsFactors = FALSE)
  parent.combinations$prob = apply(parent.combinations, 1, function(v) state[v[1]] * state[v[2]])
  
  raw.list = apply(parent.combinations, 1, function(v) transition.type(v[1], v[2]))
}
