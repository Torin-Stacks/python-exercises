no_of_does_in_rabbit_colony_for_a_month = 0;
no_of_baby_rabbits_born_in_a_month = 0
total_no_of_does_in_rabbit_colony = 0
total_no_of_baby_rabbits_born_per_doe = 0
average = 0
total_average = 0
sentinel_value = -1
while no_of_does_in_rabbit_colony_for_a_month != sentinel_value:
    no_of_does_in_rabbit_colony_for_a_month = float(input("Enter number of does for the month or press -1 to end: "))
    total_no_of_does_in_rabbit_colony += no_of_does_in_rabbit_colony_for_a_month
    no_of_baby_rabbits_born_in_a_month = float(input("Enter number of rabbits born in a month or press -1 to end: "))
    total_no_of_baby_rabbits_born_per_doe += no_of_baby_rabbits_born_in_a_month
    average = no_of_baby_rabbits_born_in_a_month / no_of_does_in_rabbit_colony_for_a_month
    total_average = total_no_of_baby_rabbits_born_per_doe / total_no_of_does_in_rabbit_colony
    print(f"On average {average} baby rabbits were born for each doe")
print(f"Total number of baby rabbits for each doe so far: {total_average}")