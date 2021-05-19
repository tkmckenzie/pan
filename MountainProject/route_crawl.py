from methods import *

route_id_init = '106860025'
num_levels = 1

routes = set([Route(route_id_init)])
route_ids = set([route.id for route in routes])

##################################################
# Figuring out what to do about Forbidden requests
#url_request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#url_request_headers = {}
#route = list(routes)[0]
#url = 'https://www.mountainproject.com/data/get-routes?routeIds=' + route.id + '&key=200497839-649bb2747b48a6dbc86336b8fab99b45'
#request = urllib.request.Request(url, headers = url_request_headers)
#page = urllib.request.urlopen(request)
##################################################

users = set([tick['user'] for route in routes for tick in route.retrieve_ticks(url_request_headers) if tick['user'].id != ''])
user_ids = set([user.id for user in users])

new_users = users
for level in range(num_levels):
	new_route_ids = set([str(tick['routeId']) for user in new_users for tick in user.retrieve_ticks()])
	new_route_ids.difference_update(route_ids)
	new_routes = [Route(route_id) for route_id in new_route_ids]
	
	print('Step ' + str(level + 1) + ': ' + str(len(new_routes)) + ' new routes found.')
	routes.update(new_routes)
	route_ids.update(new_route_ids)
	
#	for route in new_routes:
#		for tick in route.retrieve_ticks():
#			user_id = tick['user'].id
	new_user_ids = set([str(tick['user'].id) for route in new_routes for tick in route.retrieve_ticks() if tick['user'].id != ''])
	new_user_ids.difference_update(user_ids)
	new_users = [User(user_id) for user_id in new_user_ids]
	
	print('Step ' + str(level + 1) + ': ' + str(len(new_users)) + ' new users found.')
	users.update(new_users)
	user_ids.update(new_user_ids)
	
	print()
