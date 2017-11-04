d = {}

import re, sys, os
file = open('file.html', 'r')

text = file.read()

result = re.sub(r'(\<(/?[^>]+)>)', '', text)
result = re.findall(r"([a-zA-Z-']+)", result)

lsWord = {}
for key in result:
    key = key.lower()
    if key in lsWord:
        value = lsWord[key]
        lsWord[key]=value+1
    else:
        lsWord[key]=1

sorted_keys = sorted(lsWord, key = lambda x: int(lsWord[x]), reverse=True)

for key in sorted_keys:
    s = str("{0} {1}").format(key,lsWord[key])
    print(s)
file.close()