#!/usr/bin/python3
# Program to print prime number : example of functions
# this Program is also served as example of how to use yield for sequence generation
def prime(n):
    if n == 1 :
        print("{} is special number" .format(n))
        return False
    for i in range(2, n):
        if n % i == 0 :
            # print('{} is not prime : factors {} x {}'.format(n, i, n//i))
            return False
    else:
        # print("{} is prime.".format(n))
        return True

def prime_num_generator(i = 1):
    while(True):
        if prime(i) :
            yield i 
        i = i + 1

for i in prime_num_generator():
    if i > 50 :
        break
    print (i, end = ' ')
