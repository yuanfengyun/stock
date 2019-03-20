# coding:utf-8

import urllib
import requests

headers = {
    'Host': 'index.baidu.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Cookies': 'a=1'
}

#province_code = PROVINCE_CODE
#city_code = CITY_CODE
#cls.province_code/cls.city_code

params = {
    "keywords":"apple",
    "start_date":"2019-01-01",
    "end_date":"2019-01-02",
    "area":"001"
}

query_string = urllib.parse.urlencode(params)
url = "http://index.baidu.com/api/SearchApi/index?" + query_string
r = requests.get(url,headers=headers)
data = r.json()
print(data)

