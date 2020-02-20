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
    year = input("please input year: ");
    cs = {
        "jd" + year + "01":"blue",
        "jd" + year + "02":"pink",
        "jd" + year + "03":"pink",
        "jd" + year + "04":"brown",
        "jd" + year + "05":"green",
        "jd" + year + "06":"indigo",
        "jd" + year + "07":"plum",
        "jd" + year + "08":"purple",
        "jd" + year + "09":"red",
        "jd" + year + "10":"magenta",
        "jd" + year + "11":"gray",
        "jd" + year + "12":"teal"
    }
    datas = contract.load()
    m = contract.filter(datas,cs,False)
    plt.xlabel("jd20"+year)
    plt.ylabel("")
    ls = []
    
    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
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
        plt.plot(d["x"],d["y"],color=cs[c],linestyle='-',linewidth = 1,label=c)
        
        for i in d["x"]:
            if i in egg_price.date2price:
                date_2_price[i] = egg_price.date2price[i] 
    
    dates = sorted(date_2_price)
    prices = []
    for k in dates:
        prices.append(date_2_price[k])
    ls.append("dayanglu egg price")
    plt.plot(dates,prices,color="black",linestyle='-',linewidth = 1,label="大洋路价格")

    plt.legend(labels = ls,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.show()

main()