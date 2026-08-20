def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [10,23,43,2334]
print(calculate_sum(numbers))