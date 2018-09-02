"""
A teacher has asked you to assist with managing student grades. She has asked you to write
a program that can take in six grades and return the highest grade, the lowest grade, and
the average of the grades. Grades will be entered as a number (i.e. 80, 73, 78.5, etc).
"""

#Function gets 6 grades and returns basic stats about them
def gradeStats():
  grades = list()
  while len(grades) < 6:
    grades.append(float(input("Enter a grade: ")))
  largest = max(grades)
  smallest = min(grades)
  average = sum(grades) / len(grades)
  return "\nMax: {}\nMin: {}\nAvg: {}\n".format(largest, smallest, average)

#Get the program going
print ("\nStarting the Program!")
print (gradeStats())

