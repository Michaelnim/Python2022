# Write your solution here

name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    soup = int(input("How many portions of soup? "))
    cost = soup * 5.90
    print(f"The total cost is {cost}")
    print("Next please!")

