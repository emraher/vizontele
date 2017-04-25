import copy
import json

import re
import requests

from base import BaseCrawler
from pyquery import PyQuery as pq


class DizipubCrawler(BaseCrawler):
    def __init__(self):
        BaseCrawler.__init__(self)

    def generate_episode_page_url(self):
        return "http://dizipub.com/" + self.episode['dizi_url'] + "-" + \
               str(self.episode['season']) + "-sezon-" + str(self.episode['episode']) + "-bolum"

    def after_body_loaded(self, text):
        ajax_headers = copy.copy(BaseCrawler.headers)
        ajax_headers['X-Requested-With'] = 'XMLHttpRequest'
        ajax_headers['Referer'] = self.generate_episode_page_url()

        page_dom = pq(text)
        player_address = page_dom('.object-wrapper').eq(0).find('iframe').attr('src')

        result = requests.get(player_address, headers=BaseCrawler.headers)

        if result.status_code == 200:
            self.after_sources_loaded(result.text)

    def after_sources_loaded(self, text):
        m = re.search(r'sources: (.*?) ],', text)
        match = m.group(1) + "]"

        sources = json.loads(match)

        for source in sources:
            if 'p' not in source['label']:
                source['label'] += 'p'
            video_link = {"res": source['label'], "url": source['file']}
            if source['type'] == "mp4":
                self.episode['video_links'].append(video_link)


