#!/usr/bin/python
# -*- coding: cp936 -*-
file_old=open('file_old.txt','r')
file_table=open('file_table.name','r')
new=open('new.txt','w+')

##��ʽ��Ϊ��������
table_all = (file_table.read()).split( )

##����data[]
table_n = 0
table_len = len(table_all)
data = []
data_mean = []
while ( table_n < table_len ):
##    s=''.join(table_all[table_n])  ##��һ���ƺ�������
    s_all = table_all[table_n]
    if not(table_n%2):
        data.append(s_all)
    if table_n%2:
        data_mean.append(s_all)
    table_n = table_n + 1

##����table{}�ֵ�
table = dict(zip(data,data_mean))

##�����滻
line = file_old.read()
m=int(len(table))
n=0
while(n < m):
##        s = ''.join(data[n])  ##��һ���ƺ�������
        s = data[n]
        n=n+1
        if s in line:  ##if table in line:
                line = line.replace(s,table[s])

new.write(line)

file_old.close()
new.close()

