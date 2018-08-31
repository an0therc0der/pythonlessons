userWord = input("Enter a word: ")
userWordTwo = input("Enter another word: ")

#The way we have been using so far.
print ("The first word you entered was " + userWord)
print ("The second word you entered was " + userWordTwo)

#Print some space between the two ways
print ("")

#A different way, but same result
print ("The first word you entered was {}\nThe second word you entered was {}".format(userWord, userWordTwo))


