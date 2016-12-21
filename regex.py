#!/usr/bin/python3
import re
f = open('sample.regex.txt')

for line in f:
    match = re.search('name|Ram', line)
    if match:

        # here we have used line's replce function to replce match string
        # instead we can search and replace we re's sub method re.sub(pattern,replace pattern, line)

        print(line.replace(match.group(),"####"), end='')
        print('match patter {}'.format(match.group()))


# using pre compled regex and regex's sub method

f2 = open('sample.regex.txt2')
patter = re.compile('name|ram', re.IGNORECASE)
for line in f2:
    if re.search(patter, line):
        print(patter.sub('XXX', line))
