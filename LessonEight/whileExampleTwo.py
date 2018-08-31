keepGoing = True

while keepGoing:
  print("Command Options are '1' to do nothing, '2' to print a message, and '3' to quit.")
  userCommand = input("Enter a command (1, 2, or 3): ")
  if userCommand == '1':
    keepGoing = True
  elif userCommand == '2':
    print ("Tis a flesh wound")
  elif userCommand == '3':
    keepGoing = False
  else:
    print ("Unrecognized command. Please try again.")

print ("Program is complete!")

