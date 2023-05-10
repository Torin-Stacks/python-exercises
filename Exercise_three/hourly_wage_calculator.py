percentage_increase = 0.03
count = 1
new_hourly_wage = 0
no_of_years = int(input("Enter number of years: "))
hourly_wage = int(input("Enter hourly wage: "))
print(f"Year    Hourly wage ")
while count <= no_of_years:
    new_hourly_wage = new_hourly_wage + (hourly_wage * (1 + percentage_increase) ** count)
    print(f"{count: <} {new_hourly_wage: 12.2f}")
    count += 1



