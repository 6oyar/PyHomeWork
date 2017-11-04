import re

def getStrings(fileName):
    file = open(fileName, 'r')
    lines = file.read()
    result = re.findall(r'<a \w+', lines)
    file.close()
    return len(result)

print(getStrings("file.html"))