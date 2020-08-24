import csv
import numpy as np

class Graph:
	def __init__(self, names, distance_matrix, starting_point, ending_point):
		self.names = set(names)
		self.distance_matrix = np.array(distance_matrix)
		self.distance_dict = {names[i]:{names[j]: self.distance_matrix[i,j] for j in range(self.distance_matrix.shape[1])} for i in range(self.distance_matrix.shape[0])}
		
		if starting_point in names:
			self.starting_point = starting_point
		else:
			raise ValueError('starting_point must be one of names.')
			
		if ending_point in names:
			self.ending_point = ending_point
		else:
			raise ValueError('ending_point must be one of names.')
		
class Individual:
	def __init__(self, graph, path = None):
		self.graph = graph
		
		if path == None:
			remaining_points = self.graph.names.difference([graph.starting_point, graph.ending_point])
			self.path = [self.graph.starting_point] + list(np.random.choice(list(remaining_points), size = len(remaining_points), replace = False)) + [graph.ending_point]
		else:
			self.path = path
		
		self.fitness = self.calculate_fitness()
		
	def calculate_fitness(self):
		path_length = 0
		for i in range(len(self.path) - 1):
			name_1 = self.path[i]
			name_2 = self.path[i + 1]
			
			path_length += self.graph.distance_dict[name_1][name_2]
		
		return -path_length
	
	def mutate(self):
		index_1, index_2 = np.random.choice(range(1, len(self.path) - 1), size = 2, replace = False)
		
		name_1 = self.path[index_1]
		name_2 = self.path[index_2]
		
		new_path = list(self.path)
		new_path[index_1] = name_2
		new_path[index_2] = name_1
		
		new_individual = Individual(self.graph, new_path)
		
		return(new_individual)
		
	def procreate(self, temperature):
		# Returns next generation
		# Child is returned if more fit or by MH step
		# Parent (self) is returned otherwise
		child = self.mutate()
		
		if child.fitness >= self.fitness:
			return child
		else:
			prob = np.power(2.7, (child.fitness - self.fitness) / temperature)
			
			if np.random.uniform() < prob:
				return child
			else:
				return self

def csv_to_graph(file_name, starting_point, ending_point):
	f = open(file_name, 'r')
	f_csv = csv.reader(f)
	
	data = np.array([row for row in f_csv])
	
	col_names = data[1:,0]
	row_names = data[0,1:]
	
	if not (col_names == row_names).all():
		raise ValueError('Column and row names must match.')
	
	distance_matrix = data[1:,1:].astype(float)
	
	return Graph(col_names, distance_matrix, starting_point, ending_point)
