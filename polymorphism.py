#!/usr/bin/python3

# Simple example of polymorphism

class A:
    def method(self):
        print("Inside A")

class B:
    def method(self):
        print("Inside B")

def main():
    a = A()
    b = B()
    for o in (a,b):
        o.method()      # accessing interface irrespective of class type

if __name__ == "__main__": main()
