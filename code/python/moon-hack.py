#!/bin/python3

items = [
    "A: 3 litres of water",
    "B: Shampoo",
    "C: An extra Spacesuit",
    "D: A shovel",
    "E: A 10 day oxygen supply",
    "F: Solar panels",
    "G: The seeds for your mission",
    "H: The soil for your mission",
    "I: A 3 day food supply",
    "J: Fertilizer"
]

print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
print("You can get to the base in 3 days on your lunar rover")
print("The lunar rover can only fit you in your spacesuit and 4 other items")
print("Out of the items below, which do you bring? \n")

for objects in items:
    print(objects)

print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces \n Ex: A,B,C,D")

user_choice = input("Enter your choice: ")
# print(user_choice)
user_list = list(user_choice.split(','))
# print(user_list)

if "A" not in user_list:
    print("Without a litre of water a day, you will dehydrate")

elif "E" not in user_list:
    print("Without oxygen, you will not have any air to breath")

elif "F" not in user_list:
    print("Without solar panels your rover will not have enough power")

elif "I" not in user_list:
    print("Without food you will not make it to the base")

if "A" in user_list and "E" in user_list and "F" in user_list and "I" in user_list:
    print("Hooray! You picked the right items and made it to the base")
else:
    print("You did not pick the correct 4 item.  You will die")
