from fractions import Fraction
import numpy as np

def expansion(n):
    x = Fraction(2)
    for i in range(n):
        x = Fraction(2) + 1 / x
    return 1 + 1 /  x

series = list(map(expansion, range(1000)))

results = list(filter(lambda f: len(str(f.numerator)) > len(str(f.denominator)), series))
#results = []
#for f in series:
#    if len(str(f.numerator)) > len(str(f.denominator)):
#        results.append(f)

print(len(results))
