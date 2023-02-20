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

cars = 100
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
print("We need to put ", average_passengers_per_car, " in each car")








