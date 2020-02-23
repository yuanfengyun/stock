# -*- coding: UTF-8 -*-
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir+'/..')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
from data import contract
import datetime

cs = [
    ["jd14","gray"],
    ["jd15","pink"],
    ["jd16","green"],
    ["jd17","brown"],
    ["jd18","blue"],
    ["jd19","red"],
    ["jd20","black"],
    ["jd21","yellow"]
]

datas = contract.load()


def gen_pic(prefix,month1,month2):
    l = []
    name_list = []
    for i, val in enumerate(cs):
        a = val[0] + month1
        b = val[0] + month2
        if month2 < month1:
            if i >= len(cs)-1:
                continue
            b = cs[i+1][0]+month2
        l.append([a,b,a+" - "+b])
        name_list.append(a)
        name_list.append(b)
    
    m = contract.filter1(datas,name_list,False)

    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    #X轴的间隔为小时
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    y_major_locator=MultipleLocator(100)
    ax.yaxis.set_major_locator(y_major_locator)

    diff_l = []
    for pair in l:
        diff_x = []
        diff_y = []
        if pair[0] not in m or pair[1] not in m:
            continue
        ma = m[pair[0]]
        mb = m[pair[1]]
        year = int("20"+pair[0][2:4])
        for (date,v) in ma.items():
            if date not in mb:
                continue
            diff_y.append(v - mb[date])
            diff_x.append(datetime.date(2019 + date.year - year,date.month,date.day))
                

        diff_l.append([pair[2],diff_x,diff_y])
        
    plt.xlabel("jd price diff " + month1 + " " + month2)
    plt.ylabel("")
    ls = []
    labels = []
    for i,v in enumerate(diff_l):
        plt.plot(v[1],v[2],color=cs[i][1],linestyle='-',linewidth = 1,label=v[0])
        labels.append(v[0])
    
    plt.legend(labels = labels,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.savefig("pictures/" +prefix+ "/" +month1+"_" +month2+".png")
    plt.clf()

def main():
    pairs = {
        "1_month_diff":[["01","02"],["02","03"],["03","04"],["04","05"],["05","06"],["06","07"],["07","08"],["08","09"],["09","10"],["10","11"],["11","12"],["12","01"]],
        "2_month_diff":[["01","03"],["02","04"],["03","05"],["04","06"],["05","07"],["06","08"],["07","09"],["08","10"],["09","11"],["10","12"],["11","01"],["12","02"]],
        "3_month_diff":[["01","04"],["02","05"],["03","06"],["04","07"],["05","08"],["06","09"],["07","10"],["08","11"],["09","12"],["10","01"],["11","02"],["12","03"]],
        "4_month_diff":[["01","05"],["02","06"],["03","07"],["04","08"],["05","09"],["06","10"],["07","11"],["08","12"],["09","01"],["10","02"],["11","03"],["12","04"]],
        "5_month_diff":[["01","06"],["02","07"],["03","08"],["04","09"],["05","10"],["06","11"],["07","12"],["08","01"],["09","02"],["10","03"],["11","04"],["12","05"]],
        "6_month_diff":[["01","07"],["02","08"],["03","09"],["04","10"],["05","11"],["06","12"],["07","01"],["08","02"],["09","03"],["10","04"],["11","05"],["12","06"]],
        "7_month_diff":[["01","08"],["02","09"],["03","10"],["04","11"],["05","12"],["06","01"],["07","02"],["08","03"],["09","04"],["10","05"],["11","06"],["12","07"]],
        "8_month_diff":[["01","09"],["02","10"],["03","11"],["04","12"],["05","01"],["06","02"],["07","03"],["08","04"],["09","05"],["10","06"],["11","07"],["12","08"]],
        "9_month_diff":[["01","10"],["02","11"],["03","12"],["04","01"],["05","02"],["06","03"],["07","04"],["08","05"],["09","06"],["10","07"],["11","08"],["12","09"]],
        "10_month_diff":[["01","11"],["02","12"],["03","01"],["04","02"],["05","03"],["06","04"],["07","05"],["08","06"],["09","07"],["10","08"],["11","09"],["12","10"]],
        "11_month_diff":[["01","12"],["02","01"],["03","02"],["04","03"],["05","04"],["06","05"],["07","06"],["08","07"],["09","08"],["10","09"],["11","10"],["12","11"]]
    }

    for (k,v) in pairs.items():
        print(k)
        for pair in v:
            gen_pic(k,pair[0],pair[1])

main()