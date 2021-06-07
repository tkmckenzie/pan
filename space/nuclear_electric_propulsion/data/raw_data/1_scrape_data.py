from bs4 import BeautifulSoup as bs
import requests

electric_url = 'http://www.astronautix.com/e/electricxenon.html'
nuclear_url = 'http://www.astronautix.com/n/nuclear-powered.html'

##################################################
# Electric xenon propulsion data
page = requests.get(electric_url)
soup = bs(page.content, features = 'lxml')

table_entries = soup.findAll('table')
table_links = list(map(lambda entry: '/../' + entry.find('a').attrs['href'], table_entries))

for link in table_links[:1]:
    page = requests.get(electric_url + link)
    soup = bs(page.content, features = 'lxml')