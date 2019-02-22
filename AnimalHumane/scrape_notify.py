import urllib3
from bs4 import BeautifulSoup as bs

http = urllib3.ProxyManager('https://wwwproxy.sandia.gov:80')

base_url = 'https://petsearch.animalhumanenm.org/search/searchResults.asp?s=adoption&searchTypeId=4&animalType=2%2C15&statusID=3&submitbtn=Find+Animals&pagesize=16&task=view&tpage='
first_page_content = bs(http.request('GET', base_url + '1').data)
