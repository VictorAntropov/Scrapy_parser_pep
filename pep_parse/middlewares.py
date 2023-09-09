from typing import Iterable

from scrapy import Item, Spider, http, signals
from scrapy.crawler import Crawler


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self,
                             response: http.Response, spider: Spider) -> None:
        return None

    def process_spider_output(self, response: http.Response,
                              result: Iterable[Item], spider: Spider
                              ) -> Iterable[Item]:
        for i in result:
            yield i

    def process_spider_exception(self, response: http.Response,
                                 exception: Exception, spider: Spider) -> None:
        pass

    def process_start_requests(self, start_requests: Iterable[http.Request],
                               spider: Spider) -> Iterable[http.Request]:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: http.Request, spider: Spider) -> None:
        return None

    def process_response(self, request: http.Request, response: http.Response,
                         spider: Spider) -> http.Response:
        return response

    def process_exception(self, request: http.Request,
                          exception: Exception, spider: Spider) -> None:
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
