from pprint import pprint

from vizontele.crawler import MovieCrawler

movie = MovieCrawler('720pizle', 'beauty-and-the-beast').get_sources()
assert len(movie['video_links']) > 0
pprint('720pizle test successful')