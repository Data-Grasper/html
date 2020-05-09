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
        return None

    #拦截到响应对象，即下载器传递给spider的响应对象
    def process_response(self, request, response, spider):
        #request：响应对象对应的请求对象
        #response：拦截到的响应对象
        #spider：爬虫文件中对应的爬虫类实例
        if request.url in ["http://news.163.com/domestic/","http://news.163.com/world/","http://war.163.com/","http://news.163.com/air/"]:
            spider.bro.get(url=request.url)

            #将滚轮滚动到最底部
            js="window.scrollTo(0,document.body.scrollHeight)"
            spider.bro.execute_script(js)
            #如果没有获取到更多的数据，这里给浏览器一定的加载时间
            #time.sleep(3
            page_text=spider.bro.page_source
            with open("./domestic.html","w",encoding="utf8") as fp:
                fp.write(page_text)
            #自己封装response，并返回
            return HtmlResponse(url=spider.bro.current_url,body=page_text,encoding="utf-8",request=request)
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