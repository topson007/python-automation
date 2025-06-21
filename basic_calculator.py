# Basic Calculator

print('Calculator')

#Addition
def add(userInput1, userInput2):
    return userInput1 + userInput2

#Subtraction
def sub(userInput1, userInput2):
    return userInput1 - userInput2

#Multiplication 
def mul(userInput1, userInput2):
    return userInput1 * userInput2

#Division
def div(userInput1, userInput2):
    if userInput2 == 0:
        return "Zero Division Error"
    return userInput1 / userInput2

print("Enter operation:\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

enterOperation = int(input("Enter operation from 1 to 4): "))

userInput1 = int(input("Enter first number: "))
userInput2 = int(input("Enter second number: "))

if enterOperation == 1:
    print(userInput1, "+", userInput2, "=", add(userInput1, userInput2))
elif enterOperation == 2:
    print(userInput1, "-", userInput2, "=", sub(userInput1, userInput2))
elif enterOperation == 3:
    print(userInput1, "*", userInput2, "=", mul(userInput1, userInput2))
elif enterOperation == 4:
    print(userInput1, "/", userInput2, "=", div(userInput1, userInput2))
else:
    print("Invalid input")