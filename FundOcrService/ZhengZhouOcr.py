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


LOG_FILE = 'logs\ZhengZhou_OCR.log'
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
    multilist =array([[255 for col in range(66)] for row in range(29)])
    for i in range(29):
        for j in range(66):
            if (arr_r[i,j]<40)and(arr_g[i,j]<40)and(arr_b[i,j]<40):
            	multilist[i,j]=1
    imgry=Image.fromarray(uint8(multilist))
    return imgry

def im_noise(im):
    arr_im=array(im)
    multilist =array([[255 for col in range(66)] for row in range(29)])
    for i in range(2,28):
        for j in range(2,65):
            G=arr_im[i,j]
            num=0
            if (arr_im[i-1,j-1]>G):
                num=num+1
	    if (arr_im[i-1,j]>G):
                num=num+1
            if (arr_im[i-1,j+1]>G):
                num=num+1
            if (arr_im[i,j-1]>G):
                num=num+1
            if (arr_im[i,j+1]>G):
                num=num+1
            if (arr_im[i+1,j-1]>G):
                num=num+1
            if (arr_im[i+1,j]>G):
                num=num+1
            if (arr_im[i+1,j+1]>G):
                num=num+1
            if num>=7:
            	multilist[i,j]=250
            else:
                multilist[i,j]=arr_im[i,j]
    imgry=Image.fromarray(uint8(multilist))
    return imgry

def im_fill(im):
    arr_im=array(im)
    multilist =array([[255 for col in range(66)] for row in range(29)])
    for i in range(2,28):
        for j in range(2,65):
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
            if num>=4:
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
    result = image_to_string(im,config='num',lang='zhengzhou+eng')
    result=char_repalace(result)
    temp=result[0:len(result)]
    return temp
def ZhengZhoufileToImage(file, id):
    try:
        print file
        im = Image.open(file)  # 打开图片
        r, g, b = im_split(im)
        im_Color = im_color(r, g, b)
        im_Noise = im_noise(im_Color)
        im_Fill = im_fill(im_Noise)
        Str = recognition(im_Fill)
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

# path='/imageOcr/51zhengzhou/51zhengzhou/pic/'
# path_s='/imageOcr/51zhengzhou/51zhengzhou/test/'
# files = os.listdir(path)
# num=1
# for f in files:
#     im = Image.open(path+f) #打开图片
#     r,g,b=im_split(im)
#     im_Color=im_color(r,g,b)
#     im_Noise=im_noise(im_Color)
#     im_Fill=im_fill(im_Noise)
#     result=recognition(im_Fill)
#     name=path+result+'.jpg'
#     os.rename(path+f,name)
#     im_save(im_Fill,path_s+result+'__'+str(num)+'.tiff')
#     print '-------------'
#     print result
#     print '=============='
#     num=num+1
