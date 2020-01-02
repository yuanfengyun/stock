# -*- coding: UTF-8 -*-

import csv
import datetime

# "合约","日期","前收盘价","前结算价","开盘价","最高价","最低价","收盘价","结算价","成交量","持仓量"

cfg = [
    ["data\\2014.csv",[1,2,3,4,5,6,7,8,9,12,14]],
    ["data\\2015.csv",[1,2,3,4,5,6,7,8,9,12,14]],
    ["data\\2016.csv",[1,2,3,4,5,6,7,8,9,12,14]],
    ["data\\2017.csv",[1,2,3,4,5,6,7,8,9,12,14]],
    ["data\\2018.csv",[2,3,4,5,6,7,8,9,10,13,15]],
]

def load():
    l = []
    for item in cfg:
        f = csv.reader(open(item[0],"r",encoding='utf-8'))
        first = True
        for line in f:
            if first:
                first = False
                continue
            indextab = item[1]
            l.append({
                "name":line[indextab[0]],
                "date":line[indextab[1]],
                "pre_close":int(float(line[indextab[2]])),
                "pre_avg":int(float(line[indextab[3]])),
                "open":int(float(line[indextab[4]])),
                "high":int(float(line[indextab[5]])),
                "low":int(float(line[indextab[6]])),
                "close":int(float(line[indextab[7]])),
                "avg":int(float(line[indextab[8]])),
                "cloumn":int(float(line[indextab[9]])),
                "total":int(float(line[indextab[10]])),
            })
    return l

def filter(l,months):
    ret = {}
    for item in l:
        month = item["name"][4:6]
        if month not in months:
            continue
        if item["date"][4:]=="0229":
            continue

        x=datetime.date(int("20"+item["date"][2:4]),int(item["date"][4:6]),int(item["date"][6:]))
        y = item["avg"]
        if month not in ret:
            records = {"x":[x],"y":[y]}
            ret[month] = records
            continue
        records = ret[month]
        records["x"].append(x)
        records["y"].append(y)
    return ret
        
    
    