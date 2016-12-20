import scrapy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class IThomeSpoder(scrapy.Spider):
    name = "IThome"
    allowed_domains = ["ithome.com"]
    start_urls = [
        "http://www.ithome.com/html/digi/281845.htm",
        "http://www.ithome.com/html/android/281813.htm"
    ]

    def parse(self, response):
        #text = TextItem()
        url = response.url
        tile = response.xpath("//head/title/text()").extract()[-1]
        comtext = response.xpath("//div[@class = 'post_content']/p/text()").extract()
        filename = response.url.split("/")[-1].split(".")[-2]
        print comtext[-1]
        with open(filename, 'wb') as f:
            f.write(url + '\n')
            f.write(tile + '\n')
            for x in comtext:
                f.write(x + '\n')
