"""Write a program that displays the first 10 Fibonacci numbers 
using lists and a for loop. Display those numbers in a more
readable way for people using join.
"""

#Make a list with 10 spots
numbers = [0]*10

#Set the first two values
numbers[0] = '1'
numbers[1] = '1'

#Calculate the Fibonacci numbers
for index in range(2, len(numbers)):
  numbers[index] = str(int(numbers[index-1]) + int(numbers[index-2]))

#Print the Fibonacci numbers
print ("The first ten fibonacci numbers are: {}".format(', '.join(numbers)))

