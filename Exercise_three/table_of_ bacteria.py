# for number in range(10,1,-2):
#     print(number, end =' ')

for number in range(0, 16, 5):
    hours = 200 * (2 ** number)
    print(f"{number:>2} {hours:>20}")