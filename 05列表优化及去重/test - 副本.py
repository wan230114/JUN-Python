#!usr/bin/python
# -*- coding: cp936 -*-


##row = open('row_list', 'r')
##
##for a in row:
####    a=a.strip()
##    a = a.strip('.1')
####    a = a.strip('.1')
##    print a
##
####运行完后直接print a,发现末尾存在换行符，所以失败
##

a='1.AF192486.1\n12211.1\n1222344112.111111111....'
print a.strip('.1')
