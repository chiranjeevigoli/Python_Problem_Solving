"""
Write a program that:

asks the user for a positive integer n
uses a for loop with range()
calculates the sum of all numbers from 1 through n
prints the final sum

"""

number = int(input("Enter a positive number: "))

while True:
    if number < 0:
        print("Please try again with positive number.")
        number = int(input("Enter a positive number: "))
    else:
        total = 0
        for i in range(number+1):
            total += i
        print(f"Your total value is: {total}")
        break 
