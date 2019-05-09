import numpy as np

combn_dict = {} # Dictionary of dictionaries; first index gives total number of pieces, second index gives maximum size of piece groups, value gives number of combinations with that number of pieces and max group size
combn_dict[0] = {0: 1}
combn_dict[1] = {1: 1} # Max group size is 1, with 1 combination
combn_dict[2] = {2: 1, 1: 1}
#combn_dict[3] = {3: 1, 2: 1, 1: 1}

#max_n = 50
#for n in range(3, max_n + 1):
#	combn_dict[n] = {}
#	for max_group_size in range(int(np.ceil(n / 2)), n + 1):
#		combn_dict[n][max_group_size] = sum(combn_dict[n - max_group_size].values())
#	for max_group_size in range(1, int(np.ceil(n / 2))):
#		combn_dict[n][max_group_size] = sum([combn_dict[n - max_group_size][i] for i in range(1, max_group_size + 1)])
#		
#print([sum(combn_dict[n].values()) for n in range(1, max_n + 1)])
#for x in [sum(combn_dict[n].values()) for n in range(1, max_n + 1)]:
#	print(x)

n = 3
while True:
	combn_dict[n] = {}
	for max_group_size in range(int(np.ceil(n / 2)), n + 1):
		combn_dict[n][max_group_size] = sum(combn_dict[n - max_group_size].values())
	for max_group_size in range(1, int(np.ceil(n / 2))):
		combn_dict[n][max_group_size] = sum([combn_dict[n - max_group_size][i] for i in range(1, max_group_size + 1)])
	
	if sum(combn_dict[n].values()) % 1000000 == 0: break
	n += 1
	
print(n)
print(sum(combn_dict[n].values()))
