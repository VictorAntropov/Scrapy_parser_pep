import csv
import datetime as dt
from collections import defaultdict
from pep_parse.settings import (BASE_DIR, DT_FORMAT, STATUS_SUMMARY,
                                CSV, UTF, TABLE_SUM, TOTAL)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item.get('status')] += 1
        return item

    def close_spider(self, spider):
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
