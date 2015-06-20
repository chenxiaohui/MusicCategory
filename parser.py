#!/usr/bin/python
#coding=utf-8
#Filename:parser.py

import httplib2
import config
from BeautifulSoup import BeautifulSoup          # For processing HTML
import exception
import re
from collections import Counter

def download_url(filename):
    """"""
    words={}
    request = httplib2.Http()
    if not config.url_pattern:
        raise config.ConfigException

    url = config.url_pattern%(filename.replace(' ',''))
    try:
        response, content = request.request(url)
    except exception.WebException , e:
        raise
    if response.status == 200:
        try:
            soup = BeautifulSoup(content)
            song_list = soup.find(monkey="song-list")
            if song_list:
                html_tags = song_list.findAll("span", {"class":"song-title"})
                html_tags.extend(song_list.findAll("span", {"class":"singer"}))
                words = [tag.text for tag in html_tags]
        except Exception , e:
            raise

    return words

def parse(filename):
    """"""
    wordcount ={}
    try:
        words = download_url(filename)
    except Exception , e:
        raise
    if words:
        words = [re.sub(r'[-()]', '', word) for word in words]
        words_split = []
        for word in words:
            words_split.extend(word.split())
        wordcount = Counter(words_split)
    return wordcount

