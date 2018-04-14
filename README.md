# scraper
采集数据部分的实现

        self.rule.url = self.start_urls[0]
        self.rule.loop_rule = "//div[contains(@class, article)]"
        self.rule.title_rule = "null"
        self.rule.content_rule = "a[contains(@class, contentHerf)]/text()"
        self.rule.type_rule = "null"
        self.rule.url_rule = "a[contains(@class, contentHerf)]/@href"
        self.rule.table_name = "qiushibaike"