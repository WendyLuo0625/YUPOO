# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class SylgithubSpider(scrapy.Spider):
    name = 'sylgithub'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for repository in response.css('div#user-repositories-list ul li'):
            item =  ShiyanlougithubItem({
                'name': repository.xpath('.//div/h3/a/text()').extract_first().strip(),
                'update_time': repository.xpath('.//div/relative-time/@datetime').extract_first(),
            })
            course_url =response.urljoin(repository.xpath('.//div/h3/a/@href').extract_first())
            request = scrapy.Request(course_url, callback=self.parse_details)
            request.meta['item'] = item
            yield request

    def parse_details(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('//li/a/span[@class="num text-emphasized"]/text()').extract()[0].strip()
        item['branches'] = response.xpath('//li/a/span[@class="num text-emphasized"]/text()').extract()[1].strip()
        item['releases'] = response.xpath('//li/a/span[@class="num text-emphasized"]/text()').extract()[2].strip()
        yield item 
