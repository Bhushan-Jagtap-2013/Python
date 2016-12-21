#!/usr/bin/python3

class FileFormat(Exception):
    pass

def main():
    filename = input("Enter file name : ")
    try:
        for line in getLines(filename):
            print(line)
    except FileFormat as e:
        print('Error on file :', e)
    except IOError as e:
        print('Error on file :', e)
    else:
        print('in else part')

def getLines(filename):
    if filename.endswith('.txt'):
        f = open(filename)
        return f.readlines()
    else:
        raise FileFormat('Unrecognized file format')

if __name__ == '__main__': main()
