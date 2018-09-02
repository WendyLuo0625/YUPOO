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
                'update_time': repository.xpath('.//div/relative-time/@datetime').extract_first() 
            })
            yield item
