from pprint import pprint

from vizontele.crawler import Crawler

episode = Crawler('dizipub', 'legion', 1, 2).get_sources()

pprint(episode)
