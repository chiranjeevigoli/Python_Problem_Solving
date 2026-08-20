numbers = []
'''n = int(input("Enter how many numbers you want to enter: "))
i = 0
while i<n:
    number = int(input(f"Enter the {i+1} number: "))
    numbers.append(number)
    i += 1'''

for i in range(5):
    number = int(input(f"Enter the {i+1} number: "))
    numbers.append(number)
for number in numbers:
    if number > 10:
        print(number)