# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhongtroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    acreage = scrapy.Field()
    # published = scrapy.Field()
    description = scrapy.Field()
    phone_number = scrapy.Field()
    package = scrapy.Field()
    category = scrapy.Field()
    public_date = scrapy.Field()
    expired_date = scrapy.Field()
    ad_type = scrapy.Field()
    target_renter = scrapy.Field()
    pass
