# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import contract
import config

def gen_pic(month):
    cs = {}
    for (k,v) in config.YearToColor.items():
        cs[config.Name + k + month] = v

    datas = contract.load()
    m = contract.filter(datas,cs,True)
    plt.figure(figsize=(20, 10))
    plt.xlabel("jdxx"+month)
    plt.ylabel("")
    ls = []
    
    ax = plt.gca()
    #指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    #X轴的间隔为天
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    y_major_locator=MultipleLocator(100)
    ax.yaxis.set_major_locator(y_major_locator)


    for c in cs:
        if c not in m:
            continue
        d = m[c]
        ls.append(c)
        linewidth = 1
        if c[0:4] == "JD20":
            linewidth = 2
        plt.plot(d["x"],d["y"],color=cs[c],linestyle='-',linewidth = linewidth,label=c)
    plt.legend(labels = ls,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.savefig("pictures/jdxx0x/"+month+".png")
    plt.clf()

def main():
    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    for month in months:
        gen_pic(month)

main()