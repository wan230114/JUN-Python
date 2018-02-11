#!/usr/bin/python
# -*- coding: cp936 -*-
##本程序会遇到StopIteration错误，既读取最后一行的下一行不存在
file_old=open('1.txt','r')
new=open('new.txt','w+')
for line in file_old:
    if '1' in line:
        read=file_old.next()
        new.write(read)
file_old.close()
new.close()

