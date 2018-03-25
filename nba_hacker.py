from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pandas import *

browser=webdriver.Chrome("~/Project_Utilities/chromedriver")
browser.get('http://on.nba.com/2k80aXM')
lmrl=browser.find_elements_by_class_name("table-addrows__button")

while (len(lmrl)!=0):
        loader=lmrl[0]
        loader.click()
        lmrl=browser.find_elements_by_class_name("table-addrows__button")




soup = BeautifulSoup(browser.page_source, "html.parser")
headers=soup.find("nba-stat-table").find("thead").find("tr").find_all("th")
count=0
imp_headers=[]
for th in headers:
    if th.text=="PLAYER":
        imp_headers.append("PLAYER")
    if th.text=="TEAM":
        imp_headers.append("TEAM")
    if th.text=="AGE":
        imp_headers.append("AGE")
    else:
        if (th.has_attr("data-dir")):
            imp_headers.append(th.text)

#print len(imp_headers)
total_data=[]
body=soup.find("nba-stat-table").find("tbody").find_all("tr")
for tr in body:
    tds=tr.find_all("td")
    data_temp=[]
    tds=tds[1:]
    #print tds[4]
    i=0
    for td in tds:
        data_points=[]
        #print td
        if (td['class']==["rank ng-binding"]):
            x=5
        else:
            data_temp.append(td.text)
            i=i+1

    total_data.append(data_temp)

browser.close()
indexer=range(len(total_data))
indexed=np.array(indexer)
indexed=indexed+1
df = pd.DataFrame(total_data, index=indexed, columns=imp_headers)
players=df['PLAYER'].values.tolist()
df.drop('PLAYER', axis=1, inplace=True)
df.index=players
print(df)

'''



'''
