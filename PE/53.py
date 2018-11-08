from numpy import math as npm

def choose(n, r):
    return npm.factorial(n) / (npm.factorial(r) * npm.factorial(n - r))
def log_sum(n):
    #Gives sum of log(1), ..., log(n)
    #Equivalent to log(n!)
    return sum(map(npm.log, range(2, n + 1)))
def log_choose(n, r):
    return log_sum(n) - log_sum(r) - log_sum(n - r)

threshold = npm.log(1e6)
count = 0
for n in range(1, 101):
    for r in range(n + 1):
        if log_choose(n, r) > threshold:
            count += 1

print(count)
