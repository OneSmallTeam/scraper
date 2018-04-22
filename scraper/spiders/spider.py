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
    def __init__(self, rule_id=33, **kwargs):
        super().__init__(**kwargs)

        dbHelper = TestDBHelper()
        self.rule = dbHelper.getRule(rule_id)
        print(self.rule)
        self.start_urls[0] = self.rule.url

        self.parses = dict(
            article=self.article_parse,
            article_no_content=self.article_no_content_parse
        )

    # 这里是如何处理你爬取回来的信息
    def parse(self, response):
        yield scrapy.Request(self.rule.url, callback=self.parses[self.rule.type])

    # 爬取内容的
    def content_parse(self, response):
        article = response.meta['article']
        url = article.xpath(self.rule.url_rule).extract_first()
        talbe_name = self.rule.table_name
        title = article.xpath(self.rule.title_rule).extract_first()
        type = article.xpath(self.rule.type_rule).extract()
        content = response.xpath(self.rule.content_rule).extract()

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
        except Exception  as e:
            print(e)

        if not content:
            return

        if len(content) > 800:
            content = content[:800] + "..."

        item = ArticleItem()
        item['table_name'] = str(talbe_name)
        item['title'] = str(title)
        item['content'] = str(content)
        item['type'] = str(type)
        item['url'] = str(url)

        yield item

    # 内容要去特地查找内容的文章
    def article_no_content_parse(self, response):
        articles = response.xpath(self.rule.loop_rule)

        for article in articles:
            url = article.xpath(self.rule.url_rule).extract_first()

            try:
                if (url[0] == '/'):
                    url = self.start_urls[0] + url
            except Exception as e:
                print(e)

            # content的内容要特地去爬取
            yield scrapy.Request(url, callback=self.content_parse, meta={'article': article})

    # 第一类普通的文章
    def article_parse(self, response):
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
            item['table_name'] = str(talbe_name)
            item['title'] = str(title)
            item['content'] = str(content)
            item['type'] = str(type)
            item['url'] = str(url)

            yield item
