import numpy as np

p = 0.5
target = 0.5

max_D = 4
max_L = 4

# p_array[D, L] = prob L will win given armies of size D and L
p_array = np.zeros((max_D + max_L + 1, max_L + 1))

p_array[0,:] = 1
p_array[:,0] = 0

p_array[:,1] = p**np.arange(max_D + max_L + 1)

for L in range(2, max_L + 1):
	for D in range(1, max_D + max_L):
		p_array[D, L] = p * p_array[D - 1, L] + (1 - p) * p_array[D + 1, L - 1]
p_array = p_array[:max_D + 1, :max_L + 1]

print(p_array)

asdf
# Alternate method
p_array = np.zeros((max_D + max_L + 1, max_L + 1))

p_array[0,:] = 1
p_array[:,0] = 0

p_array[:,1] = p**np.arange(max_D + max_L + 1)

for L in range(2, max_L + 1):
	p_array[:,L] = (1 - p) * np.concatenate((p_array[1:,L-1], np.array([0])))
	