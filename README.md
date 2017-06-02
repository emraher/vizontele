# Vizontele

Vizontele is a web crawler specialized for Turkish Tv Show sites. It supports many well-known sites like SezonlukDizi, Dizilab, Dizibox etc.

**Currently, many websites that are supported by vizontele are having source problems with their cloud services. Hopefully they will resolve this issue.**

## Install

Vizontele is hosted at PyPI, so you can simply install the latest released package by
```
pip install vizontele
```

You can import vizontele as python module in your python applications or use the CLI to extract information from anywhere.
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