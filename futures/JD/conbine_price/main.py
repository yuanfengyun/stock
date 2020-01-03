# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
import egg_price

def main():
    cs = {
        "2014":"brown",
        "2015":"green",
        "2016":"indigo",
        "2017":"plum",
        "2018":"blue",
        "2019":"red",
    }
    plt.xlabel("2014-2019")
    plt.ylabel("")
    ls = []
    
    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m.%d'))
    #X轴的间隔为天
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    y_major_locator=MultipleLocator(200)
    ax.yaxis.set_major_locator(y_major_locator)

    date_2_price = {}

    for c in cs:
        v = egg_price.getYearData(c,False,False)
        ls.append(c)
        plt.plot(v[0],v[1],color=cs[c],linestyle='-',linewidth = 1,label=c)

    plt.legend(labels = ls,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.show()

main()