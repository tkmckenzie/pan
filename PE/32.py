import numpy as np
import itertools

def is_pandigital(s):
    a = list(s)
    all_digits = all([c in '123456789' for c in a])
    no_reps = len(a) == len(set(a)) == 9
    return all_digits and no_reps

max_num_digits_n = 3

results = []
for num_digits_n in range(1, max_num_digits_n + 1):
    n_iter = itertools.permutations(range(1, 10), num_digits_n)
    for n_list in n_iter:
        n = int(''.join([str(n) for n in n_list]))
        
        min_num_digits_m = int(np.ceil(4.5 - num_digits_n))
        max_num_digits_m = int(np.floor(5 - num_digits_n))
        
        possible_digits_m = set(range(1, 10)).difference([int(c) for c in list(str(n))])
        
        for num_digits_m in range(min_num_digits_m, max_num_digits_m + 1):
            m_iter = itertools.permutations(possible_digits_m, num_digits_m)
            for m_list in m_iter:
                m = int(''.join([str(m) for m in m_list]))
                prod = n * m
                s_total = str(n) + str(m) + str(prod)
                if is_pandigital(s_total):
                    results.append((n, m, prod))

prods = [result[2] for result in results]
print(sum(set(prods)))
