import numpy as np

def no_rep(n):
    #Returns True if all digits in n are unique
    a = list(pad_num(n))
    a_set = set(a)
    if len(a) == len(a_set):
        return True
    else:
        return False
def pad_num(n):
    if n < 10:
        return '0' * 2 + str(n)
    elif n < 100:
        return '0' + str(n)
    else:
        return str(n)
def sub_num(s, start, stop):
    return s[start:stop]
def concat_num(a):
    return(''.join([s[0] for s in a[:-1]]) + a[-1])
def is_pandigital(s):
    a = list(s)
    a_set = set(a)
    no_reps = len(a) == len(a_set)
    
    membership = [c in a for c in '0123456789']
    sufficient_members = np.sum(membership) >= 8
    
    return no_reps and sufficient_members
def missing_digit(s):
    return list(filter(lambda c: not c in s, '123456789'))[0]

primes = [2, 3, 5, 7, 11, 13, 17]
prods = {n: [pad_num(e) for e in np.arange(n, 999, n) if no_rep(e)] for n in primes}

results = []

for n_17 in prods[17]:
    mult_13 = [n for n in prods[13] if sub_num(n_17, 0, 2) == sub_num(n, 1, 3)]
    for n_13 in mult_13:
        mult_11 = [n for n in prods[11] if sub_num(n_13, 0, 2) == sub_num(n, 1, 3)]
        for n_11 in mult_11:
            mult_7 = [n for n in prods[7] if sub_num(n_11, 0, 2) == sub_num(n, 1, 3)]
            for n_7 in mult_7:
                mult_5 = [n for n in prods[5] if sub_num(n_7, 0, 2) == sub_num(n, 1, 3)]
                for n_5 in mult_5:
                    mult_3 = [n for n in prods[3] if sub_num(n_5, 0, 2) == sub_num(n, 1, 3)]
                    for n_3 in mult_3:
                        mult_2 = [n for n in prods[2] if sub_num(n_3, 0, 2) == sub_num(n, 1, 3)]
                        final_nums = [concat_num([n_2, n_3, n_5, n_7, n_11, n_13, n_17]) for n_2 in mult_2]
                        final_nums = list(filter(is_pandigital, final_nums))
                        final_nums = [missing_digit(s) + s for s in final_nums]
                        results.extend(final_nums)

print(sum([int(s) for s in results]))
