import BloodType
import math
import random

N_init = 1000
children_per_couple = 2 # Assume all children survive to procreate
num_generations = 10000

possible_abo = ['A', 'B', 'O']
possible_rh = ['+', '-']

population = [BloodType.randomPerson() for i in range(N_init)]

for gen_i in range(num_generations):
	population_size = len(population)
	num_couples = math.floor(population_size / 2)
	
	parent_1_list = population[:num_couples]
	parent_2_list = population[num_couples:]
	
	new_population = []
	for couple_i in range(num_couples):
		for child_i in range(children_per_couple):
			new_population.append(parent_1_list[couple_i].procreate(parent_2_list[couple_i]))
	
	population = new_population
	random.shuffle(population)

population_size = len(population)
population_expressed_types = [person.expressed_type() for person in population]
all_expressed_types = sorted(set(population_expressed_types))

proportion_expressed_types = {expressed_type: sum([person_type == expressed_type for person_type in population_expressed_types]) / population_size for expressed_type in all_expressed_types}
print(proportion_expressed_types)
