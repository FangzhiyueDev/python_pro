# ! /usr/bin/python
# ! coding=utf-8



from tornado.web import RequestHandler

from BlogWeb.methods.dbHelp import MyArticleOprate


class MyIndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        print("接受到get请求")

        # 在这里获取数据进行前端的展示
        articleOprate = MyArticleOprate()
        articles = articleOprate.getArticleList()
        self.render(template_name="index.html", articles=articles)

        pass

    def post(self, *args, **kwargs):
        print("接受到post请求")
        pass


class ArticleDetailHandler(RequestHandler):
    def get(self, *args, **kwargs):
        articleId = self.get_argument("articleId")
        articleOprate = MyArticleOprate()
        article = articleOprate.getArticleDetailInfo(articleId=articleId)
        print("接受到get请求")
        self.render(template_name="articleDetail.html", article=article)
        pass

    def post(self, *args, **kwargs):
        print("接受到post请求")
        pass


class ArticleCollectionHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print("接受到get请求")
        articleIdS = self.get_cookie("articleId")
        if articleIdS == None:
            articleIdS = ""
        articleId = self.get_argument("articleId")

        status = False
        idSet = articleIdS.split(";")
        for id in idSet:
            if id == articleId:
                status = True

        if status:
            pass
        else:
            articleIdS += (";" + articleId)
        print(articleIdS)

        try:
            self.set_cookie("articleId", articleIdS)
        except TypeError as e:
            e.with_traceback()
        finally:
            pass
        self.redirect("http://localhost:8080/index")
        pass

    def post(self, *args, **kwargs):
        print("接受到post请求")
        pass


class AllCollectionHandler(RequestHandler):
    def get(self, *args, **kwargs):
        articleSet = list()

        articleId = self.get_cookie("articleId")
        if articleId == None:
            self.redirect("http://localhost:8080/index")
            pass

        print("cookie的值是=" + articleId)
        idSet = articleId.split(";")
        print(idSet)
        for id in idSet:
            print("id=", id)
            if len(id) == 0:
                continue
            articleOprate = MyArticleOprate()
            article = articleOprate.getArticleDetailInfo(articleId=id)
            articleSet.append(article)
        self.render(template_name="getCollection.html", articleSet=articleSet)
        pass

    def post(self, *args, **kwargs):
        pass
