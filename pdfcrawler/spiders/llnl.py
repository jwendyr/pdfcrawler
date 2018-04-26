# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import json
import os
#import urlparse2
from scrapy.http import Request
from scrapy.conf import settings

		
class LlnlSpider(scrapy.Spider):
	name = 'llnl'
	#allowed_domains = ['github.com','arxiv.org','cv-foundation.org']
	start_urls = ['https://www.researchgate.net/publication/247949042_Large-Scale_Synthesis_of_Uniform_Silver_Nanowires_Through_a_Soft_Self-Seeding_Polyol_Process',
		'http://pubs.acs.org/doi/abs/10.1021/nl048912c',
		'http://pubs.acs.org/doi/abs/10.1021/nn400414h',
		'http://pubs.acs.org/doi/full/10.1021/acs.nanolett.5b02582',
		'http://onlinelibrary.wiley.com/doi/10.1002/cjoc.201400518/abstract',
		'http://pubs.acs.org/doi/abs/10.1021/cr100275d',
		'http://onlinelibrary.wiley.com/doi/10.1002/anie.201100087/abstract',
		'http://pubs.acs.org/doi/abs/10.1021/acs.jpclett.5b02123',
		'https://www.researchgate.net/publication/230739689_Defining_Rules_for_the_Shape_Evolution_of_Gold_Nanoparticles',
		'http://pubs.acs.org/doi/abs/10.1021/ac0702084',
		'http://pubs.rsc.org/en/Content/ArticleLanding/2012/RA/c2ra21224b#!di-vAbstract',
		'http://www.mdpi.com/1996-1944/3/9/4626',
		'http://pubs.acs.org/doi/abs/10.1021/la050220w']

	def __init__(self):
		settings.overrides['DEPTH_LIMIT'] = 2
		
	def parse(self, response):
		# selector of pdf file.
		for href in response.xpath('//a/@href').extract():
			if href.endswith('.pdf'):
				yield Request(
					url=response.urljoin(href),
					callback=self.save_pdf
				)
			else:
				yield Request(
					url=response.urljoin(href),
					callback=self.parse
				)
				

	def save_pdf(self, response):
		""" Save pdf files """
		path = response.url.split('/')[-1]
		self.log('.pdf file found')
		self.logger.info('Saving PDF %s', path);
		with open(path, 'wb') as file:
			file.write(response.body);
