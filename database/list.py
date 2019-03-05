#-*- coding:utf8 -*-
import json
import pymysql

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )

cursor = db.cursor()

def insert_mysql(item):
   id = item[0]
   name = item[1]
   cur_price = item[2]
   ttm = item[12]
   if ttm is None:
       ttm = '0'
   high52w = item[13]
   low52w = item[14] or '0'
   market_capital = item[11] or '0'
   sql = "insert into base( \
           id, name, cur_price, high52w, low52w, ttm, market_capital) \
          values('%s', '%s',  %s, %s,  %s, %s, %s) on duplicate key update cur_price=%s, ttm=%s" % \
       (id, name, cur_price, high52w, low52w, ttm, market_capital,cur_price,ttm)
   try:
       cursor.execute(sql)
   except:
       print(sql)

f_sha = open('sha.json','rb')
f_sza = open('sza.json','rb')
d_sha = str(f_sha.read(),encoding='utf-8')
d_sza = str(f_sza.read(),encoding='utf-8')
f_sha.close()
f_sza.close()

j_sha = json.loads(d_sha)
j_sza = json.loads(d_sza)

f = open('list.csv','w',encoding='utf-8')

# 给csv文件写入表头
f.write(','.join(j_sha['column']) + '\n')

used = {}
for item in j_sha['data']:
    item = [str(i) for i in item]
    id = item[0]
    if id in used:
       continue
    used[id] = True
    f.write(','.join(item) + '\n')
    insert_mysql(item)

for item in j_sza['data']:
    item = [str(i) for i in item]
    id = item[0]
    if id in used:
       continue
    used[id] = True
    f.write(','.join(item) + '\n')
    insert_mysql(item)

db.commit()
db.close()
f.close()

