# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number2: "))
operation = input("Operation: ")

res_add = num1 + num2
res_multi = num1 * num2
res_sub = num1 - num2


if (operation == "add"):
    print(f"{num1} + {num2} = {res_add}")
if (operation == "multiply"):
    print(f"{num1} * {num2} = {res_multi}")
if (operation == "subtract"):
    print(f"{num1} - {num2} = {res_sub}")

    