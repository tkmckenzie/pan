f.to.c = function(x){
  return((x - 32) * 5 / 9)
}
c.to.f = function(x){
  return(x * 9 / 5 + 32)
}

does.satisfy = function(f){
  c = round(f.to.c(f))
  c.rev = as.numeric(paste0(rev(strsplit(as.character(c), "")[[1]]), collapse = ""))
  return(f == c.rev)
}

f.range = c(32, 212)
for (f in f.range[1]:f.range[2]){
  if (does.satisfy(f)) print(f)
}