import numpy as np

def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    else:
        for i in np.arange(3, np.floor(np.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(int(i))
                n /= i
    if n > 2:
        factors.append(int(n))
    
    return(factors)
