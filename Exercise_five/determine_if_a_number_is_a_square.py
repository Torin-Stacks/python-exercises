def visualize(number):
    for i in range(number):
        if i * i == number:
            print(f"{number} is a square of {i}")
        else:
            print(f"{number} is not a square of any number")

visualize(16)