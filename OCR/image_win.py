# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
shaoxing vaildcode
'''

import os

# os.chdir('E:\python\Lib\site-packages\pytesser')
# os.chdir('D:\Python27\Lib\site-packages\pytesser')
from pytesser import *

threshold = 85
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

path = 'D:\\Crawler\\OCR\\tobacco\\shaoxing\\file\\'
files = os.listdir(path)
for f in files:
    print f
    im = Image.open(path + f)
    imgry = im.convert('L')
    # out = imgry.point(table,'1')
    out = imgry
    result = image_to_string(out)
    if not result.strip():
        out = out.resize((80, 40))
        result = image_to_string(out)
    result = result.replace(']', '1')
    result = result.replace(':', '1')
    result = result.replace('l', '1')
    result = result.replace('J', '1')
    result = result.replace('S', '8')
    result = result.replace('o', '0')
    result = result.replace('O', '0')
    result = result.replace("'y", "7")
    result = result.replace("*1", "7")
    result = result.replace('v', '7')
    result = result.replace('s', '6')
    result = result.replace('Z', '2')
    temp = result[0:len(result) - 2]
    print temp
    print temp.isdigit()
