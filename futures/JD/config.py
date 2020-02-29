# -*- coding: UTF-8 -*-

Name = "JD"

YearToColor = {
    "08" : "gold",
    "09" : "navy",
    "10" : "deeppink",
    "11" : "cyan",
    "12" : "olivedrab",
    "13" : "fuchsia",
    "14" : "slategray",
    "15" : "darkorange",
    "16" : "black",
    "17" : "darkred",
    "18" : "lime",
    "19" : "red",
    "20" : "blue",
    "21" : "gray"
}

MonthToColor = {
    "01" : "blue",
    "02" : "deeppink",
    "03" : "fuchsia",
    "04" : "peru",
    "05" : "lime",
    "06" : "teal",
    "07" : "darkred",
    "08" : "cyan",
    "09" : "red",
    "10" : "darkorange",
    "11" : "gold",
    "12" : "navy"
}

# y轴刻度
y_major_locator = 100

y_diff_major_locator = 50

def NextYear(y):
    i = int(y)
    i = i + 1
    y = str(i)
    if len(y) ==1:
        y = "0" + y
    return y