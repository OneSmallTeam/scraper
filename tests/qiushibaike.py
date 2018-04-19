from tests.monitor import Model

class Qiushibaike(Model):
    def fillMyList(self):
        print(self.soup)

if __name__ == '__main__':
    qiushibaike = Qiushibaike("http://renjian.163.com")