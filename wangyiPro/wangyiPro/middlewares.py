# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware(object):

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
    #拦截整个工程中所有的响应对象,一请求对应一响应
    def process_response(self, request, response, spider):
        if request.url in spider.urls:
            #就要将其对应的响应对象进行处理
            #获取了在爬虫类中定义号的浏览器对象
            bro=spider.bro   #包含动态加载出来的数据
            bro.get(request.url)

            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)

            #获取携带了新闻数据的页面源码数据
            page_text=bro.page_source    #spider.bro.current_url==request.url
            new_response=HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass