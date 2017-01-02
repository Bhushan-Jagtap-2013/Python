#!/usr/bin/python3

class Sample:
    def __init__(self, v):
        self._var = v;
        print("Inside contructor")
    def display(self):
        print("Value of variable :", self._var)

def main():
    o = Sample(10)
    o.display()

if __name__ == "__main__": main()
