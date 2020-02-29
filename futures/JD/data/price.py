# -*- coding: UTF-8 -*-
import csv
import datetime
import os

date2price = {}

def load():
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
            d = str(line[0])
            p = int(float(line[1])*1000.0)
            d = datetime.date(int(d[0:4]),int(d[5:7]),int(d[8:]))
            date2price[d] = p

load()

def getYearData(year,one,yinli):
    date_2_price = {}

    for (k,v) in date2price.items():
        if k.year == int(year):
            if yinli:
                day = ZhDate.from_datetime(k)
                if day.lunar_month == 2 and day.lunar_day >= 29:
                    continue
                k = datetime.date(day.lunar_year,day.lunar_month,day.lunar_day)
            if not one:
                k = datetime.date(2020,k.month,k.day)
            date_2_price[k] = v
    dates = sorted(date_2_price)
    prices = []
    for k in dates:
        prices.append(date_2_price[k])
    return [dates,prices]