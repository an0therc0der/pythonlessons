#First we open the file using its path. The 'r' tells python to open the file for reading.
testfile = open('/home/student/Documents/PythonLessons/LessonThirteen/PythonDocs/testFile', 'r')

#Now that we have the file, we need to actually read its contents
testFileContents = testfile.readlines()

#Close the file now that we are done.
testfile.close()

#The contents are return in a list. Let's print each element in that list.
for line in testFileContents:
  print (line.strip())

