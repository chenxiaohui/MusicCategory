#!/usr/bin/python
#coding=utf-8
#Filename:except.py

class ConfigException(Exception):
    def __init__(self):
        """"""
        print "config Error"

class WebExcetiption(Exception):
    def __init__(self):
        """"""
        print "Connection Error whild downloading"
