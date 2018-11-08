# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class GenipSpider(Spider):
	name = 'genip'
	allowed_domains = ['www.sslproxies.org']
	start_urls = ['http://www.sslproxies.org']

	def parse(self, response):

		dats = response.xpath('//tbody/tr')

		ipaddr = []

		for dat in dats:
			tda = dat.xpath('.//td/text()').extract()
			proxy = tda[0] + ':' + tda[1]
			ipaddr.append(proxy)
		
		file = open("ipaddr.txt", "a")

		for ipc in ipaddr:
			file.write(ipc+'\n')

		file.close()

		



