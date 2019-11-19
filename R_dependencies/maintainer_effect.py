from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
import pickle as pkl
import re

with open('maintainers.pkl', 'rb') as pkl_file:
	mntnrs = pkl.load(pkl_file)

with open('package_network.pkl', 'rb') as pkl_file:
	n_pkg = pkl.load(pkl_file)
	
with open('maintainer_network.pkl', 'rb') as pkl_file:
	n_mntnr = pkl.load(pkl_file)

num_pkgs = len(n_pkg.nodes())

n = nx.compose(n_pkg, n_mntnr)

print(len(nx.descendants(n, 'Hadley Wickham')) / num_pkgs)

pkg_dict = {}
for mntnr in n_mntnr.nodes():
	pkg_dict[mntnr] = set(nx.descendants(n, mntnr))

num_mntnrs = len(mntnrs)
reach_list = []
for i in range(num_mntnrs):
	num_mntnr_pkgs = {}
	for mntnr in mntnrs:
		key = len(pkg_dict[mntnr])
		
		if key in num_mntnr_pkgs:
			num_mntnr_pkgs[key].append(mntnr)
		else:
			num_mntnr_pkgs[key] = [mntnr]
	
	max_num_pkgs = max(num_mntnr_pkgs.keys())
	max_mntnr = num_mntnr_pkgs[max_num_pkgs][0]
	max_mntnr_pkgs = list(pkg_dict[max_mntnr])
	
	for mntnr in mntnrs:
		pkg_dict[mntnr].difference_update(max_mntnr_pkgs)
	
	reach_list.append((max_mntnr,  max_num_pkgs))
	
#	if np.cumsum([e[1] for e in reach_list])[-1] == 15142: break

plt.plot(np.cumsum([e[1] for e in reach_list])[:100] / num_pkgs, '.')
plt.ylim(bottom = 0)
