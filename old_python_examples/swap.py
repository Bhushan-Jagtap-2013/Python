#!/usr/bin/python3
def main():
    a, b = 1, 2
    c = "bhushan"
    print("Before : ", a, b)
    a, b = b, a
    print("After : ", a, b)
    print("type of a and b and c: ", type(a), type(b), type(c))
if __name__ == "__main__": main()
