#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests

db = pymysql.connect(host="127.0.0.1",user="root",password="password",database="stock" )
cursor = db.cursor()

def get_base_info(id):
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'cookie': 's=e5156opgk7; xq_a_token=176b14b3953a7c8a2ae4e4fae4c848decc03a883; xq_r_token=2c9b0faa98159f39fa3f96606a9498edb9ddac60; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxMzQ0MzE3MSwiY3RtIjoxNjExOTg1MzQwNTk2LCJjaWQiOiJkOWQwbjRBWnVwIn0.A2gOuRIiW46_wC5QVMDezxSCVpcGLXvh0ex48g-bg-K4iSgLsA_wKefNZpJ8VQqpGbnLBGugMaxPUYghA-w035coAxhDh-J1ALwBvWsaGDUuJjrFgx4-SBmInKsUYVtpFRi3IYGXb6bII98ATcBKRsvasDk3AQJaSPvhCKI2MNWucUJ88fexEQzuu9lEyOH8eZFTDDLsW4oBylIR93Nb-G8J6TWn4R2S3CSPmGvsdk6qnqLbbJ60wesS8fjW4Zgad4UeXQ4tgK_5XSYAwtEcFIw5VFdMKwVHI2LYqIEAfvC2_ofASBHLTzX0ZxzDiCpV44bHIW4ADnwldOEvT3Fn_w; u=271611985343563; cookiesu=271611985343563; Hm_lvt_1db88642e346389874251b5a1eded6e3=1611985344; device_id=41380507a0c87b9e46e212648490b162; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1611985456'
        }
    url = "https://stock.xueqiu.com/v5/stock/f10/cn/company.json?symbol=" + id
    r = requests.get(url,headers=headers)
    data = r.json()
    print(data)
    t = data['data']['company']
    if t is None:
        return
    orgtype = t['classi_name']
    bizscope = t['operating_scope']
    majorbiz = t['main_operation_business']
    compname = t['org_name_cn']
    province = t['provincial_name']
    city = '' 
    industry = ''
    sql = "update base set orgtype='%s',bizscope='%s',majorbiz='%s',compname='%s',province='%s',city='%s',industry='%s' where id='%s'" % \
       (orgtype, bizscope, majorbiz, compname, province, city,industry, id)
    try:
       cursor.execute(sql)
    except:
       print(sql)

cursor.execute("select id from base;")
results = cursor.fetchall()
for row in results:
    get_base_info(row[0])

db.commit()
db.close()

