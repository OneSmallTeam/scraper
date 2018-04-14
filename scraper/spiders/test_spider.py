from functools import reduce

import scrapy
from scraper.helpers.rule import Rule
from scraper.helpers.dbhelper import dbHelper


# 测试用的爬虫
class Spider(scrapy.Spider):
    name = "test_spider"

    # 这里放你要爬取的网站的ＵＲＬ
    start_urls = ["https://www.llss.pw/wp", ]

    # 初始化爬虫,先获取爬取规则
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rule = Rule()
        self.rule.url = self.start_urls[0]
        self.rule.loop_rule = "//article"
        self.rule.title_rule = "header/h1/a/text()"
        self.rule.content_rule = "div/p/text()"
        self.rule.type_rule = "footer/span/a/text()"
        self.rule.url_rule = "header/h1/a/@href"
        self.rule.table_name = "hacg"

        # 请帮我放到数据库
        # dbHelper.setRule(self.rule)


    # 这里是如何处理你爬取回来的信息
    def parse(self, response):
        articles = response.xpath(self.rule.loop_rule)
        # print(articles.extract())

        for article in articles:
            url = article.xpath(self.rule.url_rule).extract_first()
            talbe_name = self.rule.table_name
            title = article.xpath(self.rule.title_rule).extract_first()
            content = article.xpath(self.rule.content_rule).extract()
            type = article.xpath(self.rule.type_rule).extract()

            try:
                type = str(reduce(lambda x, y: str(x) + " " + str(y), type))
            except Exception as e:
                print(e)

            try:
                if (url[0] == '/'):
                    url = self.start_urls[0] + url
            except Exception as e:
                print(e)

            try:
                content = str(reduce(lambda x, y: str(x) + str(y), content))

            except Exception as e:
                print(e)

            yield {
                'table_name': talbe_name,
                'title': title,
                'content': content,
                'type': type,
                'url': url
            }
