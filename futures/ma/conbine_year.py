# -*- coding: UTF-8 -*-
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir+'/..')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
import contract

def main():
    month = input("please input month 01 ~ 12:  ");
    cs = {
        "ma14"+month:"gray",
        "ma15"+month:"pink",
        "ma16"+month:"green",
        "ma17"+month:"brown",
        "ma18"+month:"blue",
        "ma19"+month:"red",
        "ma20"+month:"black",
		"ma21"+month:"orange"
    }
    datas = contract.load()
    m = contract.filter(datas,cs,True)
    plt.xlabel("jdxx"+month)
    plt.ylabel("")
    ls = []
    
    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    #X轴的间隔为天
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    y_major_locator=MultipleLocator(200)
    ax.yaxis.set_major_locator(y_major_locator)


    for c in cs:
        if c not in m:
            continue
        d = m[c]
        ls.append(c)
        plt.plot(d["x"],d["y"],color=cs[c],linestyle='-',linewidth = 1,label=c)
    plt.legend(labels = ls,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.show()

main()