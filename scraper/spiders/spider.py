from functools import reduce

import scrapy
from scraper.items import ArticleItem
from scraper.helpers.dbhelper import TestDBHelper


# 测试用的爬虫
class Spider(scrapy.Spider):
    name = "spider"

    # 这里放你要爬取的网站的ＵＲＬ
    start_urls = ["", ]

    # 初始化爬虫,先获取爬取规则
    def __init__(self, rule_id=10, **kwargs):
        super().__init__(**kwargs)

        dbHelper = TestDBHelper()
        self.rule = dbHelper.getRule(rule_id)
        print(self.rule)
        self.start_urls[0] = self.rule.url

    # 这里是如何处理你爬取回来的信息
    def parse(self, response):
        articles = response.xpath(self.rule.loop_rule)

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

            item = ArticleItem()
            item['table_name'] = talbe_name
            item['title'] = title
            item['content'] = content
            item['type'] = type
            item['url'] = url

            yield item
