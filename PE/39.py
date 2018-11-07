import numpy as np
import pandas as pd

num_coprime_iter = 20

def gen_coprime(a):
    m = a[0]
    n = a[1]
    
    b1 = (2 * m - n, m)
    b2 = (2 * m + n, m)
    b3 = (m + 2 * n, n)
    
    return [b1, b2, b3]
def triple(m, n, k):
    a = k * (m**2 - n**2)
    b = 2 * m * n * k
    c = k * (m**2 + n**2)
    return (a, b, c)
def perimeter(m, n, k):
    return 2 * m * k * (m + n)
def max_k(m, n, p):
    return(int(np.floor(p / (2 * m * (m + n)))))

coprimes = [[(2, 1), (3, 1)]]
coprime_iter = 0
for coprime_iter in range(num_coprime_iter):
    added_coprimes = map(gen_coprime, coprimes[coprime_iter])
    added_coprimes = [pair for l in added_coprimes for pair in l if perimeter(pair[0], pair[1], 1) <= 100000]
    coprimes.append(added_coprimes)

min_perimeter = [min([perimeter(pair[0], pair[1], 1) for pair in pairs]) for pairs in coprimes]
print(min_perimeter)

coprimes = [(pair[0], pair[1], 1) for l in coprimes for pair in l if perimeter(pair[0], pair[1], 1) <= 1000]
coprimes_extended = [[(pair[0], pair[1], k) for k in range(1, max_k(pair[0], pair[1], 1000) + 1)] for pair in coprimes]
coprimes_extended = [t for l in coprimes_extended for t in l]

coprimes = coprimes_extended

triples = {}
for z in coprimes:
    p = perimeter(z[0], z[1], z[2])
    t = sorted(triple(z[0], z[1], z[2]))
    try:
        triples[p].append(t)
    except KeyError:
        triples[p] = [t]

lengths = {key: pd.DataFrame(triples[key]).drop_duplicates().shape[0] for key in triples.keys()}