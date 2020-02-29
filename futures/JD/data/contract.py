# -*- coding: UTF-8 -*-
import csv
import datetime
import os

ppp = "close"

# "合约","日期","前收盘价","前结算价","开盘价","最高价","最低价","收盘价","结算价","成交量","持仓量"

def load():
    l = []
    csvs = []
    for home, dirs, files in os.walk("data/contract"):
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
            ii = {
                "name":str(item[-10:-4]).lower(),
                "date":str(line[0]),
                "open":int(float(line[1])),
                "high":int(float(line[2])),
                "low":int(float(line[3])),
                "close":int(float(line[4])),
                "cloumn":int(float(line[5]))
            }
            if ii["close"] == 0:
                ii["close"] = ii["low"]
            l.append(ii)
    return l

def filter(l,names,same_year):
    ret = {}
    for item in l:
        try:
            if item["name"] not in names:
                continue
            date = item["date"].split("-")
            if (date[1]=="2" or date[1]=="02") and date[2]=="29":
                continue
            year = int(date[0])
            if same_year:
                year = 2019 + int(date[0]) - int(item["name"][2:4])
            x=datetime.date(year,int(date[1]),int(date[2]))
            y = item[ppp]
            if item["name"] not in ret:
                records = {"x":[x],"y":[y]}
                ret[item["name"]] = records
                continue
            records = ret[item["name"]]
            records["x"].append(x)
            records["y"].append(y)
        except:
            pass
    return ret
    
def filter1(l,names,same_year):
    ret = {}
    for item in l:
        try:
            if item["name"] not in names:
                continue
            date = item["date"].split("-")
            if (date[1]=="2" or date[1]=="02" )and date[2]=="29":
                continue
            year = int(date[0])
            if same_year:
                year = 2019 + int(date[0][2:4]) - int(item["name"][2:4])
            x=datetime.date(year,int(date[1]),int(date[2]))
            y = item[ppp]
            if item["name"] not in ret:
                records = {x:y}
                ret[item["name"]] = records
                continue
            records = ret[item["name"]]
            records[x] = y
        except:
            pass
    return ret
    
def filter_month(l,months):
    ret = {}
    for item in l:
        try:
            month = item["name"][4:6]
            if month not in months:
                continue
            date = item["date"].split("-")
            if (date[1]=="2" or date[1]=="02" )and date[2]=="29":
                continue
            year = int(date[0])
            x=datetime.date(year,int(date[1]),int(date[2]))
            y = item[ppp]
            if month not in ret:
                records = {x:y}
                ret[month] = records
                continue
            records = ret[month]
            records[x] = y
        except:
            pass
    return ret

def filter_month(l,months):
    ret = {}
    for item in l:
        try:
            month = item["name"][4:6]
            if month not in months:
                continue
            date = item["date"].split("-")
            if (date[1]=="2" or date[1]=="02") and date[2]=="29":
                continue
            year = int(date[0])
            x=datetime.date(year,int(date[1]),int(date[2]))
            y = item[ppp]
            if month not in ret:
                records = {"x":[x],"y":[y]}
                ret[month] = records
                continue
            records = ret[month]
            records["x"].append(x)
            records["y"].append(y)
        except:
            pass
    return ret