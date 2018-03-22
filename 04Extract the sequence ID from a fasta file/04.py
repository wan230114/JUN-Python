#!usr/bin/python
fasta_file = open('cer16.fa', 'r')
out_file = open('cer16.id', 'w')
for line in fasta_file:
    if line.startswith('>'):
        out_file.write(line)
out_file.close()
