import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS_SUMMARY = 'status_summary'
TABLE_SUM = ('Статус', 'Количество')
TOTAL = 'Total'


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
        filename = self.results_dir / f'{STATUS_SUMMARY}_{now_formated}.csv'

        with open(filename, mode='w', encoding='utf-8') as csvfile:
            csv.writer(csvfile, dialect=csv.unix_dialect,
                       quoting=csv.QUOTE_NONE
                       ).writerows([
                           TABLE_SUM,
                           *(self.results.items()),
                           [TOTAL, sum(self.results.values())]
                       ])
