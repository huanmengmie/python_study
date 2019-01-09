# -*- coding:UTF-8 -*-


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

class ParentHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('parent.html')


class ChildHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('child.html')




if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler),(r"/parent",ParentHandler),(r"/child",ChildHandler)],
        template_path = os.path.join(os.path.dirname(__file__),'templates')
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print 'server start,click http://localhost:%d' % options.port
    tornado.ioloop.IOLoop.instance().start()


# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
#
