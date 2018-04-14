#!/bin/sh
# 进入虚拟环境
source venv/bin/activate

scrapy crawl test_spider > log/test.log