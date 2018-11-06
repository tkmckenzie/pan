from primes import sieve

def no_reps(n):
    a = list(str(n))
    return len(a) == len(set(a))
def is_pandigital(n, d):
    if not no_reps(n):
        return False
    else:
        a = list(str(n))
        a = [int(c) for c in a]
        nums = set(range(1, d + 1))
        return len(nums.intersection(a)) == len(nums.union(a)) == d

asdf
max_n = int(1e7)
primes = sieve(max_n)

pandigital_primes = sorted(list(filter(lambda x: is_pandigital(x, 7), primes)))
