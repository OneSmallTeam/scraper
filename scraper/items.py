# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# define the fields for your item here like:
# name = scrapy.Field()

# 我们爬取的对象
class ArticleItem(scrapy.Item):
    table_name = scrapy.Field()  # 存储对象的表名
    title = scrapy.Field()  # 存储对象的题目
    content = scrapy.Field()  # 存储对象的内容
    url = scrapy.Field()  # 存储对象的链接
    type = scrapy.Field()  # 存储对象的类型
