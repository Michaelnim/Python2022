# Write your solution here
import math

students = int(input("How many students on the course? "))
groupSize = int(input("Desired group size? "))

groups = math.ceil(students / groupSize)

print(f"Number of groups formed: {groups}")

