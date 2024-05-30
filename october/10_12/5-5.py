num = 3
sum = 1
while(num <= 10):
  if (num % 3 == 0):
    sum = sum * num
    num = num + 3
    print("The product of all multiples of 3 to 100 is " + str(sum))
  else:
    ("Nothing")

# Find the product of all multiple of 3 from 3 to 100 
# using a while loop and accumulator variable. Print total.