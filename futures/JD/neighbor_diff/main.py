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

def main():
    year = input("please input year:  ");

    cs = [
        ["jd"+year+"01","jd"+year+"02","pink"],
        ["jd"+year+"04","jd"+year+"05","green"],
        ["jd"+year+"07","jd"+year+"08","black"],
        ["jd"+year+"08","jd"+year+"09","blue"],
        ["jd"+year+"09","jd"+year+"10","red"]
    ]

    l = []
    name_list = []
    for i, val in enumerate(cs):
        l.append([val[0],val[1],val[0]+"-"+val[1]])
        name_list.append(val[0])
        name_list.append(val[1])
    
    datas = contract.load()
    m = contract.filter1(datas,name_list,False)
    print(len(m))

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
            diff_x.append(datetime.date(date.year,date.month,date.day))
                

        diff_l.append([pair[2],diff_x,diff_y])
        
    plt.ylabel("")
    ls = []
    labels = []
    for i,v in enumerate(diff_l):
        plt.plot(v[1],v[2],color=cs[i][2],linestyle='-',linewidth = 1,label=v[0])
        labels.append(v[0])
    
    plt.legend(labels = labels,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.show()

main()