#!/usr/bin/python
# -*- coding: cp936 -*-
file_old=open('360_accessions','r')
file_1=open('abrc_plantCell','r')
file_2=open('1001_accessions','r')
new=open('new.txt','w+')

##data_old=file_old.read()
list_1=( file_1.read() ).split()
list_2=( file_2.read() ).split()

for line in file_old:
    ##print 'old',line
    data_line=line.strip()
    line=line.strip() ##replace('\n','')
    if data_line in list_1:
        line=line + '\tabrc_plantCell'
    if data_line in list_2:
        if data_line in list_1:
            line=line + '\t'
        else:
            line=line + '\t\t'
        line=line + '1001_accessions'
    ##print line
    line=line+'\n'
    new.write(line)

file_old.close()
file_1.close()
file_2.close()
new.close()
