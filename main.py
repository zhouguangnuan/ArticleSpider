# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

__author__ = 'bobby'

import sys
import os

# /Users/zhouguangnuan/workspace/article/ArticleSpider
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "jobbole"])