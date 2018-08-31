def changeMessage(message):
  newMessage = ""
  for letter in message:
    newMessage += letter*2
  return newMessage

userMessage = input("Enter a message we can change: ")
print (changeMessage(userMessage))


