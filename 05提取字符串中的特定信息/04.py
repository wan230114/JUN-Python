#!usr/bin/python

fasta_old = open('seq', 'r')
fasta_new = open('seq_new.txt', 'w+')
s=0
for line in fasta_old:
    if '>lcl|' in line:
        data = line.replace('_cds','|')
        list=data.split('|')
        print list[1]
        fasta_new.write(list[1]+'\n')
fasta_old.close()
fasta_new.close()
