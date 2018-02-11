#!/usr/bin/python
# -*- coding: cp936 -*-
file_old=open('old.txt','r')
new=open('new.txt','w+')

for line in file_old:
    if 'hits found' in line:
        if '0 hits found' in line:
            continue
        read=file_old.next()
        new.write(read)

file_old.close()
new.close()
