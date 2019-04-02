#! /usr/bin/python
# ! coding=utf-8

from BlogWeb.Handlers.IndexHandler import MyIndexHandler
from BlogWeb.Handlers.IndexHandler import ArticleDetailHandler
from BlogWeb.Handlers.IndexHandler import ArticleCollectionHandler
from BlogWeb.Handlers.IndexHandler import AllCollectionHandler
url = [
    (r'^/index', MyIndexHandler),
    (r'^/detailPage', ArticleDetailHandler),
    (r'^/collection', ArticleCollectionHandler),
    (r'^/allCollection',AllCollectionHandler)
]
