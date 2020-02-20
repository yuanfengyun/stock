#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
import time
from dongfang import headers

url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery112407468156378518487_1554296869371&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOIATC&js=(%7Bdata%3A%5B(x)%5D%2CrecordsFiltered%3A(tot)%7D)&cmd=C._A&st=(ChangePercent)&sr=-1&p=1&ps=5000&_=1554296869372"

db = pymysql.connect("120.79.91.100","root","yungege_test","stock" )
cursor = db.cursor()

r = requests.get(url,headers=headers)
s = r.text
s = s[48:-23]
l = json.loads(s)
for v in l:
    values = v.split(",")
    for index,s in enumerate(values):
        if s[-1:] == "%":
            values[index] = s[:-1]
        if s=="-":
            values[index] = 0
    cur_price = values[3]
    percent = values[4]
    ttm = values[15]
    pb = values[16]
    market_capital = values[17]
    float_market_capital = values[18]
    id = values[1]
    if int(id) < 600000:
        id = "SZ" + id
    else:
        id = "SH" + id
    sql = "update base set cur_price=%s, percent = %s, ttm=%s, pb=%s,market_capital=%s, float_market_capital=%s  where id='%s'" % (cur_price,percent,ttm,pb,id,market_capital,float_market_capital)
    try:
        cursor.execute(sql)
    except BaseException as e:
        print(sql,e)

    volume = values[7]
    open = values[11]
    high = values[9]
    low = values[10]
    close = cur_price
    turnrate = values[15]
    dt = values[-2]
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)

    index = int(id[2:])
    index = (index % 20) + 1
    sql = "insert into daily_history_%d(id,volume,open,high,low,close,turnrate,percent,time,timestamp) values('%s','%s','%s','%s','%s','%s','%s','%s','%s',%d)" % (index,id,volume,open,high,low,close,turnrate,percent,dt,timestamp)
    try:
        cursor.execute(sql)
    except BaseException as e:
        print(sql,e)

db.commit()
db.close()

