file = open('month.txt', 'r')

list = []
for line in file:
    list.append(line.strip())

list.sort()

for line in list:
    print(line)

outFile = open('sorted_month.txt','w')

for line in list:
    outFile.write(line + '\n')

file.close()
outFile.close()