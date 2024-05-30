num = 1
sum = 0
while(num <= 10):
  sum = sum + num
  num = num + 1
  print("Sum with value " + str(num - 1) + " is " + str(sum))
  if(num == 4):
    print("terminating program at num == 3")
    break

"""
Sum all numbers between 1 to 10 but exit if it is 3

Sample output:
Sum with value 1  is 1
Sum with value 2  is 3
Sum with value 3  is 6
terminating program at num == 3

Pseudocode:
DISPLAY(Expression)
a + b
IF(condition) 
REPEAT UNTIL(condition) 
"""