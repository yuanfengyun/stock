# -*- coding: UTF-8 -*-
import os
import sys
import csv
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir+'/..')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
from data import contract
import datetime

cs = [
    "jd14",
    "jd15",
    "jd16",
    "jd17",
    "jd18",
    "jd19",
    "jd20",
    "jd21"
]

datas = contract.load()

def gen_diff(year,month1,month2):
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

def main():
    pairs = ["01","02","03","04","05","06","07","08","09","10","11","12","01","02","03","04","05","06","07","08","09","10","11"]
    t = []
    
    title = ["year"]
    for year in cs:
        title.append(year[2:] + "_max")
        title.append(year[2:] + "_min")
    title.append("max")
    title.append("min")
        
    
    t.append(title)
    
    for i in range(0,12):
        for j in range(1,12):
            if i == j:
                continue;
            record = [pairs[i]+"_"+pairs[j]]
            max = -10000
            min = 10000
            for year in cs:
                pp = gen_diff(year,pairs[i],pairs[j])
                if pp is None:
                    record.append("")
                    record.append("")
                else:
                    record.append(pp[0])
                    record.append(pp[1])
                    if max < pp[0]:
                        max = pp[0]
                    if min > pp[1]:
                        min = pp[1]
            
            record.append(max)
            record.append(min)            
            t.append(record)
    print(t)
    
    out = open("./data/diff.csv",'w+', newline='')
    csv_writer = csv.writer(out, dialect = "excel")
    
    for row in t:
        csv_writer.writerow(row)

main()