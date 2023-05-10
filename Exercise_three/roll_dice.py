import random


count = 1
num_one = 0
num_two = 0
num_three = 0
num_four = 0
num_five = 0
num_six = 0
no_of_throws = 100000

while count <= no_of_throws:
    random_number = random.randint(1, 6)

    if random_number == 1:
        num_one = num_one + 1
    elif random_number == 2:
        num_two = num_two + 1
    elif random_number == 3:
        num_three == num_three + 1
    elif random_number == 4:
        num_four = num_four + 1
    elif random_number == 5:
        num_five = num_five + 1
    else:
        num_six = num_six + 1
    count += 1

print(f"1 {num_one: <} \n2 {num_two: <} \n3 {num_three: <} \n4 {num_four: <} \n5 {num_five: <} \n6 {num_six: <}")


# print(f"2 {num_two: <}")
# print(f"3 {num_three: <}")
# print(f"4 {num_four: <}")
# print(f"5 {num_five: <}")
# print(f"6 {num_six: <}")
