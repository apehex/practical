# -*- coding: utf-8 -*-

"""
============
Web scraping
============

Utilities to extract meaningful information from the web.

Examples
--------
    >>> 
"""

from __future__ import division, print_function, absolute_import

from bs4 import BeautifulSoup

from practical.types import *

#####################################################################
# TEXT EXTRACTION
#####################################################################
def extract_text_from_html_script(html):
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text