import re

def getStrings(fileName, template):
    file = open(fileName, 'r')
    lines = file.read()
    lines = re.split(r'\n', lines)

    n = len(lines)
    for i in range(n):
        if (re.search(template, lines[i]) != None):
            print(lines[i])
    file.close()
    pass

getStrings("file.html", "Borat")