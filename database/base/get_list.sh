#!/bin/bash
echo "拉取上交所股票"

curl 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=8000&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1611985534199' \
	  -H 'Connection: keep-alive' \
	    -H 'Accept: */*' \
	      -H 'cache-control: no-cache' \
	        -H 'X-Requested-With: XMLHttpRequest' \
		  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36' \
		    -H 'Sec-Fetch-Site: same-origin' \
		      -H 'Sec-Fetch-Mode: cors' \
		        -H 'Sec-Fetch-Dest: empty' \
			  -H 'Referer: https://xueqiu.com/hq' \
			    -H 'Accept-Language: zh-CN,zh;q=0.9' \
			      -H 'Cookie: acw_tc=2760820316119852884877121ef84a93f1fb1cbc334a0b924b7b191596e154; s=e5156opgk7; xq_a_token=176b14b3953a7c8a2ae4e4fae4c848decc03a883; xq_r_token=2c9b0faa98159f39fa3f96606a9498edb9ddac60; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxMzQ0MzE3MSwiY3RtIjoxNjExOTg1MzQwNTk2LCJjaWQiOiJkOWQwbjRBWnVwIn0.A2gOuRIiW46_wC5QVMDezxSCVpcGLXvh0ex48g-bg-K4iSgLsA_wKefNZpJ8VQqpGbnLBGugMaxPUYghA-w035coAxhDh-J1ALwBvWsaGDUuJjrFgx4-SBmInKsUYVtpFRi3IYGXb6bII98ATcBKRsvasDk3AQJaSPvhCKI2MNWucUJ88fexEQzuu9lEyOH8eZFTDDLsW4oBylIR93Nb-G8J6TWn4R2S3CSPmGvsdk6qnqLbbJ60wesS8fjW4Zgad4UeXQ4tgK_5XSYAwtEcFIw5VFdMKwVHI2LYqIEAfvC2_ofASBHLTzX0ZxzDiCpV44bHIW4ADnwldOEvT3Fn_w; u=271611985343563; cookiesu=271611985343563; Hm_lvt_1db88642e346389874251b5a1eded6e3=1611985344; device_id=41380507a0c87b9e46e212648490b162; __utma=1.1777376993.1611985354.1611985354.1611985354.1; __utmc=1; __utmz=1.1611985354.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.3.10.1611985354; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1611985456' \
			        --compressed > list.json

