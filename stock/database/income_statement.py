#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
from xueqiu import headers

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_info(id):
    url = "https://xueqiu.com/stock/f10/incstatement.json?symbol="+id
    r = requests.get(url,headers=headers)
    data = r.json()
    l = data['list']
    fields = [
            'begindate',
            'enddate',
            'biztotinco',
            'biztotcost',
            'biztax',
            'salesexpe',
            'manaexpe',
            'finexpe',
            'asseimpaloss',
            'valuechgloss',
            'inveinco',
            'assoinveprof',
            'perprofit',
            'nonoreve',
            'nonoexpe',
            'totprofit',
            'incotaxexpe',
            'netprofit',
            'parenetp',
            'minysharrigh',
            'basiceps',
            'dilutedeps',
            'othercompinco',
            'parecompinco',
            'compincoamt',
            'parecompincoamt',
            'minysharincoamt'
    ]
    for v in l:
        values = []
        for field in fields:
            value = 0
            if field in v:
                value = v[field]
            if value is None:
                value = 0
            values.append(value)
        sql = "insert into income_statement(id,%s) values('%s',%s);" % (','.join(fields),id,','.join(str(i) for i in values))
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

