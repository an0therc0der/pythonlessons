previousFib = 1
currentFib = 1

userLimit = int(input("Print fibonacci numbers less than what number? "))

if userLimit <= 1:
  print ("None!")
else:
  print (currentFib)
  while currentFib < userLimit:
    print (currentFib)
    nextFib = previousFib + currentFib
    previousFib = currentFib
    currentFib = nextFib

print ("Complete!")
