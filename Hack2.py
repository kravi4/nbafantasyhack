from selenium import webdriver
from bs4 import BeautifulSoup
import time



newDriver = webdriver.Firefox()
newDriver.get('http://stats.nba.com/tracking/#!/player/shooting/')
newDriver.set_window_position(0, 0)
newDriver.set_window_size(100000, 200000)
newDriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5) # wait to load

# now print the response
soup = BeautifulSoup(newDriver.page_source, "html.parser")
element = newDriver.find_element_by_css_selector('.page-nav.right')

data = soup.find("body").find("table", {'class': 'table'}).find('tbody').find_all("tr")
count = 0
playerStats = {}
names=""
while count < 10:
	for row in data:
		agData = row.find_all("td")
		i = 1
		stats = []
		while(i < 20):
			stats.append(agData[i].string)
			i = i + 1
		names=agData[0].string
		playerStats[names] = stats
	element.click()
	soup = BeautifulSoup(newDriver.page_source, "html.parser")
	data = soup.find("body").find("table", {'class': 'table'}).find('tbody').find_all("tr")
	count = count + 1
	
print (playerStats)