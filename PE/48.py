def pow_mod(n, power, mod):
    base = n
    factor = 1
    base %= mod
    while power > 0:
        factor *= base
        power -= 1
        factor %= mod
    return factor

term_mods = list(map(lambda n: pow_mod(n, n, 10**10), range(1, 1001)))
term_sum = sum(term_mods)

print(term_sum % (10**10))
