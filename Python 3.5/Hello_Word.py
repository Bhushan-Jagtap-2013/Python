import random

# print hello world

# comment
'''
 multi line comment
'''
print("Hello World")

name = "Bhushan"
print(name)

'''
Notes :
Data Types :
1 numbers 2 string 3 lists 4 tuples 5 dictionary
 
Operators :
+ - * / ** // %
'''

# 1. STRINGS

# Various types of String declarations
single_line_string = "\"Bhushan\\"
Multi_line_string = '''what is your name?
whats is addition of 2 + 2'''

# printing methods

combined_string = "1." + Multi_line_string + "\nAnswer :" + single_line_string + "2 + 2"
print(combined_string)

print("2.", Multi_line_string, "\nAnswer :", single_line_string, 2 + 2)

print("%s %s %s %s %d" % ("3.", Multi_line_string, "\nAnswer :", single_line_string, 2 + 2))

# No end of line
print("1st line", end="")
print("This Line is added to same line as end = \" \"")

# Print multiple times

print("Bhushan\n" * 5)

# 2. LISTS

# declare

consonants = ['x', 'y', 'z', 'p']
vowels = ['a', 'e', 'i', 'o', 'u']

print("1. consonants", consonants)

# combine lists

combined_lists = consonants + vowels
print("2.", combined_lists)

combined_lists = [consonants, vowels]
print("3.", combined_lists)

# replace and access and print

consonants[0] = 'q'
print("4.", consonants[0])
print("5.", combined_lists[0][0])
print("6.", consonants[0:2])

# functions

print("7.", consonants.count('z'))

consonants.append('b')
print("8.", consonants)

consonants.reverse()
print("9.", consonants)

consonants.remove('z')
print("10.", consonants)

consonants.insert(2, 'z')
print("10.", consonants)

consonants.sort()
print("11.", consonants)

consonants.sort(reverse=True)
print("12.", consonants)

print("13.", max(consonants))
print("14.", min(consonants))
print("15.", len(consonants))

# TUPLE
# can not be able to change value easily
my_tuple = (1, 2, 3, 4)

# Conversion between tuple and list
my_list = list(my_tuple)
my_tuple = tuple(my_list)

# we can use min max len in tuple

# DICTIONARY
# Unique key for each value
# we can not join dictionary with +

string_to_number = {'one': 1,
                    'two': 2,
                    'three': 3,
                    'four': 4,
                    'five': 6}

print("DICTIONARY")
print("1.", string_to_number)
string_to_number['one'] = 8
print("2.", string_to_number['one'])
print("3.", len(string_to_number))
print("4.", string_to_number.get('three'))
print("5.", string_to_number.values())
print("6.", string_to_number.keys())

# CONDITIONALS

print("CONDITIONALS")
if 10 > 20:  # == >= <= != and or not
    print("Greater")
elif 15 > 20:
    print("Little Greater")
else:
    print("Even More")

if ((10 < 20) and (10 > 5)):
    print("HiFi")

# LOOPS
print("\nLOOPS")

for x in range(1, 10):
    print(x, end=" ")
print("\n")

for x in consonants:
    print(x, end=" ")
print("\n")

for x in combined_lists:
    for y in x:
        print(y, end=" ")
print("\n")

# while loop we don't know in advance how many time we need to loop

print("WHILE")

rnd = random.randrange(1, 10)
while rnd != 5:
    print(rnd, end=" ")
    rnd = random.randrange(1, 10)
print("\n")

i = 0
while i < 10:
    if i % 2 == 0:
        print(i, end=" ")
    elif i == 7:
        print("B", end=" ")
        break
    else:
        i = i + 1
        print("C", end=" ")
        continue
    i = i + 1
print("\n")

# FUNCTIONS
print("FUNCTIONS")


def sum_two(num1, num2):
    s = num1 + num2
    return s


# num1 = int(sys.stdin.readline())
# num2 = int(sys.stdin.readline())
num1 = num2 = 10
total = sum_two(num1, num2)
print("1.", total)

# STRINGS FUNCTIONS

print("STRING FUNCTIONS")
sample_long_string = "0123456789"
print("1.", sample_long_string[2:5])  # from 2 to 5
print("2.", sample_long_string[-4:])  # last 4 num
print("3.", sample_long_string[:-4])  # start to except last 4
print("4.", sample_long_string[-4:] + " last 4 numbers")  # concat substring
print("5.", "character %c | decimal %d | float %.5f | string %s" % ('a', 10, 20, 'Sample'))

all_alpha = "abcdefghijklmnopqrstuvwxyzzzzzz"
print("6.", all_alpha.capitalize())  # Capitalize start
print("7.", all_alpha.find("cd"))  # find sub string
print("8.", all_alpha.isalpha())  # check all alpha
print("9.", sample_long_string.isalnum())  # check all num
print("10.", len(sample_long_string))  # return length
print("11.", all_alpha.split('p'))  # split in list at char 'p'
print("12.", all_alpha.strip('z'))  # remove 'z'from start and end of string
print("13.", all_alpha.replace('o', ' '))  # replace 'o' with space
