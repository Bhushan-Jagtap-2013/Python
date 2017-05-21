#!/usr/bin/python3
# Conditional statement in python

a, b = 1, 1
if a == b:
    print("Both are equal")
elif a > b:
    print("a is bigger")
else:
    print("b is bigger")

str = "false" if a > b else "true"
print(" Value of str is :", str)
