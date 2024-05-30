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