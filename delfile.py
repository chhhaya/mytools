#coding:utf8
import glob
import os

def fun(path):
    """
    删除指定目录下除.cs和.py之外的其他文件，并删除所有空目录
    """
    for fn in glob.glob(path + os.sep + '*'):
        if os.path.isdir(fn):
            if len(os.listdir(fn)) == 0:
                os.rmdir(fn)
                print('empty:%s' % fn)
            else:
                fun(fn)
        else:
            tmps = os.path.splitext(fn)[1][1:]
            if tmps != 'cs' and tmps != 'py':
                os.unlink(fn)
                print('delete file %s' % fn)



fun('.')