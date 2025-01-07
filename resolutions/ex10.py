"""
10. Band Name Generator Project
a. Create a greeting for your program.
b. Ask the user for the city that they grew up in and store it in a variable.
c. Ask the user for the name of a pet and store it in a variable.
d. Combine the name of their city and pet and show them their band name.
"""

print("Hello, Stranger Musician")
print("Welcome to the Band Name Generator")
city = input("What city that you grew up? ")
petName = input("Whats your pet name? ")
bandName = city + " " + petName

print(f"This is your band name: {bandName}")