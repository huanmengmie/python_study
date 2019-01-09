# -*- coding:UTF-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options,define
define('port',default=80,help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PoemHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                    difference=noun3)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/index',IndexHandler),(r'/poem',PoemHandler)],
        template_path = os.path.join(os.path.dirname(__file__),'templates')
    )
    print os.path.join(os.path.dirname(__file__),'templates')
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port=options.port)
    tornado.ioloop.IOLoop.current().start()