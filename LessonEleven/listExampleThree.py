#Make an empty list
userNumbers = list()

#We want the user to enter five numbers
while len(userNumbers) < 5:
  #Add numbers to our list
  userNumbers.append(int(input("Enter a number: ")))
  print ("Current numbers are: {}".format(userNumbers))

#This time, print the two largest values to the sreen.
largest = max(userNumbers)
userNumbers.remove(largest)
secondLargest = max(userNumbers)
print ("The largest number entered was: {}\nThe second largest number was: {}\n".format(largest, secondLargest))

