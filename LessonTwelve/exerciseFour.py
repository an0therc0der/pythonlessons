"""
Many languages lack articles likes 'a', 'the', and 'an.' Write a program that has three functions.
The first function should remove "the" from a sentence. The second function should remove
"an" and the third function should remove "a" from the sentence. Print the sanitized sentence
back to the screen when complete. You can assume that the user will provide a sentence that
follows proper grammar.
"""

#Remove "The" from the sentence
def removeThe(sentence):
  #We need to avoid removing words with "the" in them like the word "there"
  #We cannot simply look for "the" and replace all occurences of it
  if sentence.startswith("the "):
    return sentence.replace("the ", "")
  elif sentence.find(" the ") == -1:
    return sentence
  else:
    return sentence.replace(" the ", " ")

#Remove "A" from the sentence with same considerations as our first function
def removeA(sentence):
  if sentence.startswith("a "):
    return sentence.replace("a ","")
  elif sentence.find(" a ") == -1:
    return sentence
  else:
    return sentence.replace(" a ", " ")

#Remove "An" from the sentence with same considerations as the other functions
def removeAn(sentence):
  if sentence.startswith("an "):
    return sentence.replace("an ", "")
  elif sentence.find(" an ") == -1:
    return sentence
  else:
    return sentence.replace(" an ", " ")

#Get the sentence and call our functions.
sentence = input("Enter a sentence to sanitize: ").lower()
sentence = removeThe(removeA(removeAn(sentence)))
print (sentence.capitalize())

"""
Notice that this solution uses three very similar functions. For an added
challenge, collapse them into one function that removes all articles.
"""
