grade = input("Please input your grade level: ")

if ((int(grade) >= 10) and int(grade) <= 12):
  ap = input("How many AP courses have you taken? ")
  if (int(ap) == 0):
    print("You can sign up for 4 more AP courses to reach 4 APs.")
  elif (int(ap) == 1):
    print("You can sign up for 3 more AP courses to reach 4 APs.")
  elif (int(ap) == 2):
    print("You can sign up for 2 more AP courses to reach 4 APs.")
  elif (int(ap) == 3):
    print("You can sign up for 1 more AP courses to reach 4 APs.")
  elif (int(ap) == 4):
    print("You can't sign up for anymore AP courses, you already reached 4 APs.")
  else:
    print("This number of AP classes you have entered is invalid. Please enter a number from 1-4.")
else:
  print("Sorry, you must be in grades 10-12 in order to take AP courses.")