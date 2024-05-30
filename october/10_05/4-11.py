age = input("Enter enter your age from the numbers 5-18: ")

if (int(age) >= 5 and int(age) <= 11):
  print("Go to elementary school.")
elif (int(age) >= 12 and int(age) <= 14):
  print("Go to middle school.")
elif (int(age) >= 15 and int(age) <= 18):
  print("Go to high school.")
else:
  print("Invalid number. Please try again.")

"""
Design a activity program
Use following nested if-else
Enter user’s age
This activity program is for users who are in between 5 to 18  years old
If user is 5 to 11, ask user to go to elementary school
If user is 12 to 14, ask user to go to middle school
If it is 15 to 18, high school
"""