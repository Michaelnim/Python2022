# Write your solution here
number = int(input("Please type a number: "))

if number < 1000 and number > 100:
    print("This number is smaller than 1000")
    print("Thank you!")
elif number < 100 and number > 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
elif number < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")
else:
    print("Thank you!")
