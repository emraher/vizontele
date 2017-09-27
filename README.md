# Vizontele

Vizontele is a web crawler specialized for Turkish Tv Show sites. It supports many well-known Turkish sites like SezonlukDizi, Dizilab, Dizibox etc.

## Install

Vizontele is hosted at PyPI, so you can simply install the latest released package by
```
pip install vizontele
```
or if you like to clone the source and install the latest snapshot
```
python setup.py install
```
should work in any environment.

## Usage

In this doc and also in many modules in the code you'll come across a word called `Dizi`. This is Turkish of `Tv Series`. It exists in many site names and also easier to use in code because it is not plural like in English.

You can import vizontele as a python module in your application or use the CLI to extract information from shell.

### Usage - Module

DiziCrawler module is designed as a factory for different crawlers to many different websites. You can get a crawler and run it as

```
crawler = DiziCrawler('sezonlukdizi', 'Family Guy', 1, 2)
episode = crawler.get_sources()
# episode is a python dictionary.
```
Representations of models that are used in this module are given below

```
[Episode][Dict]
dizi_url: string
season: int
episode: int
subtitle_links: List<SubtitleLink>
video_links: List<VideoLink>

[VideoLink][Dict]
res: Resolution of video.
url: Address of video file

[SubtitleLink][Dict]
lang: Language of subtitle. tr|en
url: Address of subtitle file
kind: MimeType of subtitle. vtt|srt
```

### Usage - CLI

You can find the implementation of CLI in ```vizontele/bin.py```. It is a great source to look for example usage.
A sample use of CLI is as follows:
```
vizontele family-guy 1 1
```
This translates to => Family Guy Season 1 Episode 1

More options can be acquired by -h flag. As of now its output is:
```
Vizontele - Watch, Download, Crawl TV Series

positional arguments:
  Family Guy            Name of the TV Show
  12                    Season number
  15                    Episode number

optional arguments:
  -h, --help                    show this help message and exit
  --site dizilab                Website to crawl
  -o output.json                Output file for crawling result
  --vlc /vlc/binary/destination Link VLC executable to play this episode
  -d                            If given, episode is downloaded with highest quality.

```

---

![Is Zeki Muren going to see us too?](https://img-s1.onedio.com/id-582cd68657c9e22156fd3b86/rev-0/w-500/s-f5f001388833892f0bb5d5b7f0cf71a6444c11cf.gif)
