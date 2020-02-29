# -*- coding: UTF-8 -*-
import os
import sys
import csv
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir+'/..')

from data import contract
import datetime

cs = ["15","16","18"]
#cs.append("14")
#cs.append("17")
cs.append("19")

datas = contract.load()

def gen_diff(year,month1,month2):
    year = "jd"+year
    name_list = []
    a = year + month1
    b = year + month2
    name_list.append(a)
    name_list.append(b)
    
    m = contract.filter1(datas,name_list,False)

    diff_x = []
    diff_y = []
    if a not in m or b not in m:
        return
    ma = m[a]
    mb = m[b]
    max = -10000
    min = 10000
    for (date,v) in ma.items():
        if date not in mb:
            continue
        diff = v - mb[date]
        if diff > max:
            max = diff
        if diff < min:
            min = diff
    return (max,min)

def get_cur_diff(a,b):
    a = "jd"+a
    b = "jd"+b
    name_list = [a,b]
    m = contract.filter1(datas,name_list,False)

    diff_x = []
    diff_y = []
    if a not in m or b not in m:
        return
    ma = m[a]
    mb = m[b]
    date_2_diff = {}
    max_date = datetime.date(2019,1,1)
    for (date,v) in ma.items():
        if date not in mb:
            continue
        diff = v - mb[date]
        date_2_diff[date] = diff
        if date > max_date:
            max_date = date
        
    return date_2_diff[max_date]

def main():
    pairs = ["01","02","03","04","05","06","07","08","09","10","11","12","01","02","03","04","05","06","07","08","09","10","11"]
    t = {}
    for i in range(0,12):
        for j in range(1,12):
            if i == j:
                continue;
            max = -10000
            min = 10000
            for year in cs:
                pp = gen_diff(year,pairs[i],pairs[j])
                if pp is not None:
                    if max < pp[0]:
                        max = pp[0]
                    if min > pp[1]:
                        min = pp[1]
            
            t[pairs[i]+"_"+pairs[j]] = (max,min)

    curs = ["2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2101","2102","2103","2104","2105","2106","2107","2108","2109","2110","2111","2112"]
    print("may be a chance:")
    for i in range(0,len(curs)):
        for j in range(i+1,len(curs)-i-1):
            if i >= j:
                continue;
            cur_diff = get_cur_diff(curs[i],curs[j])
            if cur_diff is None:
                continue
            k = str(curs[i][2:]+"_"+curs[j][2:])
            if k not in t:
                continue
            max_min = t[k]
            max = max_min[0]
            min = max_min[1]
            if cur_diff > min + (max - min)*0.8:
                print(k,"current: ",cur_diff,"\tmax: ",max,"\tmin: ",min)
            if cur_diff < min + (max - min)*0.2:
                print(k,"current: ",cur_diff,"\tmax: ",max,"\tmin: ",min)
            

main()