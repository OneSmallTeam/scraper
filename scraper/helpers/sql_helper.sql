# 用户表的建立
CREATE TABLE IF NOT EXISTS _user (
  id      BIGINT(7) NOT NULL AUTO_INCREMENT,
  name    VARCHAR(50),
  created TIMESTAMP          DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

# 规则表的建立
CREATE TABLE IF NOT EXISTS _rule (
  id           BIGINT(7)    NOT NULL AUTO_INCREMENT,
  author       BIGINT(7)    NOT NULL,

  url          VARCHAR(200) NOT NULL,
  table_name   VARCHAR(50)  NOT NULL,

  loop_rule    VARCHAR(200)          DEFAULT 'null',
  title_rule   VARCHAR(200)          DEFAULT 'null',
  content_rule VARCHAR(200)          DEFAULT 'null',
  url_rule     VARCHAR(200)          DEFAULT 'null',
  type_rule    VARCHAR(200)          DEFAULT 'null',

  content_url  VARCHAR(200)          DEFAULT 'null',
  parse        INT                   DEFAULT 1,               #爬取所用parse
  type         VARCHAR(50)           DEFAULT 'article',       #爬取的类型

  created      TIMESTAMP             DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES _user (id)
);

# 添加一个用户
INSERT INTO _user (name) VALUES (
  'niracler'
);

# 添加一条规则
INSERT INTO _rule (author, url, table_name, loop_rule, title_rule, content_rule, url_rule, type_rule) VALUES (
  1,
  'https://stackoverflow.com',
  'stackoverflow',
  '//div[contains(@class,''question-summary narrow'')]',
  'div/h3/a/text()',
  '//abc',
  'div/h3/a/@href',
  'div/div/a/text()'
);

