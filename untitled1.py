# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:40:19 2021

@author: USER
"""

import requests #透過上網尋找函式庫
import json
url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'
data = requests.get(url).text
air = json.loads(data)
allitem = air['records']
for row in allitem:
    print('地點：',row['SiteName'],'',row['County'])
    print('PM2.5值：',row['PM2.5'])
    print('PM10值：',row['PM10'])
    print('AQI值：',row['AQI'])
    print('風速：',row['WindSpeed'])
    print('空氣品質：',row['Status'])
    print('－－－－－－－')