#!usr/bin/python

row = open('row_list', 'r')
clean = open('clean_list2', 'w+')
uni = open('uni2', 'w')

for line in row:
        line=line.strip()
        line=line.strip('.1')
        line=line.strip('.2')
        clean.write(line+'\n')
        print line
clean.close()

clean = open('clean_list2', 'r')
unique = set(clean)
for line in unique:
        uni.write(line)

row.close()
clean.close()
uni.close()
