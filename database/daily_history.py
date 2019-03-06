#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_info(id):
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            "Cookie":"_ga=GA1.2.1197435973.1551018842; device_id=dd71de99dc275bf78a8853c89326d074; s=ej11t4gzin; xq_a_token=d8474141c84f89dfd8192ed057589c907247ad25; xq_a_token.sig=qQxckS03yaBOAH2A-PRiZ6RoIrc; xq_r_token=43957cca9e5babf3d6e6bfba4e8bd87d54b2b2b4; xq_r_token.sig=gfDc5JwKlyApNHlEy59tOERQoKw; _gid=GA1.2.573513587.1551876202; u=361551876202307; Hm_lvt_1db88642e346389874251b5a1eded6e3=1551714746,1551717050,1551760335,1551876202; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1551876202"}
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

