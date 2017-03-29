import os

# os.chdir('E:\python\Lib\site-packages\pytesser')
# os.chdir('D:\Python27\Lib\site-packages\pytesser')
from pytesser import *

threshold = 180
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

path = 'D:\\Crawler\OCR\\tangshan\\'
files = os.listdir(path)
i = 1
for f in files:
    print f
    im = Image.open(path + f)
    imgry = im.convert('L')
    out = imgry.point(table, '1')
    # out = imgry
    result = image_to_string(out)

    if (i % 8 == 0):
        print(i)

    print str(i) + ": " + result.strip() + "\t",
    i = i + 1
