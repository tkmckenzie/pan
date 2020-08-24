import csv
import numpy as np
import TSP

# Define parameters
population_size = 1
temperature = 1000000
min_temperature = 0.0001

def update_temperature(temperature): return temperature * 0.999

# Read graph data
graph = TSP.csv_to_graph('state_distances.csv', 'New Mexico', 'New Mexico')

# Create population
individual = TSP.Individual(graph)

out_file = open('shortest_path_iterative.csv', 'w')
out_csv = csv.writer(out_file, lineterminator = '\n')
out_csv.writerow(['cumulative.distance', 'name', 'iteration'])

num_iter = 0
while temperature >= min_temperature:	
	for i in range(population_size):
		individual = individual.procreate(temperature)
	
	temperature = update_temperature(temperature)
	
	cumulative_distance = 0
	old_state = individual.path[0]
	for state in individual.path:
		cumulative_distance += graph.distance_dict[old_state][state]
		out_csv.writerow([cumulative_distance, state, num_iter])
		old_state = state
	
	num_iter += 1

out_file.close()

print('Path length: %.3f miles' % (-individual.fitness))
print('Path: ' + ','.join(individual.path))
