#!/usr/bin/python
# -*- coding: cp936 -*-
file_old=open('1.txt','r')
new=open('new.txt','w+')

for line in file_old:
    try:
        if '1' in line:
            read=file_old.next()
            new.write(read)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
file_old.close()
new.close()

