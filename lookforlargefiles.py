#https://docs.python.org/2.7/library/stat.html

import os
import sys
import stat
import threading
import time

#top = 'D:/'
top = sys.argv[1:]
dic = []
#the number of cores of your computer
cores = 4


#Put the file found in the list
def put_file_size(filedir):
    dirattr = os.stat(filedir)
    dic.append([filedir, dirattr.st_size >> 20 ])
    
#Sort by the file size
def sort_by_value(dic):
    dic.sort(key = lambda x: x[1], reverse=True)

#Walk the directories below the top directory
path_auth = ''
def walktree(top, put_file_size):
    try:
        for f in os.listdir(top):
            path_autho = f
            pathname = os.path.join(top, f)
            mode = os.stat(pathname).st_mode
            if stat.S_ISDIR(mode):
                walktree(pathname, put_file_size)
            elif stat.S_ISREG(mode):
                put_file_size(pathname)
            else:
                print 'unknown file type %s' % pathname
    except:
        #print 'sth unexpected happened'
        pass

#print file directory
#total--the number of file directory to be printed
def print_filedir(total):
    count = 0
    print 'file directory  |  file size  | unit'
    for item in dic:
        if count < total:
            print item[0], item[1], 'M'
            count += 1

            
if __name__ == '__main__':
    top = raw_input('''Please input the directory:\n
for example,
D:/
or
D:/mydirectory/

(input 'CRTL+C' to exit)
-->''')
    entry = raw_input('Please input the number of files you want to list,\
it should be a number, like 20 or 50.(input ''CRTL+C'' to exit)\n-->')
    entry = int(entry)
    print 'Start scanning the disk, please wait a moment...\n'
    start = time.time()
    walktree(top, put_file_size)
    sort_by_value(dic)
    print_filedir(entry)
    stop = time.time()
    duration = stop - start
    print 'time cost: ', duration, 's'
    print 'Tips:\nRight click the mouse in the top of python console, click \
<Edit>--<Mark>, you can use it like a Dos window'
    input('Press ENTER to exit')

