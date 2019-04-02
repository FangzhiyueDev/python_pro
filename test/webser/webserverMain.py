# ! /usr/bin/python
# ! coding=utf-8


# 命令行解析
import tornado.options

import tornado.ioloop

import tornado.httpserver

import tornado.web

import pymysql

tornado.options.define("port", default=12345, type=int, help="run on the gived port")


class MyIndexHandler(tornado.web.RequestHandler):

    def my_write(self, *data):
        """
        该方法的作用是实现对浏览器数据的回写
        :param data:  传递的是一个数据集合，是可以迭代的对象，
        :return: void
        """
        self.write("nihap:{}".format(self.path_args))

    # 这个是对get请求的处理
    def get(self):
        name = self.get_argument("name", ("fang", "jiandan", 16780))
        # 在这里我们进行数据库链接查询数据，
        print("接受到请求")
        self.my_write(name)


class MydbConnection:
    """
     这个类的作用是进行数据库的链接

    """
    __port = 3306
    __user = "root"
    __host = "localhost"
    __password = "123"
    __db = "Person"
    __cursor = None

    def __init__(self):
        try:
            cursor = pymysql.connections.Connection(self.__host,
                                                    self.__user, self.__password, self.__db, self.__port)
        except BaseException:
            print("数据库链接错误")
        else:
            print("数据库连接成功")

    def get_cursor(self):
        return self.__cursor

    def close_db_connection(self):
        if self.__cursor:
            if isinstance(self.__cursor, pymysql.connections.Cursor):
                self.__cursor.close()
            else:
                print("游标错误")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", MyIndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()
