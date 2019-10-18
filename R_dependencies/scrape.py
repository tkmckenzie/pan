from bs4 import BeautifulSoup as bs
import csv
import os
import re
import urllib

# Finding list of all packages
package_list_url = 'https://cran.r-project.org/web/packages/available_packages_by_name.html'
package_list_html = urllib.request.urlopen(package_list_url).read()

package_list_soup = bs(package_list_html, 'lxml')
table_entries = package_list_soup.find_all('tr')
table_entries = filter(lambda entry: len(entry.attrs) == 0, table_entries)

package_names = list(map(lambda entry: entry.find('a').text, table_entries))

if 'package_data.csv' in os.listdir():
	data_file = open('package_data.csv', 'r')
	data_csv = csv.reader(data_file)
	data_csv.__next__()
	existing_package_names = [row[0] for row in data_csv]
	data_file.close()
	
	out_file = open('package_data.csv', 'a')
	out_csv = csv.writer(out_file, lineterminator = '\n')
else:
	existing_package_names = []
	
	out_file = open('package_data.csv', 'w')
	out_csv = csv.writer(out_file, lineterminator = '\n')
	out_csv.writerow(['package.name', 'dependencies', 'imports', 'suggestions', 'authors', 'maintainers'])

for package_name in package_names:
	if not package_name in existing_package_names:
		print(package_name)
		url_opened = False
		while not url_opened:
			try:
				package_url = 'https://CRAN.R-project.org/package=' + package_name
				package_html = urllib.request.urlopen(package_url).read()
				package_soup = bs(package_html, 'lxml')
				url_opened = True
			except urllib.error.URLError:
				print('*** Failed to open page for ' + package_name + '; retrying ***')
		
		table_entries = package_soup.find_all('tr')
		
		depends_entry = list(filter(lambda entry: re.search('^Depends:', entry.text.strip()), table_entries))
		if len(depends_entry) > 1: raise ValueError('Found ' + str(len(depends_entry)) + ' depends entries for package ' + package_name)
		if len(depends_entry) > 0:
			depends_entry = depends_entry[0]
			dependencies = depends_entry.find_all('td')[1].text.split(', ')
		else:
			dependencies = []
			
		imports_entry = list(filter(lambda entry: re.search('^Imports:', entry.text.strip()), table_entries))
		if len(imports_entry) > 1: raise ValueError('Found ' + str(len(imports_entry)) + ' imports entries for package ' + package_name)
		if len(imports_entry) > 0:
			imports_entry = imports_entry[0]
			imports = imports_entry.find_all('td')[1].text.split(', ')
		else:
			imports = []
	
		suggests_entry = list(filter(lambda entry: re.search('^Suggests:', entry.text.strip()), table_entries))
		if len(suggests_entry) > 1: raise ValueError('Found ' + str(len(suggests_entry)) + ' suggests entries for package ' + package_name)
		if len(suggests_entry) > 0:
			suggests_entry = suggests_entry[0]
			suggestions = suggests_entry.find_all('td')[1].text.split(', ')
		else:
			suggestions = []
			
		author_entry = list(filter(lambda entry: re.search('^Author:', entry.text.strip()), table_entries))
		if len(author_entry) > 1: raise ValueError('Found ' + str(len(author_entry)) + ' author entries for package ' + package_name)
		if len(author_entry) > 0:
			author_entry = author_entry[0]
			authors = author_entry.find_all('td')[1].text.split(', ')
		else:
			authors = []
	
		maintainer_entry = list(filter(lambda entry: re.search('^Maintainer:', entry.text.strip()), table_entries))
		if len(maintainer_entry) > 1: raise ValueError('Found ' + str(len(maintainer_entry)) + ' maintainer entries for package ' + package_name)
		if len(maintainer_entry) > 0:
			maintainer_entry = maintainer_entry[0]
			maintainers = maintainer_entry.find_all('td')[1].text.split(', ')
		else:
			maintainers = []
			
		# Replacing problematic characters in strings
		dependencies_str = ','.join(dependencies)
		imports_str = ','.join(imports)
		suggestions_str = ','.join(suggestions)
		authors_str = ','.join(authors)
		maintainers_str = ','.join(maintainers)
		
		replace_chars = {'≥': '>=', '≤': '<=', 'ł': 'l', 'č': 'c', 'ó': 'o', 'ń': 'n',
				   'ğ': 'g', 'Ö': 'O'}
		replace_char = list(replace_chars.keys())[0]
		for replace_char in replace_chars.keys():
			dependencies_str = re.sub(replace_char, replace_chars[replace_char], dependencies_str)
			imports_str = re.sub(replace_char, replace_chars[replace_char], imports_str)
			suggestions_str = re.sub(replace_char, replace_chars[replace_char], suggestions_str)
			authors_str = re.sub(replace_char, replace_chars[replace_char], authors_str)
			maintainers_str = re.sub(replace_char, replace_chars[replace_char], maintainers_str)
		
		# Write to file
		out_csv.writerow([package_name,
						dependencies_str,
						imports_str,
						suggestions_str,
						authors_str,
						maintainers_str])

out_file.close()
