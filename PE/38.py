import itertools
import numpy as np

max_num_digits = 8

def is_pandigital(s):
    a = list(s)
    all_digits = all([c in '123456789' for c in a])
    no_reps = len(a) == len(set(a)) == 9
    return all_digits and no_reps

numbers = list(range(1, 10))

n = 9
results = []
for num_digits in range(1, max_num_digits + 1):
    n_iter = itertools.permutations(numbers, num_digits)
    for n_list in n_iter:
        n = int(''.join([str(n) for n in n_list]))
        n_prods = [n]
        
        current_num_digits = np.floor(np.log10(n)) + 1
        i = 2
        while current_num_digits < 9:
            prod = n * i
            n_prods.append(prod)
            current_num_digits += np.floor(np.log10(prod)) + 1
            i += 1
#            print(current_num_digits, n_prods)

        if len(n_prods) > 1:
            n_prod_concat = ''.join([str(prod) for prod in n_prods])
            if is_pandigital(n_prod_concat):
                results.append(n_prods)
results = [int(''.join([str(n) for n in l])) for l in results]
print(sorted(results)[-1])
