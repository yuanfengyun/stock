# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import numpy
import data
import datetime

def main():
    month1 = input("please input month1 01 ~ 12:  ");
    month2 = input("please input month2 01 ~ 12:  ");

    cs = [
        ["jd14","gray"],
        ["jd15","pink"],
        ["jd16","green"],
        ["jd17","brown"],
        ["jd18","blue"],
        ["jd19","red"]
    ]

    l = []
    name_list = []
    for i, val in enumerate(cs):
        a = val[0] + month1
        b = val[0] + month2
        if month2 < month1:
            if i >= len(cs)-1:
                continue
            b = cs[i+1][0]+month2
        l.append([a,b,a+" - "+b])
        name_list.append(a)
        name_list.append(b)
    
    datas = data.load()
    m = data.filter(datas,"160110","171110",name_list)

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
            diff_x.append(datetime.date(2019 + date.year - year,date.month,date.day))
                

        diff_l.append([pair[2],diff_x,diff_y])
        
    plt.xlabel("date")
    plt.ylabel("")
    ls = []
    labels = []
    for i,v in enumerate(diff_l):
        print(v[1])
        plt.plot(v[1],v[2],color=cs[i][1],linestyle='--',linewidth = 2,label=v[0])
        labels.append(v[0])
    
    plt.legend(labels = labels,loc = 'best',shadow = True)
    plt.gcf().autofmt_xdate()
    plt.show()

main()