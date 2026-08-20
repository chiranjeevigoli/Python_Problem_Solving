numbers = []
for i in range(5):
    number = int(input(f"Enter {i + 1} number: "))
    numbers.append(number)
total = 0
for number in numbers:
    if number % 2 ==0:
        total += number
print(f"Total Sum is = {total}")
