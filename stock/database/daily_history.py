#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
from xueqiu import headers

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_info(id):
    url = "https://xueqiu.com/stock/forchartk/stocklist.json?period=1&type=normal&symbol="+id
    r = requests.get(url,headers=headers)
    data = r.json()
    l = data['chartlist']
    fields = [
        "volume",
        "open",
        "high",
        "close",        
        "low",          
        "chg",          
        "percent",      
        "turnrate",     
        "ma5",
        "ma10",
        "ma20",         
        "ma30",         
        "dif",
        "dea",          
        "macd",         
        "lot_volume",   
    ]
    index = int(id[2:])
    index = (index % 20) + 1
    print(id,index)
    for v in l:
        values = []
        for field in fields:
            value = 0
            if field in v:
                value = v[field]
            if value is None:
                value = 0
            values.append(value)
        timestamp = v['timestamp']
        sql = "insert into daily_history_%d(id,%s,timestamp) values('%s',%s,'%s');" % (index,','.join(fields),id,','.join(str(i) for i in values),timestamp)
        try:
            cursor.execute(sql)
        except BaseException as e:
            print(sql,e)

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

