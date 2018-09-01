#Create two empty lists
numbers = list()
words = list()

#Get five values from user and sort them
while len(numbers) + len(words) < 5:
  userData = input("Enter an integer or word: ")
  if userData.isdigit():
    numbers.append(userData)
  else:
    words.append(userData)

#Print out the data organized by numeric values then others. 
print ("\nThe numbers you entered were: {}\nThe words you entered were: {}".format(numbers, words))

#Print out all the data as a single string
print ("All the data you entered was: {}\n".format(', '.join(numbers + words)))

