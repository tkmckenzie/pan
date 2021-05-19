from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.mountainproject.com/area/105708964/new-mexico'

driver = webdriver.Firefox()
driver.get(base_url)
