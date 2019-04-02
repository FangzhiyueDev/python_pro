# ! /usr/bin/python
# ! coding=utf-8

import tornado.web

from MyWeb.methods.db import addUser


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        lines = addUser(username, password)


