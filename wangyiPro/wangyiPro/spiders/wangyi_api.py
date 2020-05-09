import scrapy
import json
from selenium import webdriver
from wangyiPro.settings import WANGYI_API

class WangYiSpider(scrapy.Spider):
    name="wangyi_api"
    start_urls = ['https://news.163.com/']
def __init__(self):
     self.bro = webdriver.Chrome(executable_path='chromedriver.exe')

def start_requests(self):
    yield scrapy.Request(url=self.start_urls[0],dont_filter=True,cookies=None)

def parse(self, response):
    header = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
        'Connection': 'keep - alive',
    }
    wbdata=response.get(WANGYI_API,headers=header).text
    data = json.loads(wbdata)
    news = data['T1348648517839']
    for item in news:
        digest = item['digest']
        mtime = item['mtime']
        title = item['title']
        source = item['source']
        try:
            url = item['url']
        except:
            url = ''
        newes_data = {
            'title': title,
            '内容': digest,
            '时间': mtime,
            '来源': source,
            '链接': url,
        }
        print(newes_data)
def closed(self, spider):
            # 实现父类方法，爬虫结束时调用
        print("爬虫结束")
        self.bro.quit()