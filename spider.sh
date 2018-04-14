#!/bin/sh
# 进入虚拟环境
source venv/bin/activate

scrapy crawl spider > log/spider.log