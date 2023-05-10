import math

one_box = 6
no_of_box_for_28eggs = 28 / one_box
print(no_of_box_for_28eggs)
remaining_eggs_in_uncompleted_box = 28 % 6
additional_eggs_to_fill_up = one_box - remaining_eggs_in_uncompleted_box

print(f"The number of boxes a farmer needs to store 28 eggs = {math.ceil(no_of_box_for_28eggs)}")
print(f"{remaining_eggs_in_uncompleted_box} are placed in the last uncompleted box")
print(f"{additional_eggs_to_fill_up} are needed to fill the last box")