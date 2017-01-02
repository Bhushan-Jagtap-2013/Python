#!/usr/bin/python3
# Exmaple of class with generator function

class Generator():
    def __init__(self, *args):
        num_args = len(args)
        if num_args < 1:
            raise TypeError("We need arguments in format start, end, step")
        elif num_args == 1:
            self.start = 0
            self.step = 1
            self.end = args[0]
        elif num_args == 2:
            (self.start, self.end) = args
            self.step = 1
        elif num_args == 3:
            (self.start, self.end, self.step) = args
        else:
            raise TypeError("More Number of argumens than expected: {}".format(args))

    def serise(self):
        i = self.start
        while(i <= self.end):
            yield i
            i = i + self.step

#g = Generator(5, 10)
#g = Generator(5)
#g = Generator(10, 20, 2)
#g = Generator()
g = Generator(1,2,3,4)
for i in g.serise():
    print(i)
