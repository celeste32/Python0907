# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:15:28 2021

@author: USER
"""

import requests #透過上網尋找函式庫
import json
url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
data = requests.get(url).text
bike = json.loads(data)
print(bike[1])
for row in bike:
    #print(row)
    print('車站：',row['StationName'])
    print('車輛數字：',row['Capacity'])
    print('可借：',row['AvaliableBikeCount'])
    print('可停：',row['AvaliableSpaceCount'])
    print('區域：',row['District'])
    print("--------")
    