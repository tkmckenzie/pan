from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pickle as pkl
import re

def pull_area_urls(area_url):
	# Returns {area_url: {sub_area_url: {route_1_tuple, ...}}}
	driver.get(area_url)
	sidebar = driver.find_element_by_class_name('mp-sidebar')
	
	try:
		area_description = sidebar.find_element_by_tag_name('h3').text.split(' ')[0]
		if area_description == 'Areas':
			url_description = 'area'
		elif area_description == 'Routes':
			url_description = 'route'
		else:
			raise ValueError('area_description must be "Areas" or "Routes"; instead found "%s"' % area_description)
		area_list = sidebar.find_element_by_class_name('max-height-md-0')
		area_list_urls = [e.get_attribute('href') for e in area_list.find_elements_by_partial_link_text('')]
	except NoSuchElementException:
		url_description = 'blank area'
		
	area_name = driver.find_element_by_tag_name('h1').text
	description_table_data = driver.find_element_by_class_name('description-details').find_elements_by_tag_name('tr')
	try: 
		share_date = re.sub(' · Updates', '', list(filter(lambda e: re.search('^Shared By', e.text), description_table_data))[0].text.split(' on ')[-1])
	except IndexError:
		share_date = 'NA'
	gps = list(filter(lambda e: re.search('^GPS', e.text), description_table_data))[0].find_elements_by_tag_name('td')[-1].text.split(' Google')[0]
	page_views = list(filter(lambda e: re.search('^Page Views', e.text), description_table_data))[0].find_elements_by_tag_name('td')[-1].text
	
	if url_description == 'route':
		return {'info': {'name': area_name, 'gps': gps, 'views': page_views, 'share_date': share_date, 'page_type': 'area'}, 
		  'entries': {route_url: pull_route_info(route_url) for route_url in area_list_urls[:-1]}}
	elif url_description == 'blank area':
		return {'info': {'name': area_name, 'gps': gps, 'views': page_views, 'share_date': share_date, 'page_type': 'area'},
		  'entries': {}}
	else:
		return {'info': {'name': area_name, 'gps': gps, 'views': page_views, 'share_date': share_date, 'page_type': 'area'},
		  'entries': {sub_area_url: pull_area_urls(sub_area_url) for sub_area_url in area_list_urls}}

def pull_route_info(route_url):
	driver.get(route_url)
	
	route_name = driver.find_element_by_tag_name('h1').text
	climb_difficulty = driver.find_element_by_class_name('mr-2').text
	
	description_table_data = driver.find_element_by_class_name('description-details').find_elements_by_tag_name('tr')
	climb_type = list(filter(lambda e: re.search('^Type', e.text), description_table_data))[0].find_elements_by_tag_name('td')[-1].text
	share_date = re.sub(' · Updates', '', list(filter(lambda e: re.search('^Shared By', e.text), description_table_data))[0].text.split(' on ')[-1])
	page_views = list(filter(lambda e: re.search('^Page Views', e.text), description_table_data))[0].find_elements_by_tag_name('td')[-1].text
	
	return {'info': {'name': route_name, 'difficulty': climb_difficulty, 'type': climb_type, 'views': page_views, 'share_date': share_date, 'page_type': 'route'},
		 'entries': {}}

#area_url = 'https://www.mountainproject.com/area/107519024/red-rock-arroyo'
area_url = 'https://www.mountainproject.com/area/105708964/new-mexico'
area_name = area_url.split('/')[-1]

driver = webdriver.Firefox()
area_data = {area_url: pull_area_urls(area_url)}

with open(area_name + '.pkl', 'wb') as f:
	pkl.dump(area_data, f)

driver.close()
