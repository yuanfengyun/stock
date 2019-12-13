# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
import data

def main():
    month = input("please input month 01 ~ 12:  ");
    cs = {
        "jd14"+month:"gray",
        "jd15"+month:"pink",
        "jd16"+month:"green",
        "jd17"+month:"brown",
        "jd18"+month:"blue",
        "jd19"+month:"red"
    }
    datas = data.load()
    m = data.filter(datas,"160110","171110",cs)
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