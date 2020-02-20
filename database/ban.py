#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests

db = pymysql.connect("120.79.91.100","root","yungege_test","stock" )
cursor = db.cursor()
headers = {
"Host": "stock.xueqiu.com",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Sec-Fetch-User": "?1",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
"Cookie": "xq_a_token=b2f87b997a1558e1023f18af36cab23af8d202ea; xqat=b2f87b997a1558e1023f18af36cab23af8d202ea; xq_r_token=823123c3118be244b35589176a5974c844687d5e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4MzE0MzIwMCwiY3RtIjoxNTgxMTM4ODA3OTAwLCJjaWQiOiJkOWQwbjRBWnVwIn0.ghV96QWaM4rKHCtvUy5JnM1qN1XOsB3omVO0he0MS4OZKn5kRu8l6de_eg4bOkrC57b3qxlUjyDV_KEEGIFxKVsT_h85EiNmbqqv9DZwNwpTAAOKs-L_kVZ4umIyeKszR_BG_WbgPUF4dq_jPiQ2NO1Yk5RPpGfMkBU5crwscsyBlsn9uI5l402rA1xfXg3mMyZua5Dkg9l0XZRVVrV6buSSZ5bH0ymhXYvonvDumwJwoAgkxG9bIPoEaYbNzO5LMHqlHsiTPuzyx0Z2wfbQwN1ANEP2sE9VXyrqbFs7Sa_NEBJtuFDiusIVlOdZf-kfITbRF-O88h-LoJ2umWWiOw; u=261581138822423; cookiesu=341581138823559; Hm_lvt_1db88642e346389874251b5a1eded6e3=1581138825; device_id=24700f9f1986800ab4fcc880530dd0ed; s=by13pvwo0e; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1581144460"
}

def get_info(id):
    url = "https://stock.xueqiu.com/v5/stock/f10/cn/shareschg.json?extend=true&type=restricts&page=1&size=10000&symbol="+id
    r = requests.get(url,headers=headers)
    data = r.json()
    l = data['data']['items']
    for v in l:
        holder_name = v['holder_name']
        floataable_time = v['floatable_time']
        floatable_shares_num = v['floatable_shares_num']
        float_shares_type=v['float_shares_type']
        sql = "insert into ban values('%s','%s','%s',%f,'%s');" % (id,holder_name,floataable_time,floatable_shares_num,float_shares_type)
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

