import datetime
from methods import *
import networkx as nx
import pandas as pd
import pickle as pkl
import re

area_name = 'new-mexico'
with open(area_name + '.pkl', 'rb') as f:
	area_dict = pkl.load(f)

g = AreaGraph(area_dict)

#g.filter_nodes_by_date(lambda d: d >= datetime.datetime(2021, 1, 1))
#g.filter_nodes_by_type(lambda t: re.search('^Trad', t))

#{'name': 'Cerro Guadalupe Rock Climbing',
# 'gps': '35.565, -107.14',
# 'views': '4,175 total · 74/month',
# 'share_date': datetime.datetime(2016, 8, 27, 0, 0),
# 'page_type': 'area'}

#{'name': 'West Gully',
# 'difficulty': '3rd YDS',
# 'type': 'Trad, 800 ft (242 m), Grade II',
# 'views': '3,493 total · 62/month',
# 'share_date': datetime.datetime(2016, 8, 27, 0, 0),
# 'page_type': 'route'}

edgelist_df = nx.to_pandas_edgelist(g.graph)
edgelist_df.to_csv('hierarchy_data.csv', index = False, line_terminator = '\n')

route_df = pd.DataFrame()
route_df['id'] = list(filter(lambda n: g.graph.nodes[n]['page_type'] == 'route', g.graph.nodes))
route_df['name'] = list(map(lambda id_str: g.graph.nodes[id_str]['name'], route_df['id']))
route_df['difficulty'] = list(map(lambda id_str: g.graph.nodes[id_str]['difficulty'], route_df['id']))
route_df['type'] = list(map(lambda id_str: g.graph.nodes[id_str]['type'], route_df['id']))
route_df['views'] = list(map(lambda id_str: g.graph.nodes[id_str]['views'], route_df['id']))
route_df['share_date'] = list(map(lambda id_str: g.graph.nodes[id_str]['share_date'], route_df['id']))
route_df.to_csv('route_data.csv', index = False, line_terminator = '\n')

area_df = pd.DataFrame()
area_df['id'] = list(filter(lambda n: g.graph.nodes[n]['page_type'] == 'area', g.graph.nodes))
area_df['name'] = list(map(lambda id_str: g.graph.nodes[id_str]['name'], area_df['id']))
area_df['gps'] = list(map(lambda id_str: g.graph.nodes[id_str]['gps'], area_df['id']))
area_df['views'] = list(map(lambda id_str: g.graph.nodes[id_str]['views'], area_df['id']))
area_df['share_date'] = list(map(lambda id_str: g.graph.nodes[id_str]['share_date'], area_df['id']))
area_df.to_csv('area_data.csv', index = False, line_terminator = '\n')
