# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DatabloggerScraperItem(scrapy.Item):
    link_from = scrapy.Field()
    link_to = scrapy.Field()

    
