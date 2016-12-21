#!/usr/bin/python3

# program to print binary value and slice operator

list = []
list[:] = range(0,100)
print(list)


for i in list[0:16]:
    print ("{} in binary {:08b}".format(i, i))
