import re

file = open('C:\Users\\boris\\Documents\\py\\text.txt')

for line in file:
    print line
    result = re.findall(r'\d\d rub\. \d\d kop\.', line)
    print result