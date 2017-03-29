# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web
import os
import json
from OcrUnit import fileToImage
from OcrUnit import imagecallback
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


class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/fileUpLoad.html")

    def post(self):
        self.id = str(uuid.uuid1())
        self.filePath = TimeUnil.dir(Path) + "/" + self.id + ".png"
        upload_path = os.path.join(os.path.dirname(__file__), 'file/')  # 文件的暂存路径
        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            filepath = "file/" + filename
        with open(self.filePath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
            up.write(meta['body'])
        result = fileToImage(self.filePath, self.id)

        self.write(json.dumps(result))


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
    app.listen(7010)
    tornado.ioloop.IOLoop.instance().start()
