number = int(input("Enter the number: "))

while True:
    if number >= 0:
        print("Accepted.")
        break
    else:
        print("Negative number is not accepted please try again: ")
        number = int(input("Enter the number: "))