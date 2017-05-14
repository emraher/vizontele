from pprint import pprint

from vizontele.crawler import Crawler

episode = Crawler('sezonlukdizi', 'master of none', 2, 1).get_sources()

pprint(episode)



