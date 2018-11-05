from primes import primeFactors

max_num = 1000
num_distinct_factors = 4
run_length = 4

current_num = 2
factor_history = []
current_run = 0
while True:
    current_factors = primeFactors(current_num)
    distinct_factors = set(current_factors)
    
    if len(distinct_factors) == num_distinct_factors:
        current_run += 1
    else:
        current_run = 0
    
    if current_run == run_length:
        break
    
    current_num += 1

print(list(range(current_num - run_length + 1, current_num + 1)))
