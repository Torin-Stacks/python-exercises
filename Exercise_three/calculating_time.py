no_of_minutes = 0
seconds = 0
no_of_hours = 0
no_of_seconds = int(input("Enter the number of seconds: "))
if no_of_seconds >= 60:
    no_of_minutes = no_of_seconds // 60
    seconds = no_of_seconds % 60
elif no_of_seconds < 60:
    seconds = no_of_seconds
if no_of_minutes >= 60:
    no_of_hours = no_of_minutes // 60

print(f"{no_of_hours}: {no_of_minutes}: {seconds}")
