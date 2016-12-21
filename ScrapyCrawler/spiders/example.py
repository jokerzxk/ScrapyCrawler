# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ExampleSpider(scrapy.Spider):
    name = "ithomeSipder"
    handle_httpstatus_list = [403]
    #allowed_domains = ["ithome.com"]
    start_urls = [
        "http://www.ithome.com",
    ]
    #rules = [Rule(LinkExtractor(allow=['/html/(\w+)/(\d+)\.htm']), 'parse')]

    def parse(self, response):
        with open('ithome', 'wb') as f:
            f.write(response.body)



#http://www.ithome.com/html/auto/281707.htm
#http://www.ithome.com/html/it/281666.htm