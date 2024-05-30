age = input("Enter enter your age from the numbers 5-18: ")

if (int(age) >= 5 and int(age) <= 11):
  print("Go to elementary school.")
elif (int(age) >= 12 and int(age) <= 14):
  print("Go to middle school.")
elif (int(age) >= 15 and int(age) <= 18):
  print("Go to high school.")
else:
  print("Invalid number. Please try again.")