from numpy import math as npm
import numpy as np
from primes import primeFactors

max_val = int(1e6)

def phi(n):
    #Using Euler's formula: phi(n) = n \prod_{p|n} (1 - 1 / p),
    #where p|n are primes that divide n
    if n % 100000 == 0: print(n)
    
    factors = set(primeFactors(n))
    prime_div = np.array(list(factors))
    return n * np.prod(1 - 1 / prime_div)

n_val = np.array(range(2, max_val + 1))
phi_val = np.array(list(map(phi, n_val)))

n_div_phi = n_val / phi_val

n_val[np.argmax(n_div_phi)]
