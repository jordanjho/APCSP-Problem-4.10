grade = input("What grade are you in? ")
year = input("What year is it? ")
while (str(year) <= str((int(year) - int(grade)) + 11)):
  print(str(12 - int(grade)) + " more years until 12th grade! You are currently in year " + str(year))
  grade = int(grade) + 1
  year = int(year) + 1
print("Congratulations! You are now in 12th grade!")

"""
Ask the user what Grade they are in and what the year is.
Program should print out the year in which they will complete 12th 
Grade. Use a while loop. 
(HINT: use two variables grade and year. Use while loop, Increment grade and year in while loop.)
"""