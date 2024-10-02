# Enter code here
# Read the README for instructions.
# You must write an algorithm and test cases first!
price_per_gallon = 1
distance_miles = int(input("Enter distance in miles: "))
miles_per_gallon = int(input("Enter miles per gallon: "))
price_of_trip = (distance_miles/miles_per_gallon)*price_per_gallon
print("The total cost of the trip will be", price_of_trip)

# Programmers:  Leif, Korede
# Course:  CS151, Professor Yalew
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: You are about to go on a trip and need to plan out the cost of gas.
# \ You need to know the amount of miles you are travelling, the amount of miles per gallon of your car
# \ and the price of gas
# Data In: The amount of miles the user plans to travel, the amount of miles per gallon for their car
# Data Out: The total cost of the trip
# Credits: Based on class