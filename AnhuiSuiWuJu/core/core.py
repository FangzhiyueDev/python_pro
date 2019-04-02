# ！/usr/bin/python3.5
# ! coding=utf-8


# def directoryChooser():
#     directory = tkinter.filedialog.askdirectory()
#     os.chdir(directory)
#     for files in os.listdir(directory):
#         if files.endswith(".mp3"):
#             realdir = os.path.realpath(files)
#             audio = mutagen.id3.ID3(realdir)
#             realnames.append(audio['TIT2'].text[0])


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from AnhuiSuiWuJu.Parse import ParseHtml


class AutoExec(object):
    """
    这个对象的作用是用来执行一个自动化的脚本程序
    """

    accountS = ""
    passwordS = ""
    path = "/home/fang/Desktop/"
    types = ".html"
    fileName = ""

    def __init__(self, account, password, saveFile):
        self.accountS = account
        self.passwordS = password
        self.saveFile = saveFile

    def writeFile(self, pageSource):
        """
        将获得的源代码写入到文件中
        :param pageSource:  网页的数据
        :return: none
        """
        with open(self.fileName, "w") as f:
            print("保存的文件的是" + self.fileName)
            f.write(pageSource)
            f.flush()
            f.close()

    def exec(self):
        """
        执行自动化教本程序
        :return:
        """
        browser = webdriver.Firefox()
        browser.set_window_size(1300, 800)
        browser.get('https://etax.ah-n-tax.gov.cn/')
        loginButton = browser.find_element_by_id("login")
        loginButton.click()

        # 切换到iframe中
        iframe = browser.find_element_by_id("loginSrc");
        browser.switch_to_frame(iframe)

        # 避免出错，使用休眠进行解决
        time.sleep(6)

        username = browser.find_element_by_id("username")
        username.send_keys(self.accountS)

        password = browser.find_element_by_id("password")
        password.send_keys(self.passwordS)

        slide = browser.find_element_by_class_name("sliderVc_button")

        ActionChains(browser).drag_and_drop_by_offset(slide, 182, 0).perform()

        ActionChains(browser).release(slide).perform()
        time.sleep(2)

        # loginSubmit = browser.find_element_by_class_name("login_btn");

        browser.execute_script("login('fm2')")

        browser.switch_to_default_content()

        time.sleep(6)

        # 这个是解决界面弹出的窗口
        browser.find_element_by_id("neverGuide").click()

        # 下面的代码实现的是选择查询的子菜单
        menus = browser.find_element_by_class_name("home-tab-title")
        alist = menus.find_element_by_xpath("//a[@title='我要查询']")
        alist.click()

        # 进入到下一个目录
        items = browser.find_element_by_id("home-tab-tab")
        div3 = items.find_element_by_xpath("div[3]")
        div3_div_ul = div3.find_element_by_xpath("div/ul")
        div3_div_ul_li6 = div3_div_ul.find_element_by_xpath("li[6]")
        div3_div_ul_li6.click()

        # 进行未申报情况查询
        div3_div_div = div3.find_element_by_xpath("div/div")
        real_link = div3_div_div.find_element_by_xpath("div/div/div/dl/dd/a")
        real_link.click()

        # 上面已经查询到了数据，下面就是跳转到指定的iframe

        frameQuery = browser.find_element_by_id("layui-layer-iframe16")
        browser.switch_to_frame(frameQuery)
        # 在这里进行停留是发现在浏览器转换到iframe的时候，系统会部分查不到数据
        time.sleep(5)
        print(browser.page_source)
        # 写入到文件中
        # self.fileName = self.path + self.accountS + self.types
        # self.writeFile(browser.page_source)

        # 下面便是文件的读取
        parse = ParseHtml.ParseHtml(self.saveFile, self.accountS)
        parse.feed(browser.page_source)

    def changeFileSavePath(self, path):
        """
        更改解析文件html的保存路径
        :return: self
        """
        self.path = path


if __name__ == '__main__':
    AutoExec("9134010034377792X4", "yw88888888").exec()
