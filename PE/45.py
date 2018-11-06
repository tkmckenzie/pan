import numpy as np

min_n_hex = 1
max_n_hex = int(1e5)

def quad_form(a, b, c):
    #Finds solution to quadratic equation a*x^2 + b*x + c = 0
    det = b**2 - 4 * a * c
    if det < 0:
        solutions = []
    else:
        det_sqrt = np.sqrt(det)
        solutions = [(-b + det_sqrt) / (2 * a), (-b - det_sqrt) / (2 * a)]
    return solutions

def gen_hex(n):
    return n * (2 * n - 1)
def gen_pent(n):
    return n * (3 * n - 1) / 2
def gen_tri(n):
    return n * (n + 1) / 2

results = []
for n_hex_val in range(min_n_hex, max_n_hex + 1):    
    n_pent = quad_form(1.5, -0.5, -gen_hex(n_hex_val))
    n_pent = list(filter(lambda n: n > 0 and n == np.floor(n), n_pent))
    
    for n_pent_val in n_pent:
        n_tri = quad_form(0.5, 0.5, -gen_pent(n_pent_val))
        n_tri = list(filter(lambda n: n > 0 and n == np.floor(n), n_tri))
        
        results.extend([(int(n_tri_val), int(n_pent_val), n_hex_val) for n_tri_val in n_tri])

print(results)
print([int(gen_tri(result[0])) for result in results])
