from pprint import pprint

from vizontele.crawler import Crawler

episode = Crawler('dizimag', 'supernatural', 12, 22).get_sources()

pprint(episode)
