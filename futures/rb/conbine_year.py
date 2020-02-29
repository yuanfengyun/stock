# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
import contract
import config

def main():
    month = input("please input month 01 ~ 12:  ");
    cs = {}
    for (k,v) in config.YearToColor.items():
        cs[config.Name + k + month] = v

    datas = contract.load()
    m = contract.filter(datas,cs,True)
    plt.xlabel(config.Name + "xx"+month)
    plt.ylabel("")
    ls = []
    
    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    #X轴的间隔为天
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    y_major_locator=MultipleLocator(config.y_major_locator)
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