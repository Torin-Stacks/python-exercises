numbers = list(range(1, 21))
print(numbers)
third_number = numbers[2]
print(third_number)
first_five_numbers = numbers[:5]
print(first_five_numbers)
first_half_of_the_list = numbers[:10]
print(first_half_of_the_list)
last_five_numbers_of_the_list = numbers[15:21]
print(last_five_numbers_of_the_list)
every_other_number = numbers[::2]
print(every_other_number)
reverse_list = numbers[::-1]
print(reverse_list)
third_last_number = numbers[-3]
print(third_last_number)
numbers[0:5] = []
print(numbers)