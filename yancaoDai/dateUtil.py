# -*- coding: UTF-8 -*-

import datetime


def date_List():
    d1 = datetime.date.today()
    # print d1
    # 加一天：
    d2 = d1
    # print d2
    # 減一天：
    dateLsit = [];
    for i in range(30, 392, +30):
        d3 = d2 + datetime.timedelta(-i)
        d4 = d1
        d1 = d3 + datetime.timedelta(-1)
        result = (d4.strftime('%Y%m%d'), d3.strftime('%Y%m%d'))
        dateLsit.append(result)

    return dateLsit
