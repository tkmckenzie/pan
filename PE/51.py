import numpy as np
from primes import sieve

max_n = 100
primes = sieve(max_n)

def matching_chars(s1, s2):
	if len(s1) != len(s2): return []
	
	return [i for i in range(len(s1)) if s1[i] == s2[i]]

max_family_size = 0
max_family = []
prime = 83
asdf

while len(primes) > 0:
	prime = primes.pop(0)
	num_digits = np.floor(np.log10(prime)) + 1
	matches = list(filter(lambda n: np.floor(np.log10(n)) + 1 == num_digits, primes))
	matches = list(filter(lambda n: 1 <= len(matching_chars(str(prime), str(n))) < num_digits, matches))
	
	for match in matches: primes.remove(match)
	
	while len(matches) > 0:
		