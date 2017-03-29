import tornado.ioloop
import tornado.web
import json
from OcrUnit import base64Tofile
from OcrUnit import image_ocr

l = []


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        # id = self.get_argument('id')
        # print id
        self.render('a.html', title='haha', items=l)

    @property
    def crawle(self):
        print(self.request.remote_ip)
        talk = self.get_argument('base64')
        talk = str(talk)
        print talk
        result = base64Tofile(talk)
        data = json.dumps(result)
        return data

    def api_response(self, data):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        data = json.dumps(callback=self.async_callback(self.clear(self)))
        self.finish(data)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        count = 1
        # self.data_carwle
        self.finish(callback=self.async_callback(self.crawle))

    def data_carwle(self, response, error):
        self.api_response(response[0])


def make_app():
    return tornado.web.Application([
        (r"/code", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(7101)
    tornado.ioloop.IOLoop.current().start()
