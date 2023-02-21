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
#my_list = [1,2,3]

#my_list = ["string1",12,3.0]
#print(my_list[0])

#my_list1 = [1,2,3]
#my_list2 = [4,5,6]
#finalist = my_list1 + my_list2
#print(finalist)
#print(finalist[:4])

## lists can be mutated, differently than strings
#my_list1 = [1,2,3]
#my_list1[0] = "ciao"
#print(my_list1)

## Itemps can be appended
#my_list1 = [1,2,3]
#my_list1.append(4)
#print(my_list1)

## Remove Items from a list with the pop() method
#my_list1 = [1,2,3]
#my_list1.pop() #by default index for pop() is -1
#print(my_list1)
#popped_item=my_list1.pop()
#print(popped_item)

#my_list1 = [1,2,3]
#my_list1.pop(0)
#print(my_list1)

## Sort element in a list. The sort method occurs in place
#ml =["c", "f", "k", "a"]
#ml.sort() #doesn't return anything to assign is a none type
#print(ml)

## Reverse elements of a list
#ml =["c", "f", "k", "a"]
#ml.reverse()
#print(ml)

## Nested lists
#my_nl =[1,2,[3,5,7]]
#print(my_nl[2][1])

## S3.23 Dictionaries: unordered mappings to store opbjects {'key':'value1},'key2':'value2'}
## Dictionaries are unordered and cannot be sorted

#my_dict = {'key1':'value1','key2':'value2'}
#print(my_dict)
#print(my_dict['key1'])

#my_pr_li = {'hot_dog':4.99 , 'hamburger':5.99 , 'pommes':2.99}
#print(my_pr_li['hamburger'])
#print(my_pr_li.keys())
#print(my_pr_li.values())
#print(my_pr_li.items())

## S3.25 Tuples
## Tuples are like lists but are immutable, not very used actually :-)

#my_tup = ('a','b','c')
#print(type(my_tup))
#print(my_tup[1])
#print("length of tuple is: " , len(my_tup))
#print(my_tup.count(1))
#print(my_tup.index('b'))

## S3.26 Sets: unordered collection of unique elements
#myset=set()
#myset.add(3)
#myset.add(2)
#myset.add(3)
#print(myset)

#mylist=[1,1,1,1,2,2,3]
#print(set(mylist))

## S3.26 Booleans: True and False <- Capital
#print(1>2)
#print(1==1)

## S3.28 Basic I/O with Files
## Very common error: FileNotFoundError: [Errno 2] No such file or directory
#myfile = open('myfile.txt') #open a text file
#print(myfile.read()) #read the file as a unique giant string
#myfile.seek(0) #you must put the cursor back at the beginning ot the txt file
#print(myfile.read())

#myfile = open('myfile.txt') #open a text file
#p(rint(myfile.readlines())

## For windows filepath use \\; for MacOS and Linux use /
## Remember to close the file 

#myfile = open('myfile.txt') #option 1
#print(myfile.readlines())
#myfile.close

#with open('myfile.txt') as my_new_file:
#    contents = my_new_file.read()
#    print(contents)

## Modes: r,w,a,r+,w+

#with open('test_new_file.txt',mode="w") as f: # Creating a new file simply giving the name of a non existent file
#    f.write('Creating a new file')

## S4.32 Comparison Operators
#print(2 == 1)
#print(2 == 2)
#print(2 != 1)
#print(2 != 2)
#print(2 >= 1)

## S4.33 Chaining Comparison Operators

#print(1<2<3)
#print(1<2 and 2<3)
#print(1<2 or 2>3)
#print(3<2 or 2>3)
#print(not(1==1))

## 5.34 If, Elif, Else
## id some_condition:
##      execute some code
## else:
##      do something else

#if 3>2:
#    print("its true")

#loc = "Auto"
#if loc =="Auto":
#    print("Cars are cool")
#elif loc == "Bank":
#    print("money is cool")
#else:
#    print("ciao")

## 5.35 For Loops

#my_it=[1,2,3,4]
#for i in my_it:
#    print(i)

#my_string="Hello world"
#for letter in my_string:
#    print(letter)

#for letter in "Hello World":
#    print(letter)

#tup=(1,2,3)
#for item in tup:
#    print(item)

#mylist = [(1,2),(3,4),(5,6),(7,8)]
#len(mylist)
#for item in mylist:
#    print(item)
#for (a,b) in mylist: #tuple unpucking
#    print(b)

#d={'k1':1, 'k2':2, 'k3':3}
#for item in d:
#    print(item)
#for item in d.items():
#    print(item)
#for item in d.values():
#    print(item)

## 5.36 While Loops

#x = 0
#while x<5:
#    print(f"value of x is {x}")
#    x += 1
#else:
#    print("x is not less than 5")

## break: breaks out of the current closest enclosing loop
## continue: goes to the top of the closest enclosing loop
## pass: do nothing

#x=[1,2,3]
#for item in x:
#    pass

#mystring="ciao"
#for letter in mystring:
#    if letter == "a":
#        continue
#    print(letter)

#mystring="ciao"
#for letter in mystring:
#    if letter == "a":
#        break
#    print(letter)

## 5.37 Useful Operators

#for num in range(10):
#    print(num)

#for num in range(0,11;2):
#    print(num)

#mylist = list(range(0,11,2))
#print(mylist)

#index_count = 0
#for letter in "abcdef":
#    print ("At index {} the letter is {}".format(index_count, letter))
#    index_count +=1

#myword = "abcdefg"
#for item in enumerate(myword):
#    print(item)  # returns tuples

#mylist1 =[1,2,3]
#mylist2 = ["a","b","c"]
#for item in zip(mylist1,mylist2):
#    print(item)

#mylist1 =[1,2,3,4,5,6] # values after 4 will be ignored
#mylist2 = ["a","b","c"]
#for item in zip(mylist1,mylist2):
#    print(item)

#is_in=("a" in "a World")
#print(is_in)

#mylist = [1,2,3,5]
#print(min(mylist))
#print(max(mylist))

#from random import shuffle
#mylist=[1,2,3,4,5]
#mylist2 = shuffle(mylist) #Note: shuffle operates in place, mylist2 is empty
#print(mylist)
#print(mylist2)

#from random import randint
#print(randint(0,100))

#result = input("Enter a number: ")
#print(result)
#print(type(result))

## 5.38 List Comprehension

#mystring = "hello"
#mylist = []
#for letter in mystring:
#    mylist.append(letter)
#print(mylist)

#mystring = "hello"
#mylist = [letter for letter in mystring]
#print(mylist)

#mylist = [letter for letter in "Ciao Giuseppi"]
#print(mylist)

#mylist = [x for x in range(1,10)]
#print(mylist)

#mylist = [x**2 for x in range(1,10)]
#print(mylist)

## 6.41 Methods

#mylist=[1,2,3]
#mylist.insert(0,99)
#print(mylist)
#print(sorted(mylist))

## 6.42 Functions

## 6.43 Def Keyword
## Use snake casing with the name of functions
## Docstrings explain the function '''

#def my_function():
#    '''
#    Simple function sending a greeting
#    '''
#    print("Hello")
#my_function()

#def my_function(name):
#    '''
#    Simple function sending a greeting for a person
#    '''
#    print("Hello " + name)
#my_function("Lorenzo")

#def sum_function(int1,int2):
#    return (int1 + int2)
#result = sum_function(8,7)
#print(result)

## 6.44 Basics of Functions

#def say_hello(name="Default Name"):
#    print("Hello", name)
#say_hello()
#say_hello("Mario")

#def ev_sum(num1,num2):
#    return [num1,num2,num1+num2]
#print(ev_sum(2,5))

## 6.45 Logic with Functions

#if (type ("asd")) == int:
#    print("intero")
#else:
#    print("non intero")

## 6.46 Tuple unpacking with functions

#work_hours = [("Abby",100),("Billy",2000),("Cassie",400)]

#def emp_chk(work_hours):
#    curr_max = 0
#    emp_of_month = ""
#    for employee,hours in work_hours:
#        if hours > curr_max:
#            curr_max = hours
#            emp_of_month = employee
#        else:
#            pass
#    return(emp_of_month,curr_max)

#print(emp_chk(work_hours))

## 6.47 Interaction between functions

""" from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=""
    while guess not in["0","1","2"]:
        guess = input("Pick a number: 0,1, or 2: ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == "0":
        print("Correct!")
    else:
        print("Wrong!")
        print(mylist)

mylist = [" ", "O", " "]
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list,guess) """

## 6.47 args and kwargs

#def myfunc(a,b):
#    #Returns 5% of the sum
#    return (a + b) * 0.05
#
#print(myfunc(40,60))

#def myfunc(a,b,c=0,d=0):
#    return sum((a,b,c,d)) * 0.05
#print(myfunc(30,30,40,100))

#def myfunc(*args):
#    return sum(args) * 0.05
#print(myfunc(30,20))

#def myfunc(*args):
#    for item in args:
#        print(item)
#myfunc(1,2,3,4,5)

#def myfunc(**kwargs):
#    if "fruit" in kwargs:
#        print("My fruit of choice is {}".format(kwargs['fruit']))
#    else:
#        print("no fruit")
#myfunc(fruit="apple")

#def myfunc(*args,**kwargs):
#    print("I like {} {}".format(args[0],kwargs["food"]))
#myfunc(10,20,30,fruit='orange',food='eggs')

#def myfunc(*args):
#    return [n for n in args if n % 2 == 0]
#print(myfunc(1,2,3,4,5,6,7))

""" def myfunk(mystring):
    a = 0
    out_string =""
    for i in mystring:
        print(i)
        if a % 2 == 0:
            out_string = out_string + i.upper()
        else:
            out_string = out_string + i
        a+=1
    return out_string
print(myfunk("ciao")) """

## 6.50 EXERCISES

## write a func the returns the lesser of 2 given numbers if both numbers are even, and the greater if one or both are odd

#def my_eve(num1,num2):
#    if num1 % 2 == 0 and num2 % 2 == 0:
#        return (min(num1,num2))
#    else:
#        return (max(num1,num2))
#print(my_eve(7,17))

##  Write a funk that takes a 2 words string and returns True if both words begin with the same letter
#def ani_cra(mytext):
#    mystr = mytext.split(" ")
#    str1 = mystr[0]
#    str2 = mystr[1]
#    if str1[0].upper() == str2[0].upper():
#        return True
#    else:
#        return False
#print (ani_cra("ciao Pane"))

## return 20 if num1 or num2 or num1 + num2 = 20
#def makes20(num1, num2):
#    if (num1 + num2 == 20 or num1 == 20 or num2 == 20):
#        return True
#    else:
#        return False
# print (makes20(12,8))

## capitalize the first and fourth letter of a name
#def old_mac(mystr):
#    out_str = ""
#    count = 0
#    for i in mystr:
#        if (count==0 or count==3):
#            out_str = out_str + i.upper()
#        else:
#            out_str = out_str + i
#        count +=1
#    return out_str
#print(old_mac("fetentone"))

## returns the sentence with the words reversed
#def rev_sen(mystr):
#    out_words = ""
#    mywords = mystr.split(" ")
#    i = 1
# 
#    while i <= len(mywords):
#        print(out_words)
#        out_words = out_words + mywords[-i] + " "
#        i+=1
#    return out_words
#print(rev_sen("Ciao acs der bla col cane"))

## Given an integer n, return True if n is within 10 of either 100 or 200
#def al_there(my_int):
#    if (90 <= my_int <=110) or (190 <= my_int <=210) :
#        return True
#    else:
#        return False
#print(al_there(209))
# 

#### FIND 33: 

##Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
##    has_33([1, 3, 3]) → True
##    has_33([1, 3, 1, 3]) → False
##    has_33([3, 1, 3]) → False
# 
# def has_33(nums):
#     i = 0
#     while i<= len(nums)-2:
#         if (nums[i]) == 3 and (nums[i+1]) == 3:
#                 return True
#         i+=1
#     return False
# print(has_33([1, 3, 1, 3]))

