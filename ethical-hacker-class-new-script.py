#!/bin/python3

import sys   #imports system fuctions and parameters
from datetime import datetime as dt #import with alias
print(dt.now())

sentance = "This is a sentance."
print(sentance[:4])

print(sentance.split())

sentance_split = sentance.split()
sentance_join = ' '.join(sentance_split)
print(sentance_join)

quote = "he said \"give me all you money\""
print(quote)

too_much_space = "                             hello                  "
print(too_much_space.strip())

movie = '"Man of steel"'
print("I recently watched {}.".format(movie))

#key value pairs
drinks = {"White Russian": 7, "old Fashion": 10, "Lemon Drop": 8}   #drink is key and price is value
print(drinks)

employees = {
    "Finance": ["Bob", "Linda", "Tina"], 
    "IT": ["Gene", "Louise", "Teddy"], 
    "HR": ["Jimmy Jr.", "Mort"]
}
print(employees)
print(employees["IT"])

employees["Legal"] = ["Mr. Frond"]    #adds new key value pair
