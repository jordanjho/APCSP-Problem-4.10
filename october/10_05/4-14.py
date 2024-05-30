num = int(input("Please input a number: "))
if ((num >= 0) and (num <= 6) and (num != 3) and (num !=6)):
  if(num == 0):
    print("")
  elif(num == 1):
    print("The number is 1.")
  elif(num == 2):
    print("The number is 2.")
  elif(num == 4):
    print("The number is 4.")
  else:
    print("The number is 5.")
else:
  print("3, 6, and numbers not in the range of 0-6 are invalid!")

"""
Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
Use nested if else
"""