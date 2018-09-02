#First, open a file but this time for writing.
testfile = open("/home/student/Documents/PythonLessons/LessonThirteen/PythonDocs/newFile", "w")

#Write some basic data to it.
testfile.write("It smells like up dog in here.")
testfile.write("What's up dog?\n")
testfile.write("Not much man, what's up with you?\n")

#Close the file now that we are complete.
testfile.close()

