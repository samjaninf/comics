from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'EON'
    language = 'no'
    url = 'http://www.nettavisen.no/tegneserie/striper/'
    start_date = '2008-11-19'
    rights = 'Lars Lauvik'

class Crawler(CrawlerBase):
    history_capable_date = '2008-11-19'
    schedule = 'We'
    time_zone = 1

    def crawl(self, pub_date):
        url = 'http://pub.tv2.no/nettavisen/tegneserie/pondus/eon/%s.gif' % (
            pub_date.strftime('%d%m%y'),)
        return CrawlerResult(url)