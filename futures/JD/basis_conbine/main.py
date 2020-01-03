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
import egg_price
def main():
    cs = {"01":"red","05":"green","09":"blue"}

    datas = contract.load()
    m = contract.filter_month(datas,cs)
    plt.ylabel("")
    ls = []
    
    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y%m'))
    #X轴的间隔为天
    ax.xaxis.set_major_locator(mdates.MonthLocator())

    y_major_locator=MultipleLocator(200)
    ax.yaxis.set_major_locator(y_major_locator)

    date_2_price = {}

    for c in cs:
        if c not in m:
            continue
        d = m[c]
        ls.append(c)
        plt.plot(d["x"],d["y"],color=cs[c],linestyle='-',linewidth = 1,label="c")
        
        for i in d["x"]:
            if i in egg_price.date2price:
                date_2_price[i] = egg_price.date2price[i] 
    
    dates = sorted(date_2_price)
    prices = []
    for k in dates:
        prices.append(date_2_price[k])

    ls.append("price")
    plt.plot(dates,prices,color="black",linestyle='-',linewidth = 1,label="price")

    plt.legend(labels = ls,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.show()

main()