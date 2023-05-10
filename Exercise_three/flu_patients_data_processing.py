count = 0
no_of_reported_infections_per_day = 0
total = 0
largest = 0
smallest = 0
while count < 7:
    no_of_reported_infections_per_day = int(input("Enter the number of infections for today: "))
    if count == 0:
        largest = no_of_reported_infections_per_day
        smallest = no_of_reported_infections_per_day
    if largest < no_of_reported_infections_per_day:
            largest = no_of_reported_infections_per_day
    elif smallest > no_of_reported_infections_per_day:
            smallest = no_of_reported_infections_per_day
    total = total + no_of_reported_infections_per_day
    count = count + 1
    if count != 0:
        print(total, count)
        average = total / count
print(f"total = {total} \nAverage = {average} \nLargest = {largest} \nSmallest = {smallest}")