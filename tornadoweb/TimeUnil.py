# -*- coding: utf-8 -*-
import datetime, os
import time


def timeFileFormat():
    now = datetime.datetime.now()
    MonthDayStyleTime = now.strftime("%m%d")
    return MonthDayStyleTime


def dir(path):
    thisYear = str(time.localtime()[0])
    thisMonth = str(time.localtime()[1])
    thisDay = str(time.localtime()[2])
    yearPath = path + "/" + thisYear
    monthPath = path + "/" + thisYear + '/' + thisMonth
    dayPath = path + "/" + thisYear + '/' + thisMonth + '/' + thisDay
    if not os.path.exists(yearPath):
        os.mkdir(yearPath)
    if not os.path.exists(monthPath):
        os.mkdir(monthPath)
    if not os.path.exists(dayPath):
        os.mkdir(dayPath)
    return path + "/" + thisYear + "/" + thisMonth + "/" + thisDay
