from pathlib import Path

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

ALLOWED_DOMAINS = [
    'peps.python.org'
]
CSV = 'csv'
FEEDS = {
    f'results/pep_%(time)s.{CSV}': {
        'format': CSV,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }

}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS_SUMMARY = 'status_summary'
TABLE_SUM = ('Статус', 'Количество')
TOTAL = 'Total'
UTF = 'utf-8'

ALLOWED_DOMAINS = ['peps.python.org']


class CSSSelector:
    TBODY = 'tbody'
    TR = 'tr'
    TD = 'td'
    H1 = 'h1.page-title'
    A = 'a'
    ABBR = 'abbr'
    HREF = 'href'
    ATTR = 'attr'
