hours = input("Please input how many hours you worked: ")
pay = input("Please input what the pay per hour is: ")
if (int(hours) >= 40):
  extrapay = float(2.5) * int(pay)
  print("Your total pay is $" + str(int(hours) * int(extrapay)))
else:
  print("Your total pay is $" + str(int(hours) * int(pay)))