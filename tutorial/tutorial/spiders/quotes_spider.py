import scrapy
from tutorial.items import FunplusItem
from datetime import datetime

# https://www.infoq.cn/article/qazGhIwiS2XX9hWj8QvK
class QuotesSpider(scrapy.Spider):
    name = "tutorial"
    # http://www.p7an.info/forum.php?mod=viewthread&tid=1&extra=page%3D1
    def start_requests(self):
        urls = [
        ] 

        for i in range(55087,55087+1):# 55485
            yield scrapy.Request("http://www.p7an.info/thread-{}-1-1.html".format(i),callback=self.parse)

    def parse(self, response):
        item = FunplusItem()
        htmlResult = []
        for x in scrapy.selector.Selector(response).css("td .t_f::text").extract():
            if x.strip():
                htmlResult.append(x.strip())
        item['Title'] = scrapy.selector.Selector(response).css("title::text")[0].extract()
        item['Content'] = htmlResult
        item['RawUrl'] = scrapy.selector.Selector(response).css("link::attr(href)")[0].extract()
        item['OriId']=item['RawUrl'].split('-')[1]
        strHappyDate=scrapy.selector.Selector(response).css('div .authi em::text')[0].extract().replace('发表于 ','').strip()
        item['HappyDate']=datetime.strptime(strHappyDate, '%Y-%m-%d  %H:%M')
        yield item