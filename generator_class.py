#!/usr/bin/python3
# Exmaple of class with generator function

class Generator():
    def __init__(self, a, b):
        self.a = a;
        self.b = b;
    def serise(self):
        while(True):
            yield self.a
            self.a = self.a + self.b

g = Generator(0, 5)
for i in g.serise():
    if i > 25:
        break
    print(i)
