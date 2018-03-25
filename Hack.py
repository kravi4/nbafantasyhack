from selenium import webdriver
from bs4 import BeautifulSoup
import time
#import click

driver = webdriver.Firefox()
driver.get('http://stats.nba.com/tracking/#!/player/possessions/?sort=PLAYER_NAME&dir=1')
driver.set_window_position(0, 0)
driver.set_window_size(100000, 200000)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1) # wait to load

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

statsMin = {}

for names in playerStatsTouches:
	stats = []
	j = 0
	if(float(playerStatsTouches[names][4]) > 15):
		while(j < 17):
			stats.append(playerStatsTouches[names][j])
			j = j + 1
		statsMin[names] = stats
		
total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][4])
	count += 1

AVGmin = total/count
print("Average Minutes: " + str(AVGmin))

total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][5])
	count += 1

AVGpoints = total/count
print("Average Points: "+ str(AVGpoints))

for names in statsMin:
	total += float(playerStatsTouches[names][6])
	count += 1

AVGtouch = total/count
print("Average Touches: "+ str(AVGtouch))

total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][7])
	count += 1

AVGfrontTouch = total/count
print("Average Front Court Touches: "+ str(AVGfrontTouch))

total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][8])
	count += 1

AVGpossTime = total/count
print("Average Possessions Time: "+ str(AVGpossTime))

total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][9])
	count += 1

AVGsecTouch = total/count
print("Average Seconds per touch: "+ str(AVGsecTouch))

total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][10])
	count += 1

AVGsecDrib = total/count
print("Average Seconds of Dribble: "+ str(AVGsecDrib))

total = 0
count = 0

for names in statsMin:
	total += float(playerStatsTouches[names][11])
	count += 1

AVGptsTouch = total/count
print("Average Points per Touch: "+ str(AVGptsTouch))
