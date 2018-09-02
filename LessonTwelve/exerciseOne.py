"""
A friend of yours recently opened file on his computer that has some important text. However,
it looks like something happened to all the text. Every single space and period was doubled
somehow! Write a program that takes a sentence and removes all these duplicates!

Example: "This  is  really  annoying.."   -->   "This is really annoying."
"""

#Get a sentence and turn it into a list to modify
sentence = list(input("Enter the weird sentence: "))
index = 0
limit = len(sentence)

#Use the index value to check values in our list
while index < limit:
  #If we find a space or period, then adjust position by 2 to skip the next space or period
  if sentence[index] == " ":
    sentence[index] = ""
    index += 2
  elif sentence[index] == ".":
    sentence[index] = ""
    index += 2
  else:
    index += 1

#Turn our list back into a string and print it to the screen
print ("The corrected sentence is:\n{}".format(''.join(sentence)))

