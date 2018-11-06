import fractions

def without(iterable, remove_indices):
    """
    Returns an iterable for a collection or iterable, which returns all items except the specified indices.
    """
    if not hasattr(remove_indices, '__iter__'):
        remove_indices = {remove_indices}
    else:
        remove_indices = set(remove_indices)
    for k, item in enumerate(iterable):
        if k in remove_indices:
            continue
        yield item

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.float = n / d
    def cancel_num(self):
        n_digits = [int(c) for c in list(str(self.n))]
        d_digits = [int(c) for c in list(str(self.d))]
        
        results = []
        for n_i in range(len(n_digits)):
            n_digit = n_digits[n_i]
            for d_i in range(len(d_digits)):
                d_digit = d_digits[d_i]
                if n_digit == d_digit:
                    n_omit = list(without(n_digits, n_i))
                    d_omit = list(without(d_digits, d_i))
                    results.append((int(''.join([str(e) for e in n_omit])),
                                    int(''.join([str(e) for e in d_omit]))))
        return list(set(results))
    def cancel_equiv(self):
        cancellations = self.cancel_num()
        correct_cancellations = list(filter(lambda a: a[0] / a[1] == self.float, cancellations))
        
        return(correct_cancellations)

results = []
for n_1 in range(1, 10):
    for n_2 in range(1, 10):
        n = int(str(n_1) + str(n_2))
        
        #First make first digit in denominator common
        for d_1 in list(set([n_1, n_2])):
            for d_2 in range(1, 10):
                d = int(str(d_1) + str(d_2))
                f = Fraction(n, d)
                if len(f.cancel_equiv()) > 0:
                    results.append((n, d))
        
        #Now make second digit in denominator common
        for d_2 in list(set([n_1, n_2])):
            for d_1 in range(1, 10):
                d = int(str(d_1) + str(d_2))
                f = Fraction(n, d)
                if len(f.cancel_equiv()) > 0:
                    results.append((n, d))

results = list(filter(lambda a: a[0] / a[1] < 1, results))
print(sorted(set(results)))

f_list = [fractions.Fraction(a[0], a[1]) for a in results]

f_prod = f_list[0]
for f in f_list[1:]:
    f_prod *= f
print(f_prod)
