user_problem = input("what is your problem ?: ")
yes_or_no = input("Have you had this problem before ? yes or no: ")
while yes_or_no != "yes" and yes_or_no != "no":
     print("Enter yes or no: ")
     yes_or_no = input(" have you had this problem before ?: ")
if yes_or_no == "yes":
          print("Well you have it again")
else:
          print("well, you have it now")
