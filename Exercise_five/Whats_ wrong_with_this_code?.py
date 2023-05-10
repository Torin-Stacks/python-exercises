# day, high_temperature = ('Monday', 87, 65) #too many values to unpack
# print(day)

# numbers = [1, 2, 3, 4, 5]
# print(numbers[10]) #index 10 is out of bounds

# name = 'amanda'
# name[0] = 'A' #String is immutable
# print(name)

# numbers = [1, 2, 3, 4, 5]
# print(numbers[3.4]) #index cannot be float literal

# student_tuple = ('Amanda', 'Blue', [98, 75, 87])
# student_tuple[0] = 'Ariana' #tuple is immutable
# print(student_tuple)

# random = ('Monday', 87, 65) + 'Tuesday' #can only concatenate a tuple with a tuple
# print(random)

# 'A' += ('B', 'C')

# x = 7
# del x
# print(x) # x no longer exists

# numbers = [1, 2, 3, 4, 5, 10]
# print(numbers.index(10)) # gives index no 5

# numbers = [1, 2, 3, 4, 5]
# numbers.extend(6, 7, 8) # method extend for list takes only one argument
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# numbers.remove(10) #10 is not in the list element
# print(numbers)

values = []
values.pop() #empty list cannot be popped
print(values)