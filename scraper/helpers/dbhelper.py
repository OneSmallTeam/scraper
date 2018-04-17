import pymysql
from scrapy.utils.project import get_project_settings  # 导入seetings配置

from scraper.helpers.rule import Rule


class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息

        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    # 连接到mysql，不是连接到具体的数据库
    def connectMysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               # db=self.db,不指定数据库名
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

    # 连接到具体的数据库（settings中设置的MYSQL_DBNAME）
    def connectDatabase(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

        # 创建数据库

    def createDatabase(self):
        '''因为创建数据库直接修改settings中的配置MYSQL_DBNAME即可，所以就不要传sql语句了'''
        conn = self.connectMysql()  # 连接数据库

        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)  # 执行sql语句
        cur.close()
        conn.close()

    # 创建表
    def createTable(self, sql):
        conn = self.connectDatabase()
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    # 插入数据
    def insert(self, sql, *params):  # 注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn = self.connectDatabase()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

    # 更新数据
    def update(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

    # 删除数据
    def delete(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def select(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data


'''测试DBHelper的类'''


class TestDBHelper():
    def __init__(self):
        self.dbHelper = DBHelper()

    # 测试创建数据库（settings配置文件中的MYSQL_DBNAME,直接修改settings配置文件即可）
    def testCreateDatebase(self):
        self.dbHelper.createDatabase()

    # 测试创建表的函数
    def testCreateTable(self, table_name):
        sql = "create table IF NOT EXISTS %s(" \
              "id int primary key auto_increment," \
              "title varchar(500) unique ," \
              "content TEXT," \
              "url varchar(200)," \
              "type varchar(50)," \
              "created TIMESTAMP DEFAULT CURRENT_TIMESTAMP" \
              ")" % table_name
        self.dbHelper.createTable(sql)

    # 查找信息的函数
    def testSelect(self, table_name, table_id):
        sql = "SELECT * FROM %s WHERE id=%s" % (table_name, table_id)
        data = self.dbHelper.select(sql)
        return data

    # 获得具体的爬取规则字典
    def getRule(self, rule_id):
        rule_info = self.testSelect("_rule", rule_id)  # 找到爬取规则
        print(rule_info)

        # 将爬取规则放到规则对象
        rule = Rule()
        rule.url = rule_info[2]
        rule.table_name = rule_info[3]
        rule.loop_rule = rule_info[4]
        rule.title_rule = rule_info[5]
        rule.content_rule = rule_info[6]
        rule.url_rule = rule_info[7]
        rule.type_rule = rule_info[8]
        rule.type = rule_info[10]

        self.testCreateTable(rule.table_name)

        return rule  # 返回爬取规则

    # 获得具体的爬取规则字典
    def setRule(self, rule):
        sql = "insert into _rule (" \
              "url, table_name, loop_rule, title_rule, content_rule, url_rule, type_rule,type" \
              ") values(%s,%s,%s,%s,%s,%s,%s,%s)"

        params = (
            # 将爬取规则放到规则对象
            rule.url,
            rule.table_name,
            rule.loop_rule,
            rule.title_rule,
            rule.content_rule,
            rule.url_rule,
            rule.type_rule,
            rule.type
        )
        self.dbHelper.insert(sql, *params)


dbHelper = TestDBHelper()

if __name__ == "__main__":
    rule = dbHelper.getRule(1)
    # rule = testDBHelper.testSelect("_rule", 1)
    # print(rule)
    # testDBHelper.testCreateTable(table_name="readhub")
    # testDBHelper.testCreateDatebase()
    # testDBHelper.testCreateDatebase()  # 执行测试创建数据库
    # testDBHelper.testCreateTable()  # 执行测试创建表
    # testDBHelper.testInsert()  # 执行测试插入数据
    # testDBHelper.testUpdate()  # 执行测试更新数据
    # testDBHelper.testDelete()  # 执行测试删除数据
