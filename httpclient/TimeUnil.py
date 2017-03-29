# -*- coding: utf-8 -*-
import datetime


def timeFileFormat():
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%m-%d_%H-%M-%S_")
    return otherStyleTime
