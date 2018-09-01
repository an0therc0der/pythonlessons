#First, we make a regular string variable
testWord = "Hello!"

#Then we cast it into a list
listWord = list(testWord)
print (listWord)

#Now, let's try changing some values
for index in range(0, len(listWord)):
  if listWord[index] == 'l':
    listWord[index] = '1'

#Print our listWord to see if changes were actually made
print (listWord)

#But there's a problem....that result doesn't look...right.

