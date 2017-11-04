import re, sys
file = open('file.html', 'r')

text = file.read()

result = re.sub(r'(\<(/?[^>]+)>)', '', text)


for line in result:
    sys.stdout.write(line)

file.close()
