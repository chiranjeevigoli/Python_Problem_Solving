user_age = int(input("Enter your age: "))
user_id = input("Do you have an id say yes or no: ")

if user_age >= 18 and user_id == "yes":
    print("Eligible")
else:
    print("Not eligible")