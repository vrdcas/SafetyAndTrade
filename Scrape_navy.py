# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:40:14 2020

@author: rabel005
"""

from __future__ import division
import pandas as pd
import argparse
import requests
import json
from requests import get
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import urllib

pages = range(1,16)

date_name = []
url_img = []

for page in pages:
    
    url = 'https://news.usni.org/category/fleet-tracker/page/{}'.format(page)
    
    r = requests.get(url)
    page_source = r.text
    
    soup = BeautifulSoup(page_source,'html.parser')
    
    pic_tags = soup.find_all('img', {'class': 'usninews_post_image'})
    
    for pic in pic_tags:
        pic_datename = pic['alt']
        print(pic_datename)
        pic_url = pic['src']
        print(pic_url)
        
        urllib.urlretrieve('{}'.format(pic_url), '{}.jpg'.format(pic_datename))
        
        date_name.append(pic_datename)
        url_img.append(pic_url)
        
                
test_df = pd.DataFrame({'date_name': date_name, 'url_img': url_img})
    
test_df.to_csv('H:/Ships/Navy_dates.csv', index=False, encoding='utf-8')
        

        
        
        
    
    

