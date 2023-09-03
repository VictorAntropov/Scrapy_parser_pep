import scrapy


class PepParseItem(scrapy.Item):
    '''Кастомный класс PepParseItem'''
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
