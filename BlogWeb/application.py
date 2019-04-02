#!/usr/bin/python
# ! coding=utf-8

from BlogWeb.url import url
import os
import tornado.web

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics")
)

application = tornado.web.Application(

    handlers=url,
    **settings
)
