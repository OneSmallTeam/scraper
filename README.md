# 这是一个用于数据采集的轮子

### 功能描述：
1. 每天监控用户关注的网站
2. 将**用户需要的**更新的内容存进数据库
3. 将更新信息整合，定期发送给本人
4. 专为个人定制的信息流

## 设计思想：
![image](http://upload-images.jianshu.io/upload_images/4781155-2b42473b0ac9556e?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 一、[采集数据部分](https://github.com/OneSmallTeam/scraper)--主要由Python爬虫实现
1. 用[dbhelper](https://github.com/Niracler/scraper/blob/master/scraper/helpers/dbhelper.py)来读取 **_rule** 表中的爬取规则,将其存储到 [rule](https://github.com/Niracler/scraper/blob/master/scraper/helpers/rule.py) 对象中。
2. [spider](https://github.com/Niracler/scraper/blob/master/scraper/spiders/spider.py) 按照  [rule](https://github.com/Niracler/scraper/blob/master/scraper/helpers/rule.py) 对象中的规则爬取网页内容。将网页内容存储到相应的数据库中。
  
#### 二、[产生爬取规则部分](https://github.com/OneSmallTeam/scraper)--规则调试
1. 由[test_spider](https://github.com/Niracler/scraper/blob/master/scraper/spiders/test_spider.py)用来测试爬取规则是否可行。
2. 可行的话，将爬取规则放进 **_rule** 表中


## 设计难点
1. 对用户要求较高，使用成本偏高。
2. 不过后期可以通过元素采集器的方法来降低使用成本。
2. 通用爬虫实现较为困难。
3. 爬虫的通用性提高后，对于一些大公司的网站就不适用了。


## 我这个项目是从以下项目分支出来的:
https://github.com/OneSmallTeam/scraper



## 参考项目：

[scrapy框架](https://scrapy.org/)  信息采集部分主要就是用的scrapy框架

[H-Viewer](https://github.com/PureDark/H-Viewer) 非常感谢这个项目,让我们找到了设计方向
