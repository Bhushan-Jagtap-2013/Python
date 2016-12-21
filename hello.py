#!/usr/bin/python3
print("Hello World !")


# if example

a, b = 3, 6
if a > b :
    print('a = {} is greater than b = {}' .format(a, b))
else :
    print('b = {} is greater than a = {}' .format(b, a))

print("true foo" if a > b else "false foo")


# While example
a, b = 0, 1
while (b < 50) :
    print(b)
    a, b = b, a + b

#for example

f = open('hello.py')
for line in f.readlines():
	print(line)

