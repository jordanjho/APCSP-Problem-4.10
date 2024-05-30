hours = input("Please input how many hours you worked: ")
pay = input("Please input what the pay per hour is: ")
if (int(hours) >= 40):
  extrapay = float(2.5) * int(pay)
  print("Your total pay is $" + str(int(hours) * int(extrapay)))
else:
  print("Your total pay is $" + str(int(hours) * int(pay)))

"""
write a program to prompt the user
  how many hours he worked for
  what is pay/hour
  Factory gives the employee 2.5 times hourly rate for above 40 hours and hours*pay for hours less equal to 40 hours
  Calculate total pay. Use if-else.
"""