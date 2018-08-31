"""
Write a program that takes a number from a user and prints all fibonacci numbers
that are less than that number to the screen. Assume that the user provides proper
input for this exercise.
"""
previousFib = 1
currentFib = 1

userLimit = int(input("Print fibonacci numbers less than what number? "))

if userLimit <= 1:
  print ("None!")
else:
  print (currentFib)
  while currentFib < userLimit:
    print (currentFib)
    #Calculate the Next Number
    nextFib = previousFib + currentFib
    #Update variables to setup the next iteration
    previousFib = currentFib
    currentFib = nextFib

print ("Complete!")
