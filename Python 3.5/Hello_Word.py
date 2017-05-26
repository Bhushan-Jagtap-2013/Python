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
