"""
1337 Speak! Write a program that gets a word or sentence from a user
and replaces letters with their number look-alike. 
l/L = 1; o/O = 0; e/E = 3; t/T = 7; s/S = 5

Make sure you return a string and not a list at the end!
"""

userString = input("\nEnter a message to translate: ")

#Turn the user message into a list
listString = list(userString)

#Use index values to check and change letters
for index in range(0, len(listString)):
  letter = listString[index].lower()
  if letter == 'l':
    listString[index] = '1'
  elif letter == 'o':
    listString[index] = '0'
  elif letter == 'e':
    listString[index] = '3'
  elif letter == 't':
    listString[index] = '7'
  elif letter == 's':
    listString[index] = '5'

#Turn our list back into the message and print it
print ("Your translated message is: {}\n".format(''.join(listString)))

