# -*- coding: UTF-8 -*-
'''
Created on 2016-4-26
Auther wsjian
Service Andy
'''
from numpy import *
import logging
from pytesseract import *
from PIL import Image

LOG_FILE = 'logs\TangShan_OCR.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG,
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filemode='w')
logger = logging.getLogger('OCR')
logger.addHandler(handler)


def gray(im):
    imgry = im.convert('L')
    # r,g,b=im.split()
    return imgry


def binary(im):
    threshold = 120
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    imgry = im.point(table, '1')
    return imgry


def im_array(im):
    arr = array(im)
    multilist = array([[255 for col in range(45)] for row in range(16)])
    for i in range(10):
        for j in range(40):
            multilist[i + 3, j + 4] = arr[i, j]
    imgry = Image.fromarray(uint8(multilist))
    return imgry


def im_size(im):
    imgry = im.resize((80, 20))
    return imgry


def im_save(im, path_save):
    im.save(path_save)
    return 0


def char_repalace(result):
    result = result.replace('El', '0')
    result = result.replace('U', '0')
    result = result.replace('D', '0')
    result = result.replace('l', '1')
    result = result.replace('E5', '8')
    result = result.replace('B', '8')
    result = result.replace('S', '5')
    result = result.replace('Z', '2')

    return result


def TangShanfileToImage(file, id):
    try:
        print file
        im = Image.open(file)
        im = gray(im)  # 灰度化
        im = im_array(im)  # 图片扩充
        im = binary(im)  # 二值化
        im = im_size(im)  # 图片放大
        Str = image_to_string(im, config='tangshan')
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

# ```
# path = '/imageOcr/tangshan/'
# files = os.listdir(path)
# num = 1
# for f in files:
#     im = Image.open(path + f)  # 打开图片
#     im = gray(im)  # 灰度化
#     im = im_array(im)  # 图片扩充
#     im = binary(im)  # 二值化
#     im = im_size(im)  # 图片放大
#     result = image_to_string(im, config='tangshan')
#     # result=char_repalace(result)
#     temp = result[0:len(result)]
#     name = path + temp + '.png'
#     print name
#     os.rename(path + f, name)
#     # im_save(im,path_s+str(num)+'.tif')
#     print '-------------'
#     print result
#     print '=============='
#     # abcdefghijklmnopqrstuvwxyz
# ```
