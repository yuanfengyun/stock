# -*- coding: utf-8 -*
from lxml import etree
import xml.etree.ElementTree as ET
import urllib.request
import time
import datetime
import xlwt
import csv
import sys
from asq.initiators import query

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

prices = []
dates = []

data = list()
urls = ['http://www.1nongjing.com/plus/market.php?tid=33&product_category=1501&product_category_top=1500&product_category_son=1501&starttime=2015-01-01&endtime=2019-12-19&keyword=%E5%A4%A7%E6%B4%8B%E8%B7%AF&TotalResult=696&PageNo={}'.format(str(i)) for i in range(1,51)]
for url in urls:
    html = getHtml(url)

    tree =etree.HTML(html)
    ps =tree.xpath('//html/body/div/div/div/div/div[@class="ft3"]/ul/li[2]/text()')
    ds =tree.xpath('//html/body/div/div/div/div/div[@class="ft3"]/ul/li[5]/text()')
    prices += ps
    dates += ds
    time.sleep(0.1)

used = {}
out = open("./dayanglu.csv",'w+', newline='')
csv_writer = csv.writer(out, dialect = "excel")
csv_writer.writerow(["date","price"])
print(prices)

for i in range(1,len(prices)):
    if dates[i] not in used:
        row = [dates[i],prices[i]]
        csv_writer.writerow(row)
        used[dates[i]] = True




