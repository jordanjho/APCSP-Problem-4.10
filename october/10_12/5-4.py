num = 2
sum = 0
while(num <= 1000):
  if(num % 2 == 0):
    sum = sum + num
    num = num + 2
    print("The sum of all even numbers between 1 and 1000 is " + str(sum))
  
  else:
    print("nothing")

# Find the sum of all even numbers between 1 and 1000. Use if, else, while.