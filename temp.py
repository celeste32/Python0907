# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests #透過上網尋找函式庫
import json
url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
data = requests.get(url).text
print(data)

url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
lccnet = 'https://www.lccnet.com.tw/lccnet'
data = requests.get(lccnet).text
print(data)

url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
data = requests.get(url).text
bike = json.loads(data)
print(bike[1])
for row in bike:
    print(row)