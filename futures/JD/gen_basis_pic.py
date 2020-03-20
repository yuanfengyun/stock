# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
import contract
import config
import egg_price
def gen_pic(year):
    cs = {}
    for (k,v) in config.MonthToColor.items():
        cs[config.Name + year + k] = v

    datas = contract.load()
    m = contract.filter(datas,cs,False)
    plt.figure(figsize=(20, 10))
    plt.xlabel("jd20"+year)
    plt.ylabel("")
    ls = []

    plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
    plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False

    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    #X轴的间隔为天
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.yaxis.tick_left()

    
    y_major_locator=MultipleLocator(200)
    ax.yaxis.set_major_locator(y_major_locator)

    date_2_price = {}
    egg_price.load()
    for c in cs:
        if c not in m:
            continue
        d = m[c]
        ls.append(c)
        plt.plot(d["x"],d["y"],color=cs[c],linestyle='-',linewidth = 1,label=c)
        
        for i in d["x"]:
            if i in egg_price.date_2_price:
                date_2_price[i] = egg_price.date_2_price[i]
            else:
                print(i)
    
    dates = sorted(date_2_price)
    prices = []
    for k in dates:
        prices.append(date_2_price[k])
    ls.append("dayanglu egg price")
    plt.plot(dates,prices,color="black",linestyle='-',linewidth = 2,label="大洋路价格")

    plt.legend(labels = ls,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.savefig("pictures/basis/" +year+".png")
    plt.clf()

def main():
    years = ["14","15","16","17","18","19","20"]
    for year in years:
        gen_pic(year)

main()