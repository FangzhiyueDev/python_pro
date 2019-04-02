# ! /usr/bin/python
# ! coding=utf-8


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from MyWeb.application import application
from tornado.options import define, options

define("port", default=8080, help="run on the gived port", type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print("development server is run....")
    print("quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()
