def getSum():
  myNum = 5
  userNum = int(input("Enter a number to add to program's number: "))
  return myNum + userNum

def getReverseMessage(message):
  reversedMessage = ""
  for index in range(len(message) - 1, -1, -1):
    reversedMessage += message[index]
  return reversedMessage

keepGoing = True
while keepGoing:
  command = input("Enter a command. '1' for addition. '2' for reversing. '3' to quit. Command: ")
  if command == '1':
    print (getSum())
  elif command == '2':
    message = input("Enter a message for the program to reverse: ")
    reversedMessage = getReverseMessage(message)
    print (reversedMessage)
  else:
    keepGoing = False
    
