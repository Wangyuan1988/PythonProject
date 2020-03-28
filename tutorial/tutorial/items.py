# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FunplusItem(scrapy.Item):
    Title=scrapy.Field()
    Content=scrapy.Field()
    OriId=scrapy.Field()
    RawUrl=scrapy.Field()
    HappyDate=scrapy.Field()
    pass
