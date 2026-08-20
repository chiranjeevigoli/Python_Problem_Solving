def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


numbers = [2, 7, 10, 13, 16, 21]
print(count_even(numbers))

