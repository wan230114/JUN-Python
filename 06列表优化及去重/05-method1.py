#!usr/bin/python

row = open('row_list', 'r')
clean = open('clean_list', 'w+')
uni = open('uni', 'w')

for line in row:
        new_line=''
        for line1 in line.strip():
                if line1=='.':break
                new_line=new_line+line1
        clean.write(new_line+'\n')
        print new_line
        
clean.close()

clean = open('clean_list', 'r')
unique = set(clean)
for line in unique:
        uni.write(line)

row.close()
clean.close()
uni.close()
