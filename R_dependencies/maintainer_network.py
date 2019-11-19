import csv
import networkx as nx
import pickle as pkl
import re

# Get data
data_file = open('package_data.csv', 'r')
data_csv = csv.reader(data_file)

# Set up storage objects
node_dict = {}
maintainers_list = []

# Find colnames
colnames = data_csv.__next__()
col_dict = {colnames[i]: i for i in range(len(colnames))}

for row in data_csv:
	package_name = row[col_dict['package.name']]
	maintainers = row[col_dict['maintainers']]
	
	maintainers = re.sub('[ ]+<[ -~]+>', '', maintainers)
	maintainers = re.sub('[\'\"]+', '', maintainers)
	
	if maintainers in node_dict.keys():
		node_dict[maintainers].append(package_name)
	else:
		node_dict[maintainers] = [package_name]

	maintainers_list.append(maintainers)

n = nx.DiGraph(node_dict)

with open('maintainer_network.pkl', 'wb') as pkl_file:
	pkl.dump(n, pkl_file)
with open('maintainers.pkl', 'wb') as pkl_file:
	pkl.dump(maintainers_list, pkl_file)

data_file.close()
