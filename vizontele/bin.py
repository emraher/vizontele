import json
import os
import sys
import argparse
import signal

import subprocess
import pget

from vizontele import crawler
from vizontele.crawler import Crawler


def readable_bytes(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def download_callback(downloader):
    percent = ("{0:.1f}")\
        .format(100 * (downloader.total_downloaded / float(downloader.total_length)))
    filled_length = int(80 * downloader.total_downloaded / downloader.total_length)
    bar = '█' * filled_length + '-' * (80 - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (downloader.readable_speed, bar, percent, ''))
    sys.stdout.flush()
    # Print New Line on Complete
    if downloader.total_downloaded == downloader.total_length:
        sys.stdout.write('\n')
    """
    sys.stdout.write("\r                                                                                            ")
    sys.stdout.write("\rDownloading %s [%s%%] [%s/sec] %s %s" %
                     (downloader.file_name,
                      round(100 * (float(downloader.total_downloaded) / downloader.total_length), 2),
                      downloader.readable_speed,
                      readable_bytes(downloader.total_downloaded),
                      readable_bytes(downloader.total_length)))
    sys.stdout.flush()
    """


def run(argv):
    def callback(episode):
        out_text = json.dumps(episode)
        if args.output is not None:
            with open(args.output, 'w') as f:
                f.write(out_text)
        else:
            from pprint import pprint
            pprint(episode)
            print '\n\n'

        if args.vlc is not None:
            subprocess.call([args.vlc, '-f', episode['video_links'][-1]['url']])

        if args.download:
            dirname = os.path.join(os.getcwd(), episode['dizi_url'], str(episode['season']), str(episode['episode']))

            if not os.path.isdir(dirname):
                os.makedirs(dirname)

            if os.path.isdir(dirname):
                videoname = os.path.join(dirname, 'Video.mp4')
                downloader = pget.Downloader(episode['video_links'][-1]['url'], videoname, 16)
                print("Downloading: %s" % videoname)
                downloader.subscribe(download_callback, 256)
                downloader.start_sync()
                if len(episode['subtitle_links']) > 0:
                    for sub in episode['subtitle_links']:
                        subname = os.path.join(dirname, sub['lang'] + '.vtt')
                        downloader = pget.Downloader(sub['url'], subname, 1)
                        print("Downloading: %s" % subname)
                        downloader.subscribe(download_callback, 256)
                        downloader.start_sync()

    parser = argparse.ArgumentParser(description='Vizontele - Watch, Download, Crawl TV Series')
    parser.add_argument('dizi', metavar='Family Guy', help='Name of the TV Show', type=str)
    parser.add_argument('season', metavar='12', help='Season number', type=int)
    parser.add_argument('episode', metavar='15', help='Episode number', type=int)
    parser.add_argument('--site', metavar='dizilab', help='Website to crawl', type=str, default='sezonlukdizi',
                        choices=crawler.dizisites.keys())
    parser.add_argument('-o', dest="output", metavar='output.json', help='Output file for crawling result', type=str)
    parser.add_argument('--vlc', metavar='/vlc/binary/destination', help='Link VLC executable to play this episode',
                        type=str)
    parser.add_argument('-d', dest="download", help='If given, episode is downloaded with highest quality.',
                        action='store_true', default=False)

    try:
        args = parser.parse_args(argv)
    except:
        return

    c = Crawler(args.site, callback, args.dizi, args.season, args.episode)
    c.run()


def main():
    if sys.stdin.isatty():
        run(sys.argv[1:])
    else:
        argv = sys.stdin.read().split(' ')
        run(argv)
