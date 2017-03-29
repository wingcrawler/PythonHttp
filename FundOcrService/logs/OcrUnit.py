# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
'''

import os, base64

import logging
from pytesseract import *
from PIL import Image

LOG_FILE = 'logs\PIL_OCR.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG,
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filemode='w')
logger = logging.getLogger('OCR')
logger.addHandler(handler)

threshold = 135
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)


# need  Image object
def image_ocr(im):
    # print image_path
    # im = Image.open(image_path)
    imgry = im.convert('L')
    out = imgry.point(table, '1')
    # out = out.resize((100,25))
    # out.show()
    result = image_to_string(imgry)
    if not result.strip():
        out = out.resize((200, 50))
        result = image_to_string(out)
    result = result.replace('S', '8')
    result = result.replace('B', '8')
    result = result.replace(']<', 'k')
    result = result.replace("'7", '7')
    result = result.replace('_j', 'j')
    result = result.replace(' ', '')
    result = result.replace('i;r', 'ir')
    result = result.replace('<', 'x')
    result = result.replace('>', '')
    result = result.replace('[', '')
    result = result.replace(']', '')
    result = result.replace('{', '')
    result = result.replace('}', '')
    result = result.replace(';', '')
    temp = result[0:len(result) - 2]

    return temp.strip()


def base64Tofile(Str):
    imgData = base64.b64decode(Str)
    leniyimg = open('imgout2.png', 'wb')
    leniyimg.write(imgData)
    leniyimg.close()
    im = Image.open('imgout2.png')
    Str = image_ocr(im)
    print Str
    return Str


def fileToImage(file, id):
    try:
        print file
        im = Image.open(file)
        Str = image_ocr(im)
        Str = Str.lower()
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


def imagecallback(str):
    m_dict = {
        'result': True,
        'data': str,
        'code': '215',
    }
    return m_dict
