rm(list = ls())

# All indices are treated as starting from zero until actually used to index a vector

# Base problem
# Ricky is player 20, second player eliminated is player 51, Zach is player 52 and third eliminated
# It must be the case that:
#   * N = 18 mod 61
#   * N = 31 mod 60
#   * N = 0 mod 59
coef.seq = 0:10000

n.60 = coef.seq * 61 + 18
n.59 = coef.seq * 60 + 31
n.58 = coef.seq * 59 + 0

N = min(intersect(n.60, intersect(n.59, n.58))) # Actually equal to N-1 by the problem by reindexing to start from zero
N+1

# Extra credit simulation
# N = 139
num.players = 61

players = 1:num.players

next.move = function(players, N, current.index, debug = FALSE){
  new.index = (current.index + N) %% length(players)
  if (debug) print(sprintf("Removing player %i at index %i.", players[new.index + 1], new.index))
  
  return(list(new.players = players[-(new.index + 1)],
              new.index = new.index))
}

current.index = 0

run.uninterrupted = TRUE
text.input = ""
while (text.input != "q" & length(players) > 1){
  move = next.move(players, N, current.index, debug = TRUE)
  players = move$new.players
  current.index = move$new.index
  
  if (!run.uninterrupted) text.input = readline() # "q" will quit
}

if (length(players) == 1){
  print(sprintf("Player %i is the winner!", players[1]))
}

# Double extra credit
for (N in 1:1000){
  players = 1:num.players
  current.index = 0
  
  while (length(players) > 1){
    move = next.move(players, N, current.index, debug = FALSE)
    players = move$new.players
    current.index = move$new.index
  }
  if (players[1] == 1){
    print(sprintf("N = %i results in Player 1 winning.", N + 1))
  }
}
