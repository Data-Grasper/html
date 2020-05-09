# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class WangyiproItem(scrapy.Item):
    head = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    time=scrapy.Field()
    pass
