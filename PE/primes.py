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

def sieve(max_n):
    #Sieve of Eratosthenes
    #mem_eff is an indicator of whether to use memory-efficient algorithm (good for large max_n)
    primes = [2]
    all_nums = set(np.arange(3, max_n, 2, int))
    while len(all_nums) > 0:
        current_prime = min(all_nums)
        
        if current_prime > np.sqrt(max_n): break
        
        multiples = np.arange(current_prime, max_n, current_prime)
        all_nums.difference_update(multiples)
        primes.append(current_prime)
    
    primes.extend(all_nums)
    primes.sort()
        
    return primes
