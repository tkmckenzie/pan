import csv
import networkx as nx
import pickle as pkl
import re

# Define re for base R packages
base_pkgs = ['base', 'boot', 'class', 'cluster', 'codetools', 'compiler', 'datasets', 'foreign', 'graphics', 'grDevices', 'grid', 'KernSmooth', 'lattice', 'MASS', 'Matrix', 'methods', 'mgcv', 'nlme', 'nnet', 'parallel', 'rpart', 'spatial', 'splines', 'stats', 'stats4', 'survival', 'tcltk', 'tools', 'utils']

# Get data
data_file = open('package_data.csv', 'r')
data_csv = csv.reader(data_file)

# Set up storage dict
node_dict = {}

# Find colnames
colnames = data_csv.__next__()
col_dict = {colnames[i]: i for i in range(len(colnames))}

for row in data_csv:
	package_name = row[col_dict['package.name']]
	dependencies = row[col_dict['dependencies']].split(',')
	imports = row[col_dict['imports']].split(',')
	
	dependent_pkgs = set(dependencies + imports)
	
	# Remove version info
	dependent_pkgs = set(map(lambda s: re.sub('\\([\\n-~]+\\)', '', s).strip(), dependent_pkgs))
	
	# Remove base packages
	dependent_pkgs.difference_update(base_pkgs)
	
	# Add to dict
	node_dict[package_name] = list(dependent_pkgs)

n = nx.DiGraph(node_dict)
n.remove_nodes_from(list(filter(lambda s: re.search('^R ', s), n.nodes)))

n = n.reverse()

with open('package_network.pkl', 'wb') as pkl_file:
	pkl.dump(n, pkl_file)

data_file.close()
