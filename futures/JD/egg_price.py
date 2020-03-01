# -*- coding: UTF-8 -*-
import csv
import datetime
import os

ppp = "close"

date_2_price = {}

def load():
    l = []
    csvs = []
    for home, dirs, files in os.walk("data/price/dayanglu"):
        for filename in files:
            if filename.endswith(".csv"):
                csvs.append(os.path.join(home, filename))

    for item in csvs:
        f = csv.reader(open(item,"r",encoding='utf-8'))
        first = True
        for line in f:
            if first:
                first = False
                continue
            s = str(line[0])
            ss = s.split("-")
            d = datetime.date(int(ss[0]),int(ss[1]),int(ss[2]))
            date_2_price[d] = int(float(line[1])*1000)
 
def getYearData(year):
    t = {}
    for (k,v) in date_2_price.items():
        if k.year == 2 and k.day == 29:
            continue
        if k.year == int(year):
            k = datetime.date(2020,k.month,k.day)
            t[k] = v
    dates = sorted(t)
    prices = []
    for k in dates:
        prices.append(t[k])
    return [dates,prices]
