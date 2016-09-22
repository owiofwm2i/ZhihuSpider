# -*- coding: utf-8 -*-
import scrapy
#from zhihu.settings import phone_num, password
from zhihu.items import ZhihuItem
phone_num = ''
password = ''

class ZhihuspiderSpider(scrapy.Spider):
    name = "zhihuspider"
    #allowed_domains = ["http://www.zhihu.com"]
    start_urls = (
        'http://www.zhihu.com/#signin',

    )
   
    
   
    def parse(self,response):
        return scrapy.FormRequest.from_response(response,
            formdata = {'phone_num':phone_num,'password':password},
            callback = self.parse_index,
            method = "POST",
            url="https://www.zhihu.com/login/phone_num",
        )
    def parse_index(self,response):

        return scrapy.Request('https://www.zhihu.com/',callback = self.parse_homepage)
    
    

    def parse_homepage(self,response):
        divs = response.xpath('//div[starts-with(@class,"feed-item folding feed-item-hook feed-item")]')
        for div in divs:
            items = ZhihuItem()
            label = div.xpath('div[@class ="feed-main"]/div[@class= "feed-source"]/a/text()').extract()
            print label
            #items['label'] = label[0]  if label else ''
            #items['title'] = div.xpath('./div/div/div/h2[@class ="feed-title"]/a/text()').extract()[0]
            #item['author'] = div.xpath('./div/div/div/div/div/span/span[@class = "author-link"]/a/text()').extract()[0]
            yield items

    