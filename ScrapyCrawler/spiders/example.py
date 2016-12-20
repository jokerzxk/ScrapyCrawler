# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class ExampleSpider(scrapy.Spider):
    name = "ithomeSipder"
    allowed_domains = ["ithome.com"]
    start_urls = ["http://www.baidu.com"]
    #rules = [Rule(LinkExtractor(allow=['/html/(\w+)/(\d+)\.htm']), 'parse')]

    def parse(self, response):
        text = TextItem()
        text['url'] = response.url
        text['name'] = response.xpath("//div[@class='nlst']//span[@class='title']/a[@target='_blank']/a/text()").extract()

        return text



#http://www.ithome.com/html/auto/281707.htm
#http://www.ithome.com/html/it/281666.htm