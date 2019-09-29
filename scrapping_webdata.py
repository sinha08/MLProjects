# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:14:48 2019

@author: ankur sinha
"""

#from bs4 import BeautifulSoup

#from selenium  import webdriver

#driver = webdriver.Chrome()
#driver.get('https://www.prokabaddi.com/teams/bengal-warriors-profile-4')
#soup = BeautifulSoup(driver.page_source)
#childrens = soup.findAll('div',attrs={'class':'si-stats-container'})
#print(childrens)

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.prokabaddi.com/teams/bengal-warriors-profile-4")
#more_buttons = driver.find_elements_by_class_name("si-tab si-profile-tabs")
#print(more_buttons)
#for x in range(len(more_buttons)):
#    if more_buttons[x].is_displayed():
#        driver.execute_script("arguments[0].click();", more_buttons[x])
#        time.sleep(1)
        
        
#elem = driver.find_element(by=By.SPAN,value ="stats").sendKeys(Keys.CONTROL + "t");
#elem.send_keys(Keys.TAB)

page_source = driver.page_source
soup = BeautifulSoup(page_source)

posa = []
review = soup.find_all('div', class_='si-stats-container')
rdata=review[0]
if rdata is not None:
    table = rdata.find_all("div","si-tbl-data")
    print(table)
    overall=list()
    print("##################################")
    #print(table)
    if len(table) > 0:
        for i in range(0,len(table)):
            pos = table[i].find_all('div', class_='si-data-block')
            print(pos)
            i = i+1
            for k in range(0,len(pos)):
                overall.append(pos[k].get_text())
    print(overall)
    headers = [overall[0]]+overall[25:33]
    fields = overall[1:25]
    O_o = overall[33:40]+overall[89:98]+overall[161:169]
    s7_o = overall[40:47]+overall[98:107]+overall[169:177]
    s6_o = overall[47:54]+overall[107:116]+overall[177:185]
    s5_o = overall[54:61]+overall[116:125]+overall[185:193]
    s4_o = overall[61:68]+overall[125:134]+overall[193:201]
    s3_o = overall[68:75]+overall[134:143]+overall[201:209]
    s2_o = overall[75:82]+overall[143:152]+overall[209:217]
    s1_o = overall[82:89]+overall[152:161]+overall[217:225]
        
    print(O_o)
    df = pd.DataFrame(list(zip(fields,O_o,s7_o,s6_o,s5_o,s4_o,s3_o,s2_o,s1_o)),columns=headers)
    df.to_csv("team_stats.csv")
    #if (posname is not E):
     #   posa.append(posname.strip())
#print(reviews_selector)