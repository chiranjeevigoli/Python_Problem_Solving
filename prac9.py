numbers = []
for i in range(5):
    number = int(input(f"Enter {i+1} number: "))
    numbers.append(number)

while True:
    n = int(input("Enter a number to search: "))
    if n in numbers:
        print(f"Number {n} found in the list.")
        break
    else:
        print("Not Found try again.")