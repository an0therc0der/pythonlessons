#Use an alternate way to work with files

with open("./testFile", "w") as myFile:
  myFile.write("This is an alternate way to open and use files!\n")
  myFile.write("This way is now considered best practice.\n")

