"""
11. Tip Calculator
Create a program that asks the user o total of the bill, how many people will split and the percentage of the tip.
The program will divide the bill for the people and calculate how much each person will pay.
Show the result with 2 decimal places.
"""

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = float(input("How much tip would you like to give? "))

each_pay = (total / people) * (1 + (tip/100))

print(f"Each person should pay: $ {each_pay:.2f}")