#!/usr/bin/ python
# -*- coding:Utf8 -*-
__author__ = 'Francisco Senda Buiti'

import os
import sys
import urllib
import urllib.request
import importes as im
from bs4 import BeautifulSoup

if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlretriev
    
url = 'https://www.seloger.com/'
mt = im.Methodes(url);

file_name = mt.fileterUrl() + '.html'
print(file_name)

download_folder = './dataSets/' + file_name
f = urllib.request.urlretrieve(url, download_folder)

print(mt.dataset())