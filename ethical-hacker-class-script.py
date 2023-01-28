#!/bin/python3


#Variables and Methods
print('\n')
print("Variables and Methods")

quote = "All is fair in love and war."
print("uppercase: ",quote.upper())  #uppercase
print("lowercase: ",quote.lower())  #lowercase
print("titlecase: ",quote.title())  #titlecase
print(len(quote))

name = "Adam" #string
age = 30 #int
gpa = 4.0 #float

print(int(age))
print(int(30.1))
print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)
print('\n')


#Functionsi
print('\n')
print("Here is an example function")

def who_am_I():
    name = Adam
    age = 30    
    print("My name is " + name + " and I am " + str(age) + " years old.")


#adding parameters
print('\n')
print("adding parameters")

def add_one_hundred(num):
    print(num + 100)
add_one_hundred(100)


#multiple parameters
print('\n')
print("multiple parameters")

def add(x,y):
    print(x + y)
add(7,7)

def multiply(x,y):
    return x * y
print(multiply(7,7))

def square_root(x):
    print(x ** .5)
square_root(64)

def nl():
    print('\n')

nl()
#Boolean expressions (True or False)
print('\n')
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 !=9
print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7       #all will return true

test_and = (7 > 5) and (5 < 7)   #both are true so boolean will be true
test_and2 = (7 > 5) and (5 > 7)   #2nd is false so boolean will be false
test_or = (7 > 5) or (5 < 7)   #both are true so boolean is true
test_or2 = (7 > 5) or (5 > 7)   #only first is true but boolean is true because or
print(test_and,test_and2,test_or,test_or2)

test_not = not True   #False

nl()
#Conditional statements
def drink(money):
    if money  >= 2:
        return "You've got yourself a drink"
    else:
        return "No drink for you"
print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5):
        return "Nice try kid!"
    else:
        return "You're too poor and too young"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

nl()
#Lists use brackets
movies = ["The Next Three Days", "Treasure Island", "Man of Steel", "The Batman"]
print(movies[0])    #prints first
print(movies[1:3])  #print start at one and end at 4
print(movies[1:])   #prints all (doesn't stop)
print(movies[:2])   #prints starting at first and stop at 2
print(movies[-1])   

print(len(movies))
movies.append("Robin Hood")
print(movies[4])

#tuples
grades = ("a", "b", "c", "d", "f")
print(grades[1])

#LOOPS
#for loops, start to finish
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)
#while loops, as long as true
i = 1
while i < 10:
    print(i)
    i += 1
