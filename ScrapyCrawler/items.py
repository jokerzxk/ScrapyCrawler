# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
class ScrapycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
'''

class TextItem(scrapy.Item):
    url = scrapy.Field()
    tile = scrapy.Field()
    #context = scrapy.Field()
