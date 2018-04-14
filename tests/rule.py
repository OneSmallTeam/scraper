# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:12345678@niracler.com:3306/info_db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()


# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()


# 关于爬取规则的类
class Rule(Base):
    __tablename__ = '_rule'

    id = Column(Integer, primary_key=True)
    table_name = Column(String)
    url = Column(String)
    loop_rule = Column(String)
    title_rule = Column(String)
    content_rule = Column(String)
    url_rule = Column(String)
    type_rule = Column(String)


rule = session.query(Rule).filter(Rule.id == '1').one()
# 打印类型和对象的name属性:
print('type:', type(rule))
print('name:', rule.url)

# 关闭Session:
session.close()
