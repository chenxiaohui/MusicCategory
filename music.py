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
    result_list = word_result.items()
    result_list = sorted(result_list, key=lambda x:x[1], reverse=True)
    idx = 0
    for (word, times) in result_list:
        print idx, word
        idx+=1
    return result_list

def category_file(file_path, dest_dir):
    """"""
    print file_path, dest_dir
    if not config.base_dir:
        raise config.ConfigException
    try:
        #dest_path = os.path.join(config.base_dir, dest_dir)
        dest_path = "%s/%s" %(config.base_dir, dest_dir)
    except Exception , e:
        print "failed to get dest path"
        raise e
    if not os.path.exists(dest_path):
        try:
            os.mkdir(dest_path)
        except Exception , e:
            print "failed to create dir"
            raise e

    if config.del_after_copy:
        copy_cmd = "mv '%s' %s"% (file_path, dest_path)
        try:
            shutil.move(filepath, dest_path)
        except Exception , e:
            print "Error" + str(e) 
    else:
        copy_cmd = "cp '%s' %s"% (file_path, dest_path)
        shutil.copy(filepath, dest_path)

    print copy_cmd

def process_one_file(filepath):
    """"""
    fpath, fname = os.path.split(filepath)
    filename, ext=os.path.splitext(fname)
    result = parser.parse(filename)
    result.update(config.extra)
    result = print_result(result)
    try:
        option = int(raw_input("select a most probably one: \n"))
    except Exception , e:
        print "Input data error"
        raise e

    if option >= 0 and option < len(result):
        category = result[option][0].encode('utf-8')
        if category == "自定义":
            print ("请输入："),
            category = raw_input()
        if config.prompt:
            print ("Sure to copy to category %s? (Y/n)"%category)
            confirm = raw_input()
            if confirm.upper() !='Y' and confirm !='':
                return
        try:
            category_file(filepath, category)
        except Exception , e:
            print "failed to copy file to category"
            raise e

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Help: python music.py <filename|filelist>"
    else:
        try:
            dected_base_dir()
        except Exception , e:
            print "failed to dected base dir"
        del sys.argv[0]
        for filepath in sys.argv:
            print "----------------------%s----------------------"%filepath
            process_one_file(filepath)
