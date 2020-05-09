import scrapy
import re
import json
from selenium import webdriver
from wangyiPro.settings import WANGYI_API

class WangYiSpider(scrapy.Spider):
    name="wangyi_api"
    start_urls = ['https://news.163.com/']
    bro = webdriver.Chrome(executable_path='chromedriver.exe')
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