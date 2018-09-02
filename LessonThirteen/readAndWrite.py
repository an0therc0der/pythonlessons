#Try to open a file, read it, and then write back to it.

with open("./testFile", "r+") as myFile:
  contents = myFile.readlines()
  myFile.seek(0)
  myFile.write("This is the new first line in the file!\n")
  myFile.writelines(contents)

print ("Program Complete!")

