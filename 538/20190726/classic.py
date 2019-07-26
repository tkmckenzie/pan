import csv
import networkx as nx
import re

with open('state_borders.csv', 'r') as f:
	f_csv = csv.reader(f)
	border_data = {line[0]:re.sub(', ', ',', line[1]).split(',') for line in f_csv if not line[0] in ['Alaska', 'Hawaii']}
	
g = nx.DiGraph(border_data).to_undirected()

def find_chain(edge_list):
	list_len = len(edge_list)
	for i in range(list_len - 1):
		if edge_list[i][1] != edge_list[i+1][0]: break
	
	if i == list_len - 2:
		return edge_list
	else:
		return edge_list[:i+1]
	

beginning_node = 'Maine'
dfs_result = list(nx.algorithms.traversal.dfs_edges(g, beginning_node))
