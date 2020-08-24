import csv
import numpy as np
import TSP

# Define parameters
population_size = 10
temperature = 100000000
min_temperature = 0.00001

def update_temperature(temperature): return temperature * 0.999

# Read graph data
graph = TSP.csv_to_graph('state_distances.csv', 'New Mexico', 'New Mexico')

# Create population
population = [TSP.Individual(graph) for i in range(population_size)]

num_iter = 0
while temperature >= min_temperature:	
	for i in range(population_size):
		population[i] = population[i].procreate(temperature)
	
	temperature = update_temperature(temperature)
	
	num_iter += 1

distances = [-individual.fitness for individual in population]
fittest_individual = population[np.argmin(distances)]

print('Shortest path: %.3f miles' % (-fittest_individual.fitness))
print('Shortest path: ' + ','.join(fittest_individual.path))

out_file = open('shortest_path.csv', 'w')
out_csv = csv.writer(out_file, lineterminator = '\n')
out_csv.writerow(['cumulative.distance', 'name'])

cumulative_distance = 0
old_state = fittest_individual.path[0]
for state in fittest_individual.path:
	cumulative_distance += graph.distance_dict[old_state][state]
	out_csv.writerow([cumulative_distance, state])
	old_state = state
out_file.close()
