# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import numpy
import data

def main():
    month = input("please input month 01 ~ 12:  ");
    cs = {"jd14"+month:"gray","jd15"+month:"pink","jd16"+month:"green","jd17"+month:"brown","jd18"+month:"blue","jd19"+month:"red"}
    datas = data.load()
    m = data.filter(datas,"160110","171110",cs)
    plt.xlabel("date")
    plt.ylabel("")
    ls = []
    for c in cs:
        if c not in m:
            continue
        d = m[c]
        plt.plot(d["x"],d["y"],color=cs[c],linestyle='--',linewidth = 2,label=c)
    
    plt.legend(labels = cs.keys(),loc = 'best',shadow = True)
    plt.gcf().autofmt_xdate()
    plt.show()

main()