import datetime
import csv
import math
import requests

url = "http://cif.mofcom.gov.cn/cif/seachlineNew.fhtml?commdityid=150010&enterid=3681&Bdate=2020-01-01&Edate=2022-12-31"

m = {"2020":[],"2021":[]}

print("get dayanglu egg price begin...")

requests = requests.get(url)
s = str(requests.content)
s = s[s.find("boundaryGap")+41:]
a = s[:s.find("]")+1]
a = a[3:-3]

s = s[s.find("]")+1:]
s = s[s.find("data")+5:]
b = s[:s.find("]")+1]
b = b[3:-3]
b = b.replace("    ","")
b = b.replace("   ","")

dates = a.split("\\',\\'")
prices = b.split("\\',\\'")

for i in range(len(dates)):
    date = dates[i]
    price = float(prices[i])/2.0
    l = m[date[0:4]]
    l.append([date,price,math.floor(price*44)])

for (k,v) in m.items():
    out = open("./dayanglu/"+k+".csv",'w+', newline='')
    csv_writer = csv.writer(out, dialect = "excel")
    csv_writer.writerow(["date","price","price"])

    for row in v:
        csv_writer.writerow(row)
