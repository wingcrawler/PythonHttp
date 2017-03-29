# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
'''   
import os
from numpy import *
from pytesseract import *
from PIL import Image


def gray(im):
    imgry = im.convert('L')
    #r,g,b=im.split()
    return imgry

def binary(im):
    threshold = 135
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    imgry = im.point(table,'1')
    return imgry

def im_array(im):
    arr=array(im)
    multilist =array([[255 for col in range(45)] for row in range(16)])
    for i in range(10):
        for j in range(40):
            multilist[i+3,j+4]=arr[i,j]
    imgry=Image.fromarray(uint8(multilist))
    return imgry

def im_size(im):
    imgry = im.resize((80,20))
    return imgry

def im_save(im,path_save):
    im.save(path_save)
    return 0

def char_repalace(result):
    result=result.replace(' ','')
    return result


path='/imageOcr/codd/'
#path_s='/imageOcr/yanghang_train/'
files = os.listdir(path)
num=1
for f in files:
    im = Image.open(path+f) #打开图片
    im=gray(im)             #灰度化
    #im=im_array(im)         #图片扩充
    im=binary(im)           #二值化
    #im=im_size(im)          #图片放大
    result = image_to_string(im,config='yanghang',lang='num')
    result=char_repalace(result)
    temp=result[0:len(result)]
    name=path+temp+'.png'
    print name
    os.rename(path+f,name)
    #im_save(im,path_s+str(num)+'.tif')
    print '-------------'
    print result
    print '=============='
    num=num+1
    #abcdefghijklmnopqrstuvwxyz

