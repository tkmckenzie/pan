import TSP

# Define parameters
population_size = 10
temperature = 10000
min_temperature = 1000

def update_temperature(temperature): return temperature * 0.9

# Read graph data
names = [0, 1, 2, 3, 4]
distance_matrix = [[0, 2, 10000, 12, 5],
				   [2, 0, 4, 8, 10000],
				   [10000, 4, 0, 3, 3],
				   [12, 8, 3, 0, 10],
				   [5, 10000, 3, 10, 0]]
graph = TSP.Graph(names, distance_matrix, 0, 0)

# Create population
population = [TSP.Individual(graph) for i in range(population_size)]

while temperature >= min_temperature:
	print('Temperature: %.3f' % temperature)
	for individual in population:
		print(','.join([str(point) for point in individual.path]) + '\tLength: %.3f' % (-individual.fitness))
	print('')
	
	for i in range(population_size):
		population[i] = population[i].procreate(temperature)
	
	temperature = update_temperature(temperature)
