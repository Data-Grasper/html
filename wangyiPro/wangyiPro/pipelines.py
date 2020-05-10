# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WangyiproPipeline(object):
    def process_item(self, item, spider):
        print("类别：" + item["title"])
        print(item["content"])
        print("时间：" + item["time"])
        print("标签：" + item["tag"])
        print("url链接：" + item["url"])
        print("评论数" + item["comments"])
        return item
