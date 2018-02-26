# -*- coding: utf-8 -*-
import scrapy


class Manhui_Cloud_Spider(scrapy.Spider):
    name = "manhui"

    def start_requests(self):
        urls = [
            'http://192.168.1.108:15985/logout_top',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.pars)

    def pars(self, response):
        page = response.url.split("/")[-1]  # 这里的 [-1]表示的以'/'切分的到域名前的倒序位置，即表示从最后一位表示的是文件的后缀名'
        filename = 'manhui-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
