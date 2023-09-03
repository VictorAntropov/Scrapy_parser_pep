import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, CSSSelector


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        tbody_tag = response.css(CSSSelector.TBODY).css(CSSSelector.TR)

        for tr in tbody_tag:
            pep_ref = tr.css(CSSSelector.TD).css(
                f'{CSSSelector.A}::{CSSSelector.ATTR}({CSSSelector.HREF})')
            pep_ref_get = pep_ref.get()

            if pep_ref_get is not None:
                yield response.follow(pep_ref_get, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css(f'{CSSSelector.H1}::text').get().split(' – ')

        data = {
            'number': title[0][4:],
            'name': title[1],
            'status': response.css(f'{CSSSelector.ABBR}::text').get(),
        }
        yield PepParseItem(data)
