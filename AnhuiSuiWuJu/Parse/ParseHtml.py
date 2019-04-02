#!/usr/bin/python
# !encoding=utf-8


from html.parser import HTMLParser

from AnhuiSuiWuJu.exelOprate.OprateExcel import OprateExcel

defauleTitle = ["征收项目", "征收品目", "年度", "月份", "所属期起", "所属期止", "纳税期限", "申报期限", "原申报期限", "征收方式"]


class ParseHtml(HTMLParser):
    var = ""

    def __init__(self, saveFile, account):
        HTMLParser.__init__(self)
        self.saveFile = saveFile
        self.account = account
        self.opra = OprateExcel(self.saveFile)
        self.opra.openFile()
        # self.opra.writeFile(["征收项目", "征收品目", "年度", "月份", "所属期起", "所属期止", "纳税期限", "申报期限", "原申报期限", "征收方式"])

    def handle_starttag(self, tag, attrs):
        self.var = tag
        if self.var == "tr":
            self.list1 = []

    def handle_endtag(self, tag):
        if tag == "tr":  # 代表的和解析一行的数据完成
            if len(self.list1) !=0:
                self.list1.append(self.account)
                print(self.list1)
                self.opra.writeFile(self.list1)
        if tag == "html":
            self.opra.saveFile()

    def handle_data(self, data):
        if self.var == "td":
            data = str(data).replace("\t", "")
            data = data.replace("\n", "")
            data = data.replace(" ", "")
            data = data.replace("\xa0", "")
            for value in defauleTitle:
                if value == data:
                    return

            if not data.strip() == "":
                self.list1.append(data)
            # print(data)


html = "<html><tr>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t企业所得税&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t应纳税所得额&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t2019&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t01&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t2018-01-01&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t2018-12-31&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t年&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t2019-05-31&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t2019-05-31&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t<td class=\"td_list_2\">\n" \
       "\t\t\t\t\t\t查账征收&nbsp;\n" \
       "\t\t\t\t\t</td>\n" \
       "\t\t\t\t\t\n" \
       "\t\t\t\t</tr></html>"

if __name__ == '__main__':
    parse = ParseHtml("/home/fang/Desktop/save1.xlsx", "24252352352")
    parse.feed(html)
