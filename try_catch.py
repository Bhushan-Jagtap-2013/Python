#!/usr/bin/python3
# Example of try catch
try:
    f = open('xyz')
    print(f.readlines())
except IOError as e:
    print('Someting is wrong : {}'.format(e))
print("Rest of the code")
