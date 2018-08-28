#Same problem as described in ExerciseOne.py
#This time, print all the even numbers in a single line

userNum = input("Enter a number: ")
evenNumbers = ""
for evenNum in range(0, int(userNum) + 1, 2):
  evenNumbers = evenNumbers + str(evenNum) + " "
print (evenNumbers)
