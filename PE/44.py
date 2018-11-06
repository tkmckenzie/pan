import numpy as np

max_n_2 = int(1e4)

def quad_form(a, b, c):
    #Finds solution to quadratic equation a*x^2 + b*x + c = 0
    det = b**2 - 4 * a * c
    if det < 0:
        solutions = []
    else:
        det_sqrt = np.sqrt(det)
        solutions = [(-b + det_sqrt) / (2 * a), (-b - det_sqrt) / (2 * a)]
    return solutions

def gen_pent(n):
    return n * (3 * n - 1) / 2

results = []
#n_2 = np.random.randint(1, max_n_2 + 1)
for n_2 in range(1, max_n_2 + 1):
    n_bounds = sorted(quad_form(36, -12, -24 * n_2 * (3 * n_2 - 1) - 1))
    n_bounds[0] = max(n_bounds[0], 1)
    if n_bounds[1] < 0: raise ValueError('Upper bound for n is negative.')
    n_bounds[0] = int(np.ceil(n_bounds[0]))
    n_bounds[1] = int(np.floor(n_bounds[1]))
    
#    n = np.random.randint(n_bounds[0], n_bounds[1] + 1)
    for n in range(n_bounds[0], n_bounds[1] + 1):
        n_1_solution = quad_form(1.5, -0.5, gen_pent(n_2) - gen_pent(n))
        n_1_solution = list(filter(lambda x: 0 < x < n and x == np.floor(x), n_1_solution))
        
        if len(n_1_solution) > 0:
            m_solution = quad_form(1.5, -0.5, n * (3 * n - 1) / 2 - n_2 * (3 * n_2 - 1))
            m_solution = list(filter(lambda x: 0 < x < n and x == np.floor(x), m_solution))
            
            if len(m_solution) > 0:
                results.append([n_1_solution, n_2, n, m_solution])

print(results)
# [[[1020.0], 2167, 2395, [1912.0]]]

print(gen_pent(2167) - gen_pent(1020))
print(gen_pent(1912))

print(gen_pent(2167) + gen_pent(1020))
print(gen_pent(2395))
