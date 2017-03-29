#!/usr/bin/env python
# created by yao
# 2016.12.23
from PIL import Image
im = Image.open('../file/Money/Test01.jpg')

imgWidth = 510 # width of the image you cut off
startX = 212
startY = 712 # the first line position-y
splitPoxis = 21 # split height
blackHeigh = 6 # black line height
maxLineNumber = 20


# function to deal image
def pasteImg( startY, index):
    box = (startX, startY + splitPoxis*index-blackHeigh,startX + imgWidth,startY + splitPoxis*index)
    #print box
    region = im.crop(box)

    box_dealed = (startX,startY + splitPoxis * index,startX + imgWidth,startY + splitPoxis*index+blackHeigh)
    #print box
    region_dealed = im.crop(box_dealed)

    im.paste( region, box_dealed )


pasteImg(startY, 0)

for index in range(1,maxLineNumber):
    pasteImg( startY, index )


im.save('../file/Money/dealed010.jpg')
im.show()