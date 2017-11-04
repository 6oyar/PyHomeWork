import re
file = open('file.html', 'r')

text = file.read()

result = re.findall(r'\w+@\w+.\w+',text)


outFile = open('mail.txt','w')
for line in result:
    outFile.write(line + '\n')

file.close()
outFile.close()