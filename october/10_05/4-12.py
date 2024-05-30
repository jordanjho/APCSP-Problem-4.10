num = input("Please enter a number: ")

if (int(num) // 1 != 0):
  if (int(num) > 0):
    print("The number is positive.")
  else:
    print("The number is negative.")
if (int(num) // 1 != 0):
  if ((int(num) >= 100) or (int(num) <= -100)) :
    print("The number is a three or more digit number.")
  else:
    print("The number is not a three or more digit number.")  
else:
  print("The number is 0.")

"""
Ask user to enter a number
a. Using the following structure, check if it is 
positive, negative, or 0 number
        if
              If   #------------ 1
             else   # -----------2
       else
b. Now check if it is three digits or more than three digits number
(Hint: Add one more if-else in between 1 and 2 points)
"""