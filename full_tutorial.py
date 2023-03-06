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

## Items can be appended
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

## Given a string multiply each character by 3: Hello -> HHHeeellllllooo
#def mult_str(mystr):
#    outstr = ""
#    for i in mystr:
#        outstr = outstr + 3*i
#    return outstr

#print(mult_str("ciao"))

## 6.55 LAMBDA expressions Map and Filter
#def square(num):
#    return num ** 2

#my_nums = [1,2,3,4]
#print(map(square,my_nums))
#for item in map(square,my_nums):
#    print(item)

#def splicer(mystring):
#    if len(mystring)%2 == 0:
#        return 'EVEN'
#    else:
#        return mystring[0]
#names =["pino","mauro","carlo"]
#print(list(map(splicer,names)))

#def check_even(num):
#    return num%2 == 0
#mynums = [1,2,3,4,5,6]
#print(list(filter(check_even,mynums)))

#square = lambda num: num ** 2
#print(square(5))


#my_nums = [1,2,3,4]
#print(list(map(lambda num:num ** 2, my_nums)))

## 6.56 Nested statements and scope
## LEGB: Local - Enclosing Function locals - global - built-in

#x = 25
#def printer():
#    x = 50
#    return x

#print(x)
#print(printer())


## 7 ## M I L E S T O N E    P R O J E C T

""" def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [" ", "X", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
#display(row1, row2, row3)

row2[1] = "X"
#display(row1, row2, row3)

#result = input("Please enter a value: ")
#print(type(int(result)))

def user_choice():
    choice = "WRONG"
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ?")
        if choice.isdigit() == False:
            print("Sorry this is not a digit")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, out of range")
                within_range = False

    return int(choice)

user_choice() """

## .................
## .................




## 8.1 Object Oriented Programming Introduction
## Allow to scle your code, creating your own objects with methods and attributes

#mylist = [1,2,3]
#myset = set()

#class Sample():
#    pass

#my_sample = Sample()
#print(type(my_sample))


""" class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed="Lab", name ="Pippo", spots = True)
my_dog2 = Dog(breed="cocker", name = "Cagnasso", spots = False)

print(my_dog.breed , my_dog.name , my_dog.spots)
print(my_dog2.breed) """


""" class Dog():

    #Class object attribute: same for any istance of a class
    species = "mammal"

    #Attributes
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    #Method
    def bark(self,number):
        print("BAU I am {} and the number is {}".format(self.name,number) )

my_dog = Dog(breed="Lab", name ="Pippo", spots = True)
my_dog2 = Dog(breed="cocker", name = "Cagnasso", spots = False)

print(my_dog.breed , my_dog.name , my_dog.spots)
print(my_dog2.breed, my_dog2.species)
my_dog.bark(12)
 """


""" class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
    
    #METHOD
    def get_circonference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(33)

print(my_circle.pi)
print(my_circle.radius)

print(my_circle.get_circonference()) """

## 8.71 Inheritance and Polimorphism
##

""" class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("bau")


myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()
mydog= Dog()
mydog.who_am_i()
mydog.bark() """

###########################

""" class Dog():
    def __init__(self,name) -> None:
        self.name = name
    def speak(self):
        return self.name + " woof!"
    
class Cat():
    def __init__(self,name) -> None:
        self.name = name
    def speak(self):
        return self.name + " mao"
    
niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko) """

## 8.72 OO Programming Special Methods
##

""" mylist = [1,2,3]
print(len(mylist))

class Sample():
    pass
mysample = Sample()
print(mysample)


class Book():
    def __init__(self,title,author,pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Python1","Jose",200)
print(b)
str(b) """

## 8.73 OO Programming Exercises


## 9.77 Modules and Packages


## 9.78 name and main


## 10.80 Errors and Exception Handling
## Error handling allows th code to continue with other code and report the error
## try: attempted block of code
## except: executed if there is an error in the try code
## finally: executed regardless of an error

#def add(n1,n2):
#    print(n1+n2)
#
#print(add(10,"aa"))

""" try:
#   result = 10 + "10"
    result = 10 + 10
except:
    print("Not adding correctly")
else:
    print("Correctly added")
    print(result) """


""" try:
    f = open("testfile","r")
    f.write("Write a test line")
except TypeError:
    print("Was a typerror")
except OSError:
    print("was OS error")
except:
    print("All other exceptions")
finally:
    print("I always run") """


"""  """


""" def ask_for_int():
    while True: # Remember that with while true there must always be a "break"
        try:
            result = int(input("Pls provide number:"))
        except:
            print("That is not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("End of try")

ask_for_int() """

## 10.81 Errors and exceptions homework

""" try:
    for i in [2,"b","3"]:
        print(i**2)
except:
    print("enter integers") """

## 10.84 Pylint: evaluates the quality of your code
## Pip install pylint
## pylint full_tutorial.py

#a = 1
#b = 2
#print(a)
#print(B)

## 10.85 Run tests with unittest library




## 12.98 Decorators with Python: decorate a function

""" def func():
    return 1

print(func()) """

#def hello():
#    return "Hello!"

#greet = hello
##print(greet())

#del hello
##print(hello())
#print(greet())

""" def hello(name="Lore"):
    print("The hello() func has been executed")

    def greet():
        return "\t This is the greet func inside hello"
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print(greet())
    print(welcome())

hello()
welcome() """

""" def hello(name="Lore"):
    print("The hello() func has been executed")

    def greet():
        return "\t This is the greet func inside hello"
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print("I am going to return a function!!")

    if name == "Lore":
        return greet
    else:
        return welcome

my_new_func= hello("Lore") """

## 13.100 Python Generators

#my_list = list(range(0,10))
#for i in my_list:
#    print(i)

""" def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result

print(create_cubes(10)) # The entire list is kept in memory

for x in create_cubes(10):
    print(x) """


""" def create_cubes(n):
    for x in range(n):
        yield x ** 3

for x in create_cubes(10): # it is a genarator, memory used more efficiently
    print(x) """


""" def Fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in Fibo(10):
    print(num) """


""" def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g)) # Her it will throw an error """


""" s = "hello"
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter)) """


## 14.103 Intro to Advanced Python modules

## 14.104 Python collection module

""" from collections import Counter

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,"a","a"]
print(Counter(mylist))
print(Counter(mylist)[1])

Sentence = "how many times does a word show with a word in times how ?"
print(Counter(Sentence.split()))

letters = "aaaaaaaabbbbbbbbbbbccddd"
c=Counter(letters)
print(c.most_common(2)) """


""" from collections import defaultdict
d=defaultdict(lambda: 0)
d["correct"] = 100
print(d["correct"])
print(d["wrong"])
print(d) """


""" from collections import namedtuple
Dog = namedtuple("Dog",["age","breed","name"])
sammy = Dog(age=5, breed ="Husky", name="Sam")
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy[0]) """

## 14.104 Python OS and shutil module

#f = open("practice.txt","w+")
#f.write("This is a test string")
#f.close

#import os
#print(os.getcwd())
#print(os.listdir())
#print(os.listdir("F:\_PERSONAL\THEINFOSECVAULT"))

#import shutil
#shutil.move ('practice.txt', '..')

#import os
#for folder, sub_folders, files in os.walk('.'):
#    print(f"Looking at {folder}")
#    print("\n")
#    print("The subfolders are:")
#    for sub_fold in sub_folders:
#        print(f"Subfolders: {sub_fold}")
#    print("\n")
#    print("the files are: ")
#    for f in files:
#        print(f"\t File: {f}")
#    print("\n")

## 100.106 Python DateTime

#import datetime
#mytime = datetime.time(2,20)
#print(mytime.minute)
#print(mytime)
#print(type(mytime))

#from datetime import date
#from datetime import datetime
#date1 = date(2021,11,3)
#date2 = date(2020,11,4)
#print(date1 - date2)
#datetime1 = datetime(2021,12,3,22,30)
#datetime2 = datetime(2021,11,3,21,0)
#print(datetime1 - datetime2)


## Math and Random Modules
# import math
## help(math) 
# value = 4.35
# print(math.floor(value))
# print(math.ceil(value))
# print(math.pi)

#import random
#print(random.randint(0,100))
#print(random.seed(99))
#print(random.randint(0,100))
#print(random.randint(0,100))

import random
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))