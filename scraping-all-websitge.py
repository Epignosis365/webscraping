#!/usr/bin/ python
# -*- coding:Utf8 -*-
__author__ = 'Francisco Senda Buiti'

import os
import sys
import importes as im
from pywebcopy import save_webpage


download_folder = './dataSets/'
#url = 'https://www.seloger.com/'
url = "https://openclassrooms.com/fr/paths"
mt = im.Methodes(url);

file_name = mt.fileterUrl()
print(file_name)

kwargs = {'bypass_robots': True, 'project_name': file_name}
save_webpage(url, download_folder, **kwargs)

mt = im.Methodes(url);
print(mt.dataset())

#Full documentation
#https://pypi.org/project/pywebcopy/