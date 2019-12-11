#!/usr/bin/ python
# -*- coding:Utf8 -*-
__author__ = 'Francisco Senda Buiti'

import re


class Methodes(object):
    def __init__(self, url):
        self.url = url
    
    def dataset(self):
        return self.url
    
    def fileterUrl(self):
        url = self.url            
        url = url.replace("https://www.","")
        url = url.replace("http://www.","")
        url = url.replace(".com","")
        url = url.replace("/","")
        return url
