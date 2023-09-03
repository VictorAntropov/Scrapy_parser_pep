import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        tbody_tag = response.css('tbody').css('tr')

        for tr in tbody_tag:
            pep_ref = tr.css('td').css('a::attr(href)').get()

            if pep_ref is not None:
                yield response.follow(pep_ref, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().split(' – ')

        data = {
            'number': title[0][4:],
            'name': title[1],
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
