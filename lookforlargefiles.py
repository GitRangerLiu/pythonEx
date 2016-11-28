#https://docs.python.org/2.7/library/stat.html

import os
import sys
import stat

top = 'E:\MyProjects\pythonEx'
dic = []
#Put the file found in the list
def put_file_size(filedir):
    dirattr = os.stat(filedir)
    dic.append([filedir, dirattr.st_size])
    
#Sort by the file size
def sort_by_value(dic):
    dic.sort(key = lambda x: x[1], reverse=True)

#Walk the directories below the top directory
def walktree(top, put_file_size):
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if stat.S_ISDIR(mode):
            walktree(pathname, put_file_size)
        elif stat.S_ISREG(mode):
            put_file_size(pathname)
        else:
            print 'unknown file type %s' % pathname



if __name__ == '__main__':
    walktree(top, put_file_size)
    sort_by_value(dic)
    for item in dic:
        print item

