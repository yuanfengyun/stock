#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
from xueqiu import headers

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_info(id):
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_qsfx_zjlrqs?page=1&num=30&sort=opendate&asc=0&daima="+id
    r = requests.get(url)
    s = r.text
    fields = [
        "opendate",
        "trade",
        "changeratio",
        "turnover",
        "netamount",
        "ratioamount",
        "r0_net",
        "r0_ratio",
        "r0x_ratio",
        "cnt_r0x_ratio",
        "cate_ra",
        "cate_na"
    ]
    s = s.replace("cnt_r0x_ratio","aabbccdd")
    for f in fields:
        s = s.replace(f,"\""+f+"\"")
    s = s.replace("aabbccdd","\"cnt_r0x_ratio\"")
    l = json.loads(s)
    for v in l:
        values = []
        for field in fields:
            value = 0
            if field in v:
                value = v[field]
            if value is None:
                value = 0
            values.append(value)
        sql = "insert into zhuli(id,%s) values('%s',%s);" % (','.join(fields),id,','.join("'"+str(i)+"'" for i in values))
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

