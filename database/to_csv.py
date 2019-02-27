#-*- coding:utf8 -*-
import json
 
f_sha = open('sha.json','rb')
f_sza = open('sza.json','rb')
d_sha = str(f_sha.read(),encoding='utf-8')
d_sza = str(f_sza.read(),encoding='utf-8')
f_sha.close()
f_sza.close()

j_sha = json.loads(d_sha)
j_sza = json.loads(d_sha)

f = open('list.csv','w',encoding='utf-8')

# 给csv文件写入表头
f.write(','.join(j_sha['column']) + '\n')

for item in j_sha['data']:
    item = [str(i) for i in item]
    f.write(','.join(item) + '\n')

for item in j_sza['data']:
    item = [str(i) for i in item]
    f.write(','.join(item) + '\n')
 
f.close()

