from fractions import Fraction
import numpy as np

d_max = int(1e6)

fractions = np.array(sorted({Fraction(i, d) for d in range(1, d_max + 1) for i in range(1, d)}))

index = np.argwhere(fractions == Fraction(3, 7))[0][0]
print(fractions[index - 1])
