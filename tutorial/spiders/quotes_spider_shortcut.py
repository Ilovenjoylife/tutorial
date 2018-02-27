# -*- coding: utf-8 -*-
#spider的快捷方式

import scrapy

class QuotesSpiderShortcut(scrapy.Spider):
    name = 'quotes_shortcut'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes_shortcut-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
