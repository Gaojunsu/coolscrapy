import json
from time import sleep

import scrapy as scrapy

from coolscrapy.items import CoolscrapyItem


class QuotesSpider(scrapy.Spider):
    name="coolscrapy"
    allowed_domains=['androidweekly.net']
    url = 'http://androidweekly.net/issues/issue-'
    Review=270
    start_urls=[url+str(Review)]

    def parse(self,response):

        for href in response.css('table.wrapper'):
            item=CoolscrapyItem()
            re=href.css('a.article-headline::attr(href)').re(r'https://.*')
            content=href.css('p::text').extract()
            title=href.css('a.article-headline::text').extract()
            item['href']=re
            item['content']=content
            item['title']=title
            #将获取的数据交给pipeline
            yield item
        if self.Review<278:
            self.Review+=1
        yield scrapy.Request(self.url+str(self.Review),callback=self.parse)







