# Write your solution here
days = int(input("How many times a week do you eat at the student cafeteria? "))
avgPrice = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))


print(f"Daily: {((days * avgPrice) + groceries) / 7} euros")
print(f"Weekly: {days * avgPrice + groceries} euros")

