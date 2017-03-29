# -*- coding: UTF-8 -*-
import codecs
import MysqlDB
from MybeautifulSoup import parse_table

doc = codecs.open('C:/Users/Administrator/Desktop/table.html', 'r+', 'GBK')

s = doc.readlines()
doc.close()

str_convert = ''.join(s)
# print str_convert
# for line in s:
#     print line



resultLsit = parse_table(str_convert)

for m in resultLsit:
    print m
MysqlDB.insert(resultLsit)
