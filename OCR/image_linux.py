# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
zj tobacco
'''
import os

os.chdir('D:\Python27\Lib\site-packages\pytesser')
# import numpy as np
# import cv2
from PIL import Image, ImageEnhance, ImageFilter
import sys
from pytesser import image_to_string

threshold = 85
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

'''
path1='C:\\Users\\Administrator\\Desktop\\code\\code\\02.png'   
im=Image.open(path1) 
im=im.split()
im[0].show()
im[1].show()
im[2].show()               
imgry = im.convert('L')
out = imgry.point(table,'1')
#out = out.resize((80,40))
result = image_to_string(out) 
result=result.replace(']','1')    
print result
if not result.strip():
    print 'haha'        

path = 'C:\\Users\\Administrator\\Desktop\\image50\\image50\\'
files = os.listdir(path)
for f in files:
    im = Image.open(path + f)
    imgry = im.convert('L')
    out = imgry.point(table, '1')
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
    result = result.replace("'y", "7")
    result = result.replace("*1", "7")
    result = result.replace('v', '7')
    result = result.replace('s', '6')

    print f.title() + '\t' + result.strip()
'''


def image_ocr(image_path):
    print image_path
    image_object = Image.open(image_path)
    imgry = image_object.convert('L')
    out = imgry.point(table, '1')
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
    result = result.replace("'y", "7")
    result = result.replace("*1", "7")
    result = result.replace('v', '7')
    result = result.replace('s', '6')

    return result.strip()
