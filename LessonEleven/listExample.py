#Make an empty list
userNumbers = list()

#We want the user to enter five numbers
while len(userNumbers) < 5:
  #Add numbers to our list
  userNumbers.append(int(input("Enter a number: ")))
  print ("Current numbers are: {}".format(userNumbers))

#Add all of the elements in the list together
print (sum(userNumbers))

