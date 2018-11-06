import numpy as np
from primes import sieve

max_n = 1e6
min_length = 500
max_length = 1000

primes = sieve(max_n)
max_length = min(max_length, len(primes))

print('Primes generated.')

opt_length = 0
length = 3
for length in range(min_length, max_length + 1):
    candidate_sums = np.convolve(primes, np.ones(length, dtype = int), 'valid')
    prime_sums = np.intersect1d(candidate_sums, primes)
    if len(prime_sums) > 0:
        opt_length = length
        print(opt_length)

if opt_length > 0:
    length = opt_length
    candidate_sums = np.convolve(primes, np.ones(length, dtype = int), 'valid')
    prime_sums = np.intersect1d(candidate_sums, primes)
else:
    prime_sums = []


print(opt_length)
#print(sequences)
print(prime_sums)
