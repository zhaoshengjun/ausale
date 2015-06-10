# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AusaleItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    bulk_price = scrapy.Field()
    date = scrapy.Field()
