# Write your solution here

celsius = int(input("Temperture: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")

if celsius < 21:
    print("I recommend a jumper as well")
if celsius < 11:
    print("Take a jacket with you")
if celsius < 6:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")