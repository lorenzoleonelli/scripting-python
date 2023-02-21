## Exercisec from Book: Zed Shaw "Learn Python the Hard Way", 3rd Edition

## EX1: A good First Program

#print ("Hello World!")
#print ("Hello again")
#print ("I like typing this")
#print ("This is fun")
#print ('Yay! Printing.')
#print ("I'd much rather you 'not'")
#print ('I "said" do not touch this.')

## EX2: Comments and Pound Characters

# A comment, this is so you can read your program l8r
# Anything after the # is ignored

# print("I can have code like this") #And all after this is ignored

# print("This won't run")
# print("This will run")

## EX3: Numbers and math
## Order of Operations is PEMDAS: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction 

#print("I will now count my chickens")
#print("Hens", 25 + 30/6)
#print("Roosters", 100 - 25 * 3 % 4)
#print("Now I will count the eggs")
#print(3+2+1-5+4%2-1/4+6)
#print(3+2<5-7)
#print("What is 3+2", 3+2)
#print(5>-2)
#print(5>=-2)
#print(5<=-2)

## EX4: Variables and Names

""" cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, " cars")
print("There are only ", drivers, " drivers available")
print("There will be ", cars_not_driven, "cars not driven")
print("We can transport ", carpool_capacity, " passengers today")
print("We have", passengers, " to carpool today")
print("We need to put ", average_passengers_per_car, " in each car") """

## EX5: More Variables and Printing

""" my_name = 'Lorenzo'
my_age = 49
my_height = 180
my_weight = 68
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'Brown'

print("Let's talk about %s" % my_name)
print("He's %r cm tall." % my_height)
print("He is %d kg heavy." % my_weight)
print("He has %s hair and %s eyes" % (my_hair , my_eyes))
print("His teeth are generalli %s depending on the cofee" % my_teeth) """

## EX6: Strings and Text

""" x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print(x)
print(y)

print ("I said: %r" % x)
print (" I also said: %s'." %y)

hilarious = False
joke_eval = "Isn't that joke so funnny ? %r"

print (joke_eval % hilarious)

w ="Left side of ..."
e ="a string"

print (w + e) """

## EX7: More Printing

""" print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

 # watch that comma at the end. try removing it to see what happens
print (end1 + end2 + end3 + end4 + end5 + end6,)
print (end7 + end8 + end9 + end10 + end11 + end12) """

## EX 8: Printing, Printing
# You should use %s and only use %r for getting debugging information about something. The %r will give you the “raw programmer’s” version of variable, also known as the “representation.”

""" formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing.",
    "That you could type up right",
    "But ir didn't sing",
    "So I said GN"
)) """

## EX 9: Printing, Printing, Printing

#days = "Mon Tue Wed Thu Fri Sat Sun"
#months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul"

#print("Here are the days", days)
#print("Here are the months:", months)
#print ("""
#there is something here
#with the 3 double quotes
#we can type sooo much
#""")


## EX 10: What was that

#tabby_cat = "\tI'm tabbed in."
#persian_cat = "I'm split\non a line."
#backslash_cat = "I'm \\ a \\ cat."

#fat_cat = """
#I'll do a list:
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
#"""

#print (tabby_cat)
#print (persian_cat)
#print (backslash_cat)
#print (fat_cat)

## EX 11: Asking Questions

""" age = input("How old are you ?")
print("Hello, you are %r old" % age) """












