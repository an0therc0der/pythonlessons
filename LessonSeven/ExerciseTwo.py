"""Write a program that prints the index value for each letter within a user provided word.
Example:
  Input: "Hello!"
  Output: 0:H
          1:e
	  2:l
	  3:l
	  4:o
	  5:!
"""

userWord = input("Enter a word: ")
index = 0
for letter in userWord:
  print (str(index) + ":" + letter)
  index = index + 1

