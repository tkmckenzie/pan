import numpy as np

def step(n):
    return sum(np.power(np.int8(np.array(list(str(n)))), 2))
def sequence(n):
    while n != 89 and n != 1:
        n = step(n)
    return n

max_n = 10000000
count_89 = 0
for n in range(1, max_n):
    if sequence(n) == 89: count_89 += 1
    
print(count_89)
