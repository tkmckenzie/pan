max_n = int(1e6)
for n in range(1, max_n):
	multiples = [n * i for i in range(1, 7)]
	digits = [''.join(sorted(str(i))) for i in multiples]
	if len(set(digits)) == 1: break

print(n)
