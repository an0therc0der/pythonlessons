"""Write a program that prompts the user for three things: A number, a mathematical operation (such as
+, -, /, or *), and another number. Apply the provided operation to the provided numbers and output the
result to the screen.
Example:
  Input: 15, /, 5
  Output: 3
"""

firstNum = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, /, *): ")
secondNum = int(input("Enter the second number: "))

if operation == "+":
  print (firstNum + secondNum)
elif operation == "-":
  print (firstNum - secondNum)
elif operation == "/":
  print (firstNum / secondNum)
elif operation == "*":
  print (firstNum * secondNum)
else:
  print ("Bad operation!")
