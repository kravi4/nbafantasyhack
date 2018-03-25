from selenium import webdriver
from bs4 import BeautifulSoup
import time
#import click

driver = webdriver.Firefox()
driver.get('http://stats.nba.com/tracking/#!/player/passing/?sort=PLAYER_NAME&dir=-1')
driver.set_window_position(0, 0)
driver.set_window_size(100000, 200000)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(0.1) # wait to load

# now print the response

soup = BeautifulSoup(driver.page_source, "html.parser")
element = driver.find_element_by_css_selector('.page-nav.right')

data = soup.find("body").find("table", {'class': 'table'}).find('tbody').find_all("tr")
count = 0
playerStatsTouches = {}
names = ""

while count < 10:
	for row in data:
		agData = row.find_all("td")
		i = 1
		stats = []
		while(i < 19):
			stats.append(agData[i].string)
			i = i + 1
		names = agData[0].string
		playerStatsTouches[names] = stats
	element.click()
	soup = BeautifulSoup(driver.page_source, "html.parser")
	data = soup.find("body").find("table", {'class': 'table'}).find('tbody').find_all("tr")
	count = count + 1





