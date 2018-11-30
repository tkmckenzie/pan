import numpy as np
from numpy.polynomial.polynomial import Polynomial
import scipy.optimize as spo

#Express
#Lose = 0 points
#Tie = 1 point
#Win = 2 points
#For a 12 game match, need at least 13 points

p = Polynomial((0.15, 0.65, 0.2))

def win_prob(N):
    wins_needed = int(np.ceil(N + 1))
    return sum((p**N).coef[wins_needed:])

print(win_prob(12))
print(win_prob(82) > 0.75 > win_prob(81))
