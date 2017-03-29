# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
'''   
import os
from numpy import *
#os.chdir('E:\python\Lib\site-packages\pytesser')   
from pytesseract import *
from PIL import Image


def gray(im):
    imgry = im.convert('L')
    #r,g,b=im.split()
    return imgry

def binary(im):
    threshold = 125
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
    imgry = im.resize((120,40))
    return imgry

def im_save(im,path_save):
    im.save(path_save)
    return 0

def char_repalace(result):
    result=result.replace(' ','')
    return result


path='/imageOcr/hefei_train/'
path_s='/imageOcr/hefei_train2/'
files = os.listdir(path)
num=1
for f in files:
    im = Image.open(path+f) #打开图片
    im=gray(im)             #灰度化
    #im=im_array(im)         #图片扩充
    im=binary(im)           #二值化
    im_save(im,path_s+str(num)+'.tiff')
    #im.show()
    #im=im_size(im)          #图片放大
    result = image_to_string(im,config='tangshan')
    result=char_repalace(result)
    temp=result[0:len(result)]
    name=path+temp+'.jpg'
    print name
    os.rename(path+f,name)
    print '-------------'
    print result
    print '=============='
    num=num+1
    #abcdefghijklmnopqrstuvwxyz

