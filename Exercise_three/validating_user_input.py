failure_counter = 0
number = int(input("Enter number 1 or 2: "))
while number != 1 and number != 2:
    failure_counter = failure_counter + 1
    number = int(input("Enter 1 or 2: "))

print(failure_counter)

# a = b = 7
# print(a)
# print(b)
#
# for row in range(10):
#     for column in range(10):
#         print(" < " if row % 2 == 1 else " > ", end = "")
#     print()


# for rows in range(3):
#     for columns in range(3):
#         print("0", end = " ")
#     print()