#-*- coding:utf8 -*-
import json
import pymysql
import csv
import requests

db = pymysql.connect("127.0.0.1","root","yungege_test","stock" )
cursor = db.cursor()

def get_base_info(id):
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie':'_ga=GA1.2.1197435973.1551018842; device_id=dd71de99dc275bf78a8853c89326d074; s=ej11t4gzin; __utmz=1.1551274405.2.2.utmcsr=baidu^|utmccn=(organic)^|utmcmd=organic; __utma=1.1197435973.1551018842.1551274405.1551277586.3; aliyungf_tc=AQAAAC6LV1Ib9gsAfPB9oxu4kXS59SL7; xq_a_token=61cf65fe948cf0150ca509827bc6b51cf05ba804; xq_a_token.sig=ufZ8whxoJpWVsUYRYZxo3pFQaIo; xq_r_token=0c1b70c3d72bc88edbfecac3f410070abc494bcc; xq_r_token.sig=L4cf7YTvzZCuyi75EMFM4bFhidg; _gid=GA1.2.2113169162.1551714746; Hm_lvt_1db88642e346389874251b5a1eded6e3=1551276840,1551277567,1551277580,1551714746; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1551714746; u=401551714747460'
    }
    url = "https://stock.xueqiu.com/v5/stock/realtime/quote.json?symbol=" + id
    r = requests.get(url,headers=headers)
    data = r.json()
    t = data['data']['quote']
    cur_price = t['current']
    percent = t['percent']
    market_capital = t['market_capital']
    float_market_capital = t['float_market_capital']

    sql = "update base set cur_price=%s,market_capital=%s,float_market_capital=%s where id='%s'" % \
       (cur_price,market_capital,float_market_capital, id)
    
    #cursor.execute(sql)
    try:
       cursor.execute(sql)
    except:
       print(sql)

with open('list.csv','r',encoding='utf-8') as csvfile:
    read = csv.reader(csvfile)
    title = True
    for v in read:
        if title:
            title = False
            continue
        id = v[0]
        get_base_info(id)

db.commit()
db.close()

