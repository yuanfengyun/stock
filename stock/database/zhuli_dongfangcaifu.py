#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
from dongfang import headers

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_info(id):
    zone="1"
    if id[:2]=="sz":
        zone="2"
    url = "http://ff.eastmoney.com//EM_CapitalFlowInterface/api/js?type=hff&rtntype=2&js=({data:[(x)]})&cb=var%20aff_data=&check=TMLBMSPROCR&acces_token=1942f5da9b46b069953c873404aad4b5&id="+id[2:]+zone+"&_=1553102917623"
    try:
        r = requests.get(url,headers=headers)
        s = r.text
        s = s[21:-3]
        l = json.loads(s)
        for v in l:
            values = v.split(",")
            for index,s in enumerate(values):
                if s[-1:] == "%":
                    values[index] = s[:-1]
            sql = "insert into zhuli_dongfang values('%s',%s);" % (id,','.join("'"+str(i)+"'" for i in values))
            try:
                cursor.execute(sql)
            except BaseException as e:
                print(sql,e)
    except BaseException as e:
        print(url,e)

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

