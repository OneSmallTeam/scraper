### 背景：[信息过载](https://baike.baidu.com/item/%E4%BF%A1%E6%81%AF%E8%BF%87%E8%BD%BD)
人类的记忆和信息处理能力都是有限的，但生活于其中的环境所获取或接收的信息量总是远远高于其所能消费、承受或需要的信息量，大量冗余的信息严重干扰了其对相关有用信息的准确分析和正确选择。尤其是互联网发展的今天，人们接触太多的信息，接入超过自己需要、超过自己处理能力的信息，并且这些信息的真实性无法验证，随时可能被错误信息误导，在信息不断膨胀的互联网，尤其是在标榜着多人贡献的Web2.0 时代，信息重复与信息过载尤为明显。

**相关文章：**
[信息过载是个天大的问题](http://www.xinli001.com/info/100381655)
[Long Live RSS：有感于微广场之死](https://blessing.studio/long-live-rss/)

### 功能需求：
这个内容爆炸时代，只要意识到了「我被信息所绑架」这个问题后，用户自然会想要一种更高级的聚合信息和动态更新解决方案，比如 RSS 。但是这种技术实在是太过于古老了，以至于快要被淘汰，很多网站都不支持rss这种技术，而且各大网站越发封闭，所以我想试着做一个**为用户聚合信息**的软件。能为用户将每天关注的的消息整合起来，以供一次性阅读。最关键的技术是爬虫技术，利用python语言抓取用户关注的网页信息存至数据库。作品最大的优势是专为个人定制的信息流。


### 功能描述：
1. 每天监控用户关注的网站
2. 将**用户需要的**更新的内容存进数据库
3. 将更新信息整合，定期发送给本人
4. 专为个人定制的信息流

### 设计思想：
![image.jpeg](https://upload-images.jianshu.io/upload_images/4781155-94374bb597772680.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 这个项目"暂时"主要分为五大部分

**[采集数据部分](https://github.com/OneSmallTeam/scraper)--主要由Python爬虫实现**

**[产生爬取规则部分](https://github.com/OneSmallTeam/scraper)--规则调试**

**处理客户端发送的请求--Java业务逻辑实现**

**接口部分--Java实现接口**

**[客户端部分](https://github.com/OneSmallTeam/one)--微信小程序面向用户**





### 第一个阶段
展示订阅阶段，向用户提供可以选择的订阅项，让用户能够选择自己的信息流的来源，这个阶段用户处于被动接受阶段，只能订阅我们这边爬取的内容。这个阶段用微信小程序来跟用户交互。微信小程序中，用户可以看到我们的信息流推送以及能够订阅有兴趣的信息来源。



### 第二个阶段
web网页阶段，用户可以从web网站中通过微信账号访问我们的网站，。


### 第三个阶段
用户高度自定义阶段。用户可以自己生成爬取规则。


### 第四个阶段
优化用户自定义的水平，降低使用门槛。

### 参考项目：
[爬取简书全站文章并生成 API](https://www.jianshu.com/p/c546c175b763)

[feeddiy](http://www.feeddiy.com/)

[bilibili2RSS](https://github.com/DIYgod/bilibili2RSS)

[鸟巢采集器](http://www.newcrawler.com/zh-cn/index.html)

[实时监控1000家中国企业的新闻动态](https://github.com/lazycatzh/news_feed)

[拉钩 | 豆瓣 | 链家爬虫项目的合集](https://github.com/HunterChao/Crawler)
https://scrapy.org/

github地址 :https://github.com/Niracler/nirScraper.git
