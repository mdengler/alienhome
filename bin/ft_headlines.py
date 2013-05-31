#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from urllib import urlopen
from xml.etree.ElementTree import parse

news_url = "http://www.ft.com/home/uk"
news_url = "http://www.ft.com/rss/home/uk"

def news(url):
    data = urlopen(url)
    parsed = parse(data)
    root = "./channel/item/title"
    return [title.text for title in parsed.findall(root)]

if __name__ == "__main__":
    # fix for the below fix
    #print [(k, os.environ[k]) for k in os.environ if k.startswith("L") and k != "LS_COLORS"]
    if "LANG" not in os.environ:
        os.environ["LANG"] = "en_GB.utf8"
    # from http://wjd.nu/notes/2009#unicodeencodeerror-python-redirect-pipe
    import codecs, locale
    #print locale.getdefaultlocale()
    sys.stdout = codecs.getwriter(locale.getdefaultlocale()[1])(sys.stdout, 'replace')

    print u"\n".join(news(news_url))




