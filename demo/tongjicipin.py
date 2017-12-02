def processLine(line, wordCounts):
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/!,.:;{}[]|\'""":
            line = line.replace(ch, "")
    return line
filename = input('enter a filename').strip()
infile = open(filename,"r")
wordCounts = {}
for line in infile:
    processLine(line.lower(), wordCounts)
pairs = list(wordCounts.items())

items = [[x,y] for (y,x) in pairs]
items.sort()
