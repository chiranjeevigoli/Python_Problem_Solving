number = int(input("Enter the number: "))

while True:
    if number > 0:
        print("Accepted.")
        break
    else:
        print("The number 0 and negative number is not accepted please try again: ")
        number = int(input("Enter the number: "))