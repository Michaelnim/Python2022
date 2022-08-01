# Write your solution here

wage = float(input("Hourly wage: "))
hrs_worked = int(input("Hours worked: "))
day = input("Day of the week:")

total_wage = wage * hrs_worked
sunday_wage = (wage * 2) * hrs_worked

if day != "Sunday":
    print(f"Daily wages: {total_wage} euros")
else:
    print(f"Daily wages: {sunday_wage} euros")