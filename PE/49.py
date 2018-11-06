from primes import sieve

def is_permutation(n1, n2):
    a1 = list(str(n1))
    a2 = list(str(n2))
    
    return sorted(a1) == sorted(a2)
def find_arithmetic(a, length = 3):
    #Finds arithmetic sequence for given length, if one exists
    #Length must be greater than 2 (arithmetic sequence of length 2 is trivial)
    if length <= 2: raise ValueError('length must be greater than 2.')
    
    sequences = []
    a = sorted(a)
    
    for i in range(len(a)):
        n1 = a[i]
        for n2 in a[i+1:]:
            diff = n2 - n1
            if all([n1 + diff * k in a for k in range(2, length)]):
                sequences.append([n1, n2] + [n1 + diff * k for k in range(2, length)])
    
    return sequences
        

primes = sieve(9999)
primes = list(filter(lambda n: n >= 1000, primes))

results = []

for prime in primes:
    prime_permutations = list(filter(lambda n: is_permutation(prime, n), primes))
    arithmetic_sequences = find_arithmetic(prime_permutations, 3)
    results.extend(arithmetic_sequences)

print(set([''.join([str(n) for n in sorted(a)]) for a in results]))
