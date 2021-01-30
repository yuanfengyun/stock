#-*- coding:utf8 -*-
import json
import pymysql

db = pymysql.connect(host="127.0.0.1",user="root",password="password",database="stock" )

cursor = db.cursor()

def insert_mysql(item):
   id = item["symbol"]
   name = item["name"]
   cur_price = item["current"]
   ttm = item["pe_ttm"] or 1
   market_capital = item["market_capital"] or '0'
   sql = "insert into base( \
           id, name, cur_price, ttm, market_capital) \
          values('%s', '%s',  %s, %s, %s) on duplicate key update cur_price=%s, ttm=%s" % \
       (id, name, cur_price, ttm, market_capital,cur_price,ttm)
   try:
       cursor.execute(sql)
   except Exception as e:
       print(sql)
       print(e)

f = open('list.json','rb')
d_list = str(f.read(),encoding='utf-8')
f.close()

j_list = json.loads(d_list)

for item in j_list['data']['list']:
    insert_mysql(item)
db.commit()
db.close()
