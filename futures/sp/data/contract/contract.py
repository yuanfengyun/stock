#-*- coding: UTF-8 -*
from urllib import request
import json
import os
import csv

#获取每一页数据
def get_result_page(url):
    header = {'Accept-Charset': 'UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'clientType': 'web',
            'clientVersion': '0.1.0',
#            'Cookie': 'JSESSIONID=2032D8E562F3C8A84C72E5FA286541EC',
            'Host': 'stock2.finance.sina.com.cn',
            'User-Agent ': 'Mozilla/5.0 (Windows NT 10.0;WOW64;rv:61.0) Gecko/20100101 Firefox/61.0'}
    data = None
    rq = request.Request(url, data = data,headers = {})
    res = request.urlopen(rq);
    respoen = res.read();

    result = str(respoen,encoding = "utf-8")
    js = json.loads(result)
    
    return js

#获取请求结果
def get_contract(contract):
    url = "http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=" + contract
    js = get_result_page(url)
    if js is None:
        return

    out = open("./"+contract+".csv",'w+', newline='')
    csv_writer = csv.writer(out, dialect = "excel")
    csv_writer.writerow(["date","open","high","low","close","vol"])
    
    for row in js:
        date = str(row[0]).split("-")
        if contract[2:4] != date[0][2:4] and int(contract[4:6]) == int(date[1]):
            continue
        csv_writer.writerow(row)

years = [20,21]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
       
for year in years:
    for month in months:
        contract = "SP"+str(year)+month
        try:
            get_contract(contract)
        except:
            print("get contract error: "+contract)
        