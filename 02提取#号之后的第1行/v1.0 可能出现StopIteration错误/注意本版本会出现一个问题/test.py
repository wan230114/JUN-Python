#!/usr/bin/python
# -*- coding: cp936 -*-
##�����������StopIteration���󣬼ȶ�ȡ���һ�е���һ�в�����
file_old=open('1.txt','r')
new=open('new.txt','w+')
for line in file_old:
    if '1' in line:
        read=file_old.next()
        new.write(read)
file_old.close()
new.close()

