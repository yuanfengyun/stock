#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
from xueqiu import headers

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_info(id):
    url = "https://stock.xueqiu.com/v5/stock/realtime/quotec.json?symbol=" + id
    r = requests.get(url,headers=headers)
    data = r.json()
    t = data['data'][0]
    cur_price = t['current']
    percent = t['percent']
    market_capital = t['market_capital']
    float_market_capital = t['float_market_capital']

    sql = "update base set cur_price=%s,percent=%s,market_capital=%s,float_market_capital=%s where id='%s'" % \
       (cur_price,percent,market_capital,float_market_capital, id)
    
    #cursor.execute(sql)
    try:
       cursor.execute(sql)
    except:
       print(sql)

with open('list.csv','r',encoding='utf-8') as csvfile:
    read = csv.reader(csvfile)
    title = True
    for v in read:
        if title:
            title = False
            continue
        id = v[0]
        get_info(id)

db.commit()
db.close()

