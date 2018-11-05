import numpy as np

max_num = 10000

primes = [2]
current_num = 3
while True:
    if not any([current_num % prime == 0 for prime in primes]):
        primes.append(current_num)
    else:
        if current_num % 2 == 1:
            squares = [2 * k**2 for k in np.arange(0, np.floor(np.sqrt(current_num / 2)) + 1)]
            remainders = [current_num - square for square in squares]
            
            if not any([remainder in primes for remainder in remainders]):
                print(current_num)
                break
    
    current_num += 1
    if current_num >= max_num: break

