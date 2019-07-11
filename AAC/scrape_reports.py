import bs4 as bs
import csv
import math
import re
import urllib

out_file = open('report_data/raw_aac_data.csv', 'w')
out_csv = csv.writer(out_file, lineterminator = '\n')

out_csv.writerow(['entry.num', 'year', 'entry.title', 'entry.url', 'entry.text'])

year_range = range(1990, 2019 + 1)
for year in year_range:
	print('Now scraping year %i' % year)
	year_url = 'http://publications.americanalpineclub.org/search/solr?all=&article_publication=anam&article_copyright_date=%i&article_article_type=&article_pub_title=&route_name=' % year
	while True:
		try:
			year_html = urllib.request.urlopen(year_url).read()
			break
		except:
			pass
	year_soup = bs.BeautifulSoup(year_html, 'lxml')
	
	num_records = int(re.search('[0-9]+', year_soup.find_all('h4')[1].text).group(0))
	
	entries = year_soup.find_all('td', class_ = 'highlight')
	entry_urls = [entry.find('a').attrs['href'] for entry in entries]
	
	for entry_url in entry_urls:
		entry_num = re.search('(?<=/)[0-9]+(?=/)', entry_url).group(0)
		
		while True:
			try:
				entry_html = urllib.request.urlopen(entry_url).read()
				break
			except:
				pass
		entry_soup = bs.BeautifulSoup(entry_html, 'lxml')
		
		entry_title = entry_soup.title.text
		
		entry_text = entry_soup.find_all('div', class_ = 'well-small')[0]
		entry_text = [p.text for p in entry_text.find_all('p')]
		entry_text = '\n\n'.join(entry_text).encode('utf-8').decode('ascii', 'ignore')
		
		out_csv.writerow([entry_num, year, entry_title, entry_url, entry_text])
	
	for page in range(1, math.floor(num_records / 50)):
		page_url = year_url + '&offset=' + str(50 * page)
		while True:
			try:
				page_html = urllib.request.urlopen(page_url).read()
				break
			except:
				pass
		page_soup = bs.BeautifulSoup(page_html, 'lxml')
		
		entries = page_soup.find_all('td', class_ = 'highlight')
		entry_urls = [entry.find('a').attrs['href'] for entry in entries]
		for entry_url in entry_urls:
			entry_num = re.search('(?<=/)[0-9]+(?=/)', entry_url).group(0)
			
			while True:
				try:
					entry_html = urllib.request.urlopen(entry_url).read()
					break
				except:
					pass
			entry_soup = bs.BeautifulSoup(entry_html, 'lxml')
			
			entry_title = entry_soup.title.text
			
			entry_text = entry_soup.find_all('div', class_ = 'well-small')[0]
			entry_text = [p.text for p in entry_text.find_all('p')]
			entry_text = '\n\n'.join(entry_text).encode('utf-8').decode('ascii', 'ignore')
			
			out_csv.writerow([entry_num, year, entry_title, entry_url, entry_text])

out_file.close()
