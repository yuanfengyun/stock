#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests
import time
from dongfang import headers

url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=ct&st=(BalFlowMain)&sr=-1&p=1&ps=5000&js=var%20BrZrpKmQ={pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=51810169"

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

r = requests.get(url,headers=headers)
s = r.text
s = s[45:-1]
print(s[0:100])
print(s[-100:])
l = json.loads(s)
for v in l:
    values = v.split(",")
    for index,s in enumerate(values):
        if s[-1:] == "%":
            values[index] = s[:-1]
        if s=="-":
            values[index] = 0
    id = values[1]
    if int(id) < 600000:
        id = "SZ" + id
    else:
        id = "SH" + id

    sql = "insert into zhuli_dongfang values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (id,values[2],values[-2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14])
    try:
        cursor.execute(sql)
    except BaseException as e:
        print(sql,e)

db.commit()
db.close()

