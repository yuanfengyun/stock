# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import numpy
import contract as contract_hc
import contract_rb
import datetime
import config

def main():
    month = input("please input month1 01 ~ 12:  ");

    l = []
    name_list_hc = []
    name_list_rb = []
    for (k, v) in config.YearToColor.items():
        a = "HC" + k + month
        b = "RB" + k + month
        l.append([a,b,a+" - "+b,v])
        name_list_hc.append(a)
        name_list_rb.append(b)

    datas_hc = contract_hc.load()
    datas_rb = contract_rb.load()

    m_hc = contract_hc.filter1(datas_hc,name_list_hc,False)
    m_rb = contract_rb.filter1(datas_rb,name_list_rb,False)

    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    y_major_locator=MultipleLocator(config.y_diff_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

    diff_l = []
    for pair in l:
        diff_x = []
        diff_y = []
        if pair[0] not in m_hc or pair[1] not in m_rb:
            continue
        ma = m_hc[pair[0]]
        mb = m_rb[pair[1]]
        year = int("20"+pair[0][2:4])
        for (date,v) in ma.items():
            if date not in mb:
                continue
            diff_y.append(v - mb[date])
            diff_x.append(datetime.date(2019 + date.year - year,date.month,date.day))
                

        diff_l.append([pair[2],diff_x,diff_y,pair[3]])
        
    plt.xlabel(" price diff " + month)
    plt.ylabel("")
    ls = []
    labels = []
    for i,v in enumerate(diff_l):
        plt.plot(v[1],v[2],color=v[3],linestyle='-',linewidth = 1,label=v[0])
        labels.append(v[0])
    
    plt.legend(labels = labels,loc = 'best',shadow = True)
    plt.grid(axis="y",linestyle="--")
    plt.show()

main()