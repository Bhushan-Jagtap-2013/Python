#!/usr/bin/python3
class Base:
    def method1(self):
        print("Base:Method1")
    def method2(self):
        print("Base:Method2")
    def method3(self):
        print("Base:Method3")

class Derived(Base):
    def method3(self):
        super().method3()
        print("Derived:Method3")
    def method2(self):
        print("Derived:Method2")

def main():
    o = Derived()

    # Calling methods with Derived class's Object

    o.method1() # Calling method of Base class
    o.method2() # Give new defination to base class method
    o.method3() # Extend the base class's method

if __name__ == "__main__": main()

# Output
# [root@localhost Python-Examples]# ./inheritance.py 
# Base:Method1
# Derived:Method2
# Base:Method3
# Derived:Method3

