#Make an empty list
userNumbers = list()

#We want the user to enter five numbers
while len(userNumbers) < 5:
  #Add numbers to our list
  userNumbers.append(int(input("Enter a number: ")))
  print ("Current numbers are: {}".format(userNumbers))

#This time, print the two largest values to the sreen.
userNumbers.sort()
userNumbers.reverse()
print ("The largest number entered was: {}\nThe second largest number was: {}\n".format(userNumbers[0], userNumbers[1]))

