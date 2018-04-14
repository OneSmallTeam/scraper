"""
这是对于每个网站的相同操作的抽象类
"""
import json

from bs4 import BeautifulSoup
import requests




# 建立对象时要指定其url
class Model():
    # 初始化数据，以及初始化动作
    def __init__(self, url):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        self.myList = {}
        self.url = url
        self.upDatedMyList()


    # 最重要的是重写这个方法
    def fillMyList(self):
        pass

    # 更新列表
    def upDatedMyList(self):
        self.html = self.getHTMLText()
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.fillMyList()
        self.save_in_sql()

    # 获取ＨＴＭＬ页面
    def getHTMLText(self):
        try:
            r = requests.get(self.url, timeout=30,headers=self.headers)
            r.raise_for_status()  # 不是200,引发HTTPError异常
            # r.encoding = r.apparent_encoding  # 转编码,假如编码有问题，可以试试
            r.encoding = "UTF-8"
            # print(r.encoding)
            return r.text
        except:
            print("产生异常")

    # 存储到数据库
    def save_in_sql(self):
        pass

    # 利用数据结构展示并输出结果
    def printMyList(self):
        # indent=1是格式化的模式,ensure_ascii=False解决编码问题
        jsonDumpsIndentStr = json.dumps(self.myList, indent=1, ensure_ascii=False)
        print(jsonDumpsIndentStr)