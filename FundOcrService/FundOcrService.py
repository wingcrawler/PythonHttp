# -*- encoding:utf-8 -*-
import json
import os

import tornado.web

from HeFeiOcr import HeFeifileToImage
from TangShanOcr import TangShanfileToImage
from PbccrcOcr import PbccrcfileToImage
from ChongQingOcr import ChongQingfileToImage
from ZhengZhouOcr import ZhengZhoufileToImage
from SuZhouOcr import SuZhoufileToImage
from WuLuMuQiOcr import WuLuMuQifileToImage
from BeiJingOcr import BeiJingfileToImage

from OcrUnit import fileToString
import logging.handlers
import uuid
import TimeUnil

KB = 1024
MB = 1024 * 1024
GB = 1024 * MB
TB = 1024 * GB

MAX_STREAMED_SIZE = 30 * KB
Path = "file/"

LOG_FILE = 'PIL_OCR.log'

logger = logging.getLogger('OCR')


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/fileUpLoad.html")

    def post(self):
        self.id = str(uuid.uuid1())
        self.filePath = TimeUnil.dir(Path) + "/" + self.id + ".png"
        upload_path = os.path.join(os.path.dirname(__file__), 'file/')  # 文件的暂存路径
        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        token = self.get_argument("token", strip=True)
        if ("IM9AWGE2OFTCR16@2121" == token):
            code = self.get_argument("areaNumber", strip=True)
            # print token
            # print code
            for meta in file_metas:
                filename = meta['filename']
                filepath = "file/" + filename
            with open(self.filePath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])
            for case in switch(code):
                if case('0'):  # 默认识别引擎
                    result = fileToString(self.filePath, self.id)
                    break
                if case('130200'):
                    result = TangShanfileToImage(self.filePath, self.id)
                    break
                if case('340100'):
                    result = HeFeifileToImage(self.filePath, self.id)
                    break
                if case('pbccrc'):
                    result = PbccrcfileToImage(self.filePath, self.id)
                    break
                if case('500000'):
                    result = ChongQingfileToImage(self.filePath, self.id)
                    break
                if case('410100'):
                    result = ZhengZhoufileToImage(self.filePath, self.id)
                    break
                if case('320500'):
                    result = SuZhoufileToImage(self.filePath, self.id)
                    break
                if case('650100'):
                    result = WuLuMuQifileToImage(self.filePath, self.id)
                    break
                if case('110000'):
                    result = BeiJingfileToImage(self.filePath, self.id)
                    break

                if case():  # default, could also just omit condition or 'if True'
                    result = {
                        'result': False,
                        'data': "areacode error",
                        'code': '561',
                        'id': self.id
                    }
                    # No need to break here, it'll stop anyway
            self.write(json.dumps(result))
        else:
            self.write("License is invalid or expired")


@tornado.web.stream_request_body
class ByteHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/index.html")

    def prepare(self):
        self.id = str(uuid.uuid1())
        self.filePath = TimeUnil.dir(Path) + "/" + self.id + ".png"
        self.f = open(self.filePath, "wb")
        self.request.connection.set_max_body_size(MAX_STREAMED_SIZE)

    def data_received(self, data):
        self.f.write(data)

    def post(self):
        logger.info("ip " + self.request.remote_ip)
        self.f.close()
        result = fileToImage(self.filePath, self.id)
        self.write(json.dumps(result))


class callbackHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            id = self.get_arguments("imageID")
            id = id[0] if id else None
            logger.info("callback_imageID [" + id + "]")
            result = imagecallback(id)
            self.write(json.dumps(result))
        except Exception as e:
            print('postcode error [%s]' % str(e))


app = tornado.web.Application([
    (r'/file', UploadFileHandler), (r'/byte', ByteHandler), (r'/imagecallback', callbackHandler),
])

if __name__ == '__main__':
    app.listen(7020)
    tornado.ioloop.IOLoop.instance().start()
