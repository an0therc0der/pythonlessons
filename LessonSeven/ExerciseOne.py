"""Write a program that gets a number from the user and prints all even numbers between 0 and the 
user provided number.
Example:
  Input: 8
  Output: 0 2 4 6 8 (Each can be on a separate line but see if you can print them all on the same 
  line as a challenge.
"""
#Example Solution One

userNum = input("Enter a number: ")
for evenNum in range(0, int(userNum) + 1, 2):
  print (evenNum)
