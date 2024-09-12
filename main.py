# Enter code here
# Read the README for instructions.
# You must write an algorithm and test cases first!
price_per_gallon = 1
distance_miles = int(input("Enter distance in miles: "))
miles_per_gallon = int(input("Enter miles per gallon: "))
price_of_trip = (distance_miles/miles_per_gallon)*price_per_gallon
print("The total cost of the trip will be", price_of_trip)