height = input("Please enter your height in inches: ")
convert = input("Enter 1 to convert height to cm or enter 2 for converting height to mm: ")
if ((int(convert) == 1)):
  print("Your height, when converted to cm, is " + str(int(height) * 2.54) + " cm.")
elif ((int(convert) == 2)):
  print("Your height, when converted to mm, is " + str(int(height) * 25.4) + " mm.")
else:
  print("Invalid number. Please enter 1 or 2.")

"""
Write a program 
  That prompts the user to enter height in inches. 
  Prompt the user to enter 1 for converting height to cm and 2 for converting height to mm. ( 1 inch  = 2.54cm)
  Use if, elif and else
"""