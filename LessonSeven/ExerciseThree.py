"""Write a program that takes a word from the user and prints it to the screen one character at
a time UNLESS that character is an uppercase or lowercase 'o' or 'e'. In those cases, print a '0'
or '3' instead.
Examples:
  Input: zombies
  Output: z
          0
	  m
	  b
	  i
	  3
	  s
"""

userWord = input("Enter a word: ")
for letter in userWord:
  if letter == 'o' or letter == 'O':
    print ('0')
  elif letter == 'e' or letter == 'E':
    print ('3')
  else:
    print (letter)
