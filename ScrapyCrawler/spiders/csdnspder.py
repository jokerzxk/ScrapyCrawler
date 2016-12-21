import scrapy
import sys
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
reload(sys)
sys.setdefaultencoding("utf-8")


class csdnSpider(CrawlSpider):
    name = "csdnSpider"
    allowed_domains = ["csdn.net"]
    start_urls = [ "http://www.csdn.net"]#,"http://geek.csdn.net/forum/AI"]

    rules = (
        Rule(LinkExtractor(allow=('/news/detail/(\d+)',)), callback='textparse'),
        Rule(LinkExtractor(allow=('http://geek\.csdn\.net/(\w+)',)), follow='True')#callback为none时，默认follow为ture，表示匹配到的url继续跟进搜索
    )

    def pageparse(self,response):
        print response.url
        return scrapy.Request(url = response.url,callback='textparse')

    def textparse(self, response):
        dirname = response.url.split('/')[-2]
        filename = response.url.split('/')[-1]
        if os.path.exists('./%s' %dirname) is False:
            os.mkdir('./%s' %dirname)
        file = './' + dirname + '/' + filename

        title = response.xpath("//dl[@class = 'header  bor']/dd/h2/span/text()").extract()

        if len(title) is not 0:
            context = response.xpath("//div[@class = 'description markdown_views']/p/text()").extract()
            text = ''
            for x in context:
                text = text + x

            with open(file, 'wb') as f:
                f.write(title[0] + '\n')
                f.write(text)

