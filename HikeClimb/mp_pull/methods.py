import datetime as dt
import networkx as nx

class AreaGraph:
	def __init__(self, area_dict):
		self.graph = self.dict_to_graph(area_dict)
	
	def dict_to_graph(self, area_dict):
		g = nx.Graph()
		g.add_node('head')
		self.update_dict(g, area_dict, 'head')
		
		g.remove_node('head')
		
		return g
		
	def update_dict(self, g, sub_area_dict, super_area_key):
		keys = sub_area_dict.keys()
		
		for key in keys:
			self.convert_date(sub_area_dict[key]['info'])
			g.add_node(key, **sub_area_dict[key]['info'])
			g.add_edge(super_area_key, key)
			
			if len(sub_area_dict[key]['entries']) > 0:
				self.update_dict(g, sub_area_dict[key]['entries'], key)
	
	def convert_date(self, entry_info_dict):
		if entry_info_dict['share_date'] != 'NA':
			entry_info_dict['share_date'] = dt.datetime.strptime(entry_info_dict['share_date'], '%b %d, %Y')

	def filter_nodes_by_date(self, func):
		# func is a boolean lambda function of share_date indicating which nodes to keep
		delete_nodes = filter(lambda n: self.graph.nodes[n]['share_date'] == 'NA' or not func(self.graph.nodes[n]['share_date']), list(self.graph.nodes))
		self.graph.remove_nodes_from(delete_nodes)
	
	def filter_nodes_by_type(self, func):
		# func is a boolean lambda function of type indicating which nodes to keep
		delete_nodes = filter(lambda n: self.graph.nodes[n]['page_type'] == 'area' or not func(self.graph.nodes[n]['type']), list(self.graph.nodes))
		self.graph.remove_nodes_from(delete_nodes)
