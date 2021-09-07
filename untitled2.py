# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:55:35 2021

@author: USER
"""

import requests
import xml.sax #sax為解析xml的方式
class BikeHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.station = ''
        self.rent = ''
        self.space = ''
    
    #開始(物件,名字,屬性):
    def startElement(self, name, attrs):
        self.tag = name
    #結束(物件,名字):
    def endElement(self, name):
        if self.tag == "StationName":
            print("站名：",self.station)
        elif self.tag == "AvaliableBikeCount":
            print("可借：",self.rent)
        elif self.tag == "AvaliableSpaceCount":
            print("可停：",self.space)
        
    #定義物件內容
    def characters(self, content):
        if self.tag == "StationName":
            self.station = content
        elif self.tag == "AvaliableBikeCount":
            self.rent = content
        elif self.tag == "AvaliableSpaceCount":
            self.space = content
if __name__ == "__main__":
    parser = xml.sax.make_parser()
    bike = BikeHandler()
    parser.setContentHandler(bike)
    url = "http://tbike-data.tainan.gov.tw/Service/StationStatus/Xml"

data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
fileName = "bike.xml"
with open(fileName,"w",encoding="UTF-8") as fobj:
    fobj.write(data)
parser.parse(fileName)
        