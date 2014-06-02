#!/usr/bin/python
#coding=utf-8
#Filename:music.py
import sys,os
import parser
import config
import shutil

def dected_base_dir():
    """"""
    if not config.base_dir:
        raise config.ConfigException
    if not os.path.exists(config.base_dir):
        try:
            os.mkdir(config.base_dir)
        except Exception , e:
            print "failed to create dir"
            raise e

def print_result(word_result):
    """"""
    result_list = result.items()
    result_list = sorted(result_list, key=lambda x:x[1], reverse=True)
    idx = 0
    for (word, times) in result_list:
        print idx, word
        idx+=1

def category_file(file_path, dest_dir):
    """"""
    if not config.base_dir:
        raise config.ConfigException
    dest_path = os.path.join(config.base_dir, dest_dir)
    if not os.path.exists(dest_path):
        try:
            os.mkdir(dest_path)
        except Exception , e:
            print "failed to create dir"
            raise e

    copy_cmd = "cp '%s' %s"% (file_path, dest_path)
    print copy_cmd
    shutil.copy(filepath, dest_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Help: python music.py <filename>"
    else:
        try:
            dected_base_dir()
        except Exception , e:
            print "failed to dected base dir"

        filepath = sys.argv[1].decode("utf-8")
        fpath, fname = os.path.split(filepath)
        filename, ext=os.path.splitext(fname)
        result = parser.parse(filename)
        print_result(result)
        while True:
            try:
                option = int(raw_input("select a most probably one: \n"))
            except Exception , e:
                print "Input data error"
                continue
            if option >= 0 and option < len(result):
                try:
                    category_file(filepath, result.items()[option][0])
                except Exception , e:
                    print "failed to copy file to category"
                    raise e
                finally:
                    break
