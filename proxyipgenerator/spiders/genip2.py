# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class Genip2Spider(Spider):
	name = 'genip2'
	allowed_domains = ['classic.scraperwiki.com']
	start_urls = ['https://classic.scraperwiki.com/scrapers/hide_my_ass_proxy_list_ip_8']

	def parse(self, response):
		file = open("ipaddr.txt", "a")

		rows = response.xpath('//tbody/tr')
		
		for row in rows:
			data = row.xpath('.//td/text()').extract()
			proxy = data[-2]+':'+data[-1]
			file.write(proxy+'\n')

		file.close()
