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
        if self.site in dizisites.keys():
            self.crawler = dizisites[self.site]()
        elif self.site == '':
            self.crawler = None

        self.episode = {"dizi_url": vizontele.slugify(dizi_url),
                        "season": season_number,
                        "episode": episode_number}

    def run(self):
        if self.crawler is not None:
            self.crawler.get_sources(self.episode, self.callback)
        else:
            # Site is not specified, lets check them all
            for site in dizisites.keys():
                self.crawler = dizisites[site]()
                self.crawler.get_sources(self.episode)
                if 'video_links' in self.crawler.episode and len(self.crawler.episode['video_links']) > 0:
                    self.callback(self.crawler.episode)
                    return

            self.callback(self.episode)

