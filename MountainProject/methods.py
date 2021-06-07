from bs4 import BeautifulSoup as bs
import json
import re
import urllib

class Route:
	def __init__(self, route_id):
		self.id = str(route_id)
		self.info_retrieved = False
		self.ticks_retrieved = False
	
	def retrieve_info(self, url_request_headers = {}):
		if not self.info_retrieved:
			url = 'https://www.mountainproject.com/data/get-routes?routeIds=' + self.id + '&key=200497839-649bb2747b48a6dbc86336b8fab99b45'
			request = urllib.request.Request(url, headers = url_request_headers)
			page = urllib.request.urlopen(request)
			self.info = json.loads(page.read())['routes'][0]
			self.info_retrieved = True
			return self.info
		else:
			return self.info
	
	def retrieve_ticks(self, url_request_headers = {}):
		if not self.ticks_retrieved:
			url = self.retrieve_info(url_request_headers = url_request_headers)['url'].replace('/route/', '/route/stats/')
			request = urllib.request.Request(url, headers = url_request_headers)
			page = bs(urllib.request.urlopen(request).read(), 'lxml')
			tick_table = page.findAll('table')[-1]
			
			tick_list = []
			rows = tick_table.findAll('tr')
			for row in rows:
				try:
					user_url = row.find('a').get('href')
					user_id = re.sub('[^0-9]+', '', user_url)
					user = User(user_id)
				except AttributeError:
					# Private tick
					user_url = ''
					user_id = ''
					user = User(user_id)
				
				dates = [e.text for e in row.findAll('strong')]
				
				entries = row.find('div').findAll('div')
				entries = [e.text[e.text.find('·'):].replace('·', '').strip() for e in entries] # · is a bullet, not a period
				
				row_dict = {'user': user, 'dates': dates, 'entries': entries}
				tick_list.append(row_dict)
			
			self.tick_list = tick_list
			self.ticks_retrieved = True
			return self.tick_list
		
		else:
			return self.tick_list
		
class User:
	def __init__(self, user_id):
		self.id = str(user_id)
		self.info_retrieved = False
		self.ticks_retrieved = False
	
	def retrieve_info(self, url_request_headers = {}):
		if not self.info_retrieved:
			url = 'https://www.mountainproject.com/data/get-user?userId=' + self.id + '&key=200497839-649bb2747b48a6dbc86336b8fab99b45'
			request = urllib.request.Request(url, headers = url_request_headers)
			page = urllib.request.urlopen(request)
			try:
				self.info = json.loads(page.read())
			except json.JSONDecodeError:
				self.info = {}
			self.info_retrieved = True
			return self.info
		else:
			return self.info
		
	def retrieve_ticks(self, url_request_headers = {}):
		if not self.ticks_retrieved:
			url = 'https://www.mountainproject.com/data/get-ticks?userId=' + self.id + '&key=200497839-649bb2747b48a6dbc86336b8fab99b45'
			request = urllib.request.Request(url, headers = url_request_headers)
			page = urllib.request.urlopen(request)
			
			try:
				self.tick_list = json.loads(page.read())['ticks']
			except json.JSONDecodeError:
				self.tick_list = []
			self.ticks_retrieved = True
			return self.tick_list
		
		else:
			return self.tick_list
