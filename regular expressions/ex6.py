import re
def getStrings(fileName, template):
    file = open(fileName, 'r')
    lines = file.read()
    result = re.findall(template, lines)
    file.close()
    return len(result)

print(getStrings("file.html", "Borat"))