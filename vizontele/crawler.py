import vizontele
from diziay import DiziayCrawler
from dizibox import DiziboxCrawler
from dizilab import DizilabCrawler
from dizipub import DizipubCrawler
from dizist import DizistCrawler
from sezonlukdizi import SezonlukDiziCrawler
from dizimag import DizimagCrawler

dizisites = {
    "dizilab": DizilabCrawler,
    "dizipub": DizipubCrawler,
    "sezonlukdizi": SezonlukDiziCrawler,
    "dizimag": DizimagCrawler,
    "dizibox": DiziboxCrawler,
    "diziay": DiziayCrawler,
    "dizist": DizistCrawler
}


class Crawler:
    def __init__(self, site, callback, dizi_url, season_number, episode_number):
        self.site = site
        self.callback = callback
        self.crawler = dizisites[self.site]()
        self.episode = {"dizi_url": vizontele.slugify(dizi_url),
                        "season": season_number,
                        "episode": episode_number}

    def run(self):
        self.crawler.get_sources(self.episode, self.callback)
