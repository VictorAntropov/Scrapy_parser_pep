import csv
import datetime as dt
from collections import defaultdict

from scrapy import Item, Spider

from pep_parse.settings import (BASE_DIR, CSV, DT_FORMAT, STATUS_SUMMARY,
                                TABLE_SUM, TOTAL, UTF)


class PepParsePipeline:
    '''Подсчитываем количество PEP по статусам и суммарное количество'''

    def __init__(self) -> None:
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider: Spider) -> None:
        self.results = defaultdict(int)

    def process_item(self, item: Item, spider: Spider) -> Item:
        self.results[item.get('status')] += 1
        return item

    def close_spider(self, spider: Spider) -> None:
        now_formated = dt.datetime.now().strftime(DT_FORMAT)
        filename = self.results_dir / f'{STATUS_SUMMARY}_{now_formated}.{CSV}'

        with open(filename, mode='w', encoding=f'{UTF}') as csvfile:
            csv.writer(csvfile, dialect=csv.unix_dialect,
                       quoting=csv.QUOTE_NONE
                       ).writerows([
                           TABLE_SUM,
                           *(self.results.items()),
                           [TOTAL, sum(self.results.values())]
                       ])
