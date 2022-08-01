# Write your solution here

tempature = int(input("Please type in a temperature(F): "))

celsius = (tempature - 32) * (5/9)

if celsius > 0 or celsius == 0:
    print(f"{tempature} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print(f"{tempature} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")

