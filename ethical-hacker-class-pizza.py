#!/bin/python3

def happy(pizza_int):
    if pizza_int > 0:
        print("Happy Bob")
    else:
        print("Not happy, Bob. Not happy")
 
pizza_str = input("How many slices of pizza do you have? ")
happy(int(pizza_str))
