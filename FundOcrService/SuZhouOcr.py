# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
'''   
import os
from numpy import *
from pytesseract import *
from PIL import Image


import logging


LOG_FILE = 'logs\SuZhou_OCR.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG,
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filemode='w')
logger = logging.getLogger('OCR')
logger.addHandler(handler)

def im_split(im):
    im=im.convert('RGB')
    r,g,b=im.split()
    return r,g,b

def gray(im):
    imgry = im.convert('L')
    return imgry

def binary(im,num):
    threshold = num
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    imgry = im.point(table,'1')
    return imgry

def im_color(r,g,b):
    arr_r=array(r)
    arr_g=array(g)
    arr_b=array(b)
    w=r.size[0]
    h=r.size[1]
    multilist =array([[255 for col in range(w)] for row in range(h)])
    for i in range(2,h-1):
        for j in range(2,w-1):
            if (arr_r[i,j]<40)and(arr_g[i,j]<40)and(arr_b[i,j]<40):
            	multilist[i,j]=250
            else:
		multilist[i,j]=min(arr_r[i,j],arr_g[i,j],arr_b[i,j])
    imgry=Image.fromarray(uint8(multilist))
    return imgry

def im_noise(im):
    w=im.size[0]
    h=im.size[1]
    arr_im=array(im)
    multilist =array([[255 for col in range(w)] for row in range(h)])
    for i in range(2,h-1):
        for j in range(2,w-1):
            G=arr_im[i,j]
            num=0
            if (G<arr_im[i-1,j-1]):
                num=num+1
	    if (G<arr_im[i-1,j]):
                num=num+1
            if (G<arr_im[i-1,j+1]):
                num=num+1
            if (G<arr_im[i,j-1]):
                num=num+1
            if (G<arr_im[i,j+1]):
                num=num+1
            if (G<arr_im[i+1,j-1]):
                num=num+1
            if (G<arr_im[i+1,j]):
                num=num+1
            if (G<arr_im[i+1,j+1]):
                num=num+1
            if num>=7:
            	multilist[i,j]=250
            else:
                multilist[i,j]=arr_im[i,j]
    imgry=Image.fromarray(uint8(multilist))
    return imgry

def im_fill(im):
    w=im.size[0]
    h=im.size[1]
    arr_im=array(im)
    multilist =array([[255 for col in range(w)] for row in range(h)])
    for i in range(2,h-1):
        for j in range(2,w-1):
            G=arr_im[i,j]
            num=0
            if (G>arr_im[i-1,j-1]):
                num=num+1
	    if (G>arr_im[i-1,j]):
                num=num+1
            if (G>arr_im[i-1,j+1]):
                num=num+1
            if (G>arr_im[i,j-1]):
                num=num+1
            if (G>arr_im[i,j+1]):
                num=num+1
            if (G>arr_im[i+1,j-1]):
                num=num+1
            if (G>arr_im[i+1,j]):
                num=num+1
            if (G>arr_im[i+1,j+1]):
                num=num+1
            if num>=8:
            	multilist[i,j]=0
            else:
                multilist[i,j]=arr_im[i,j]
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

def recognition(im):
    result = image_to_string(im,config='num')
    result=char_repalace(result)
    temp=result[0:len(result)]
    return temp


def SuZhoufileToImage(file, id):
    try:
        print file
        im = Image.open(file)  # 打开图片
        r, g, b = im_split(im)
        ima_color = im_color(r, g, b)
        ima_noise = im_noise(ima_color)
        # ima_fill=im_fill(ima_noise)
        # ima_gray = gray(ima_fill)             #灰度化
        ima_binary = binary(ima_color, 200)  # 二值化
        Str = recognition(ima_binary)
        m_dict = {
            'result': True,
            'data': Str,
            'code': '202',
            'id': id
        }
        logger.info(Str)

    except IOError as io:
        logger.info('FileToImage error [%s]' % str(io))
        print('main1 error [%s]' % str(io))
        m_dict = {
            'result': False,
            'data': str(io),
            'code': '572',
            'id': id
        }
    except Exception as  e:
        logger.info('FileToImage error [%s]' % str(e))
        print('main1 error [%s]' % str(e))
        m_dict = {
            'result': False,
            'data': str(e),
            'code': '573',
            'id': id
        }
    logger.info('OCR Result [%s]' % str(m_dict))
    return m_dict

#
# path='/imageOcr/51suzhou/pic/'
# files = os.listdir(path)
# for f in files:
#         print path+f
#     	im = Image.open(path+f) #打开图片
#     	r,g,b=im_split(im)
# 	ima_color=im_color(r,g,b)
# 	ima_noise=im_noise(ima_color)
# 	#ima_fill=im_fill(ima_noise)
# 	#ima_gray = gray(ima_fill)             #灰度化
# 	ima_binary=binary(ima_color,200)           #二值化
# 	result=recognition(ima_binary)
#         name=path+result+'.jpg'
#     	os.rename(path+f,name)
#     	print '-------------'
#     	print result
#     	print '=============='


