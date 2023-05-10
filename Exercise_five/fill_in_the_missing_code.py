alist = []
# alist += (6,7,8)
# print(alist)
alist += "birthday"

print(alist)
#
# list1 = [10, 20, 30]
# list2 = [40, 50]
# concatenated_list = list1 + list2
# print(concatenated_list)
#
# for i in range(len(concatenated_list)):
#     print(f'{i}: {concatenated_list[i]}')

def cube(list_of_numbers):
    cubed = 0
    for element in range(len(list_of_numbers)):
        cubed =list_of_numbers[element] ** 3
        print(f"{element}: {cubed}")



print(cube([9,7,6,5]))