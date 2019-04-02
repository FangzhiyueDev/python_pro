#!/usr/bin/python
# ! coding=utf-8


from mysql.connector import connect

conn = connect(host="localhost", user="root", password="123", db="BlogTest", port=3306, charset="utf8")
cur = conn.cursor()

class MyArticleOprate:
    """

    这个类的作用是用来操作文章的相关数据的操作
    """

    def getArticleList(self):
        cur.execute("select id,title,content from article")
        articles = cur.fetchall()
        return articles

    def getArticleDetailInfo(self, articleId):
        sql = "select id,title,content from article where id=" + articleId
        print(sql)
        cur.execute(sql)
        articles = cur.fetchall()
        return articles[0]


if __name__ == '__main__':
    demo = MyArticleOprate()
    articles = demo.getArticleList()
    for article in articles:
        print(article)
