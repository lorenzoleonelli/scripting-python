## Staff from tutorial The Complete Python Bootcamp From Zero to Hero in Python (Udemy)
## Comments are doubled, real code has a single comment

## S3.11 Introduction to Python Data Types
## NAME             TYPE        DESCRIPTION
## Integers         int
## Floating Point   float
## Strings          str         Ordered Sequence of Characters
## Lists            list        Ordered Sequence of Objects
## Dictionaries     dict        Unordered Key:Value pair
## Tuples           tup         Ordered non mutable sequence of objects
## Sets             set         Unordered Collection of Unique Objects
## Booleans         bool
##

## S3.11 Remember floating point accuracy and computer's abilities to represent numbers in memory
# print (0.1+0.2-0.3)

## S3.14 Variable Assignement
## Use lower case, do not use special character , do not use word with special meaning (ex: list, str)
## Dynamic Typing: you can reassign variables to different Data Types
## type() is helpful to identify what data type you are using
## variable assignement: a = 5
## variable reassignement: a = a + 10

## S3.15 Strings
## Ordered and Immutable Sequences of characters using " or ' -> can be indexed/sliced
## slicing = [start:stop:step]
# print("hello") 
# print ("hello \nworld")
# print ("hello \tworld")
## len() gives the length of a string
#print(len("ciao"))

## S3.16 Strings Indexing and Slicing
#my_string = "Hello World"
#print(my_string)
#print(my_string[0])
#print(my_string[-1])
#print(my_string[1:]) #First character is character 0
#print(my_string[:5]) # The stop is up to , but not included
#print(my_string[3:8])
#print(my_string[::]) # Technically valid but not in use
#print(my_string[::3])
#print(my_string[::-1]) # Reverse the String

## S3.17 Strings Properties and Methods
## String Concatenation
# name = "Sam"
# last_letters = name[1:]
# new_name = "P" + last_letters
# print(new_name)

## String multiplication
# my_name = "Sam is my Friend"
# print(my_name * 3)

## String methods
# my_name = "Sam is my Friend"
# print(my_name.upper())
# print(my_name.lower())
# print(my_name.split())
# print(my_name.split('i'))

## S3.19 Print Formatting with strings
## 2 methods: .format() and f-strings (formatted strings literals)
# print("This is a string {}" .format('-inserted-'))

# print("The {} {} {}" .format("fox", "quick", "brown"))

# print("The {1} {2} {0}" .format("fox", "quick", "brown"))

# print("The {q} {b} {f}" .format(f = "fox", q = "quick", b = "brown"))

#result = 1/7
#print("Result= {r}" .format (r=result))
#print("Result= {r:1.2f}" .format (r=result))

#name = "Pino"
#print(f"Hello, he is {name}")

## S3.21 Lists
## Ordered sequences that can hold a variety of object types, use [] and , to separate objects in a list, support indexing and slicing and can be nested

