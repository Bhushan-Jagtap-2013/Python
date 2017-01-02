#!/usr/bin/python3


# In python create variables inside class with underscore "_" infornt of it
# eg. _variblename
# This allows to distiguish attribute varible of class from other
# So that we can not modify them accidently outsize the class methods

class Dictionary_variable:
    def __init__(self, **kwargs):
        self._variable = kwargs

    def setter(self, name, value):
        self._variable[name] = value

    def getter(self, name):
        return self._variable.get(name, None)

def main():
    o = Dictionary_variable(feet = 10)
    print(o.getter('feet'));
    o.setter('feet', 20)
    print(o.getter('feet'));
    
if __name__ == '__main__': main()
