# -*- coding: utf-8 -*
from lxml import etree
import xml.etree.ElementTree as ET
import urllib.request
import time
import datetime
import xlwt
from asq.initiators import query

def getHtml(url):
    html = urllib.request.urlopen(url).read() 
    return html

data = list() 
urls = ['http://219.140.69.151/opac/newbookpub?page={}'.format(str(i)) for i in range(1,10)]
for url in urls:
    html = getHtml(url)

    tree =etree.HTML(html)
    #heads =tree.xpath('//table/tr/th/text()') 
    rows =tree.xpath('//table/tr')

    for row in rows:
      #data.append([c.text for c in row.getchildren()])
      #data.append([c.text for c in row.getchildren()])
      strs=(etree.tostring(row.getchildren()[0].xpath('//td/a')[0],encoding = "UTF-8").decode('utf-8'))
      #print(strs)
      #print(row.getchildren()[1].text.replace('\t','').replace('\r\n',''))
      #print(row.getchildren()[2].text.replace('\t','').replace('\r\n',''))
      #print(row.getchildren()[3].text.replace('\t','').replace('\r\n',''))
      data.append([strs,row.getchildren()[1].text.replace('\t','').replace('\r\n',''),row.getchildren()[2].text.replace('\t','').replace('\r\n',''),row.getchildren()[3].text.replace('\t','').replace('\r\n','')])
    time.sleep(1)
for row in data: print(row)
print(len(data))
