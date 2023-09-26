

# To calculate area of a rectangle

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         ar = self.length * self.breadth
#         print("The area of the rectangle is : ", ar)

#     def perimeter(self):
#         peri = 2 * (self.length + self.breadth)
#         print("The perimeter of the rectangle is : ",peri)

# length = float(input("Enter the length of the rectangle : "))
# breadth = float(input("Enter the breadth of the rectangle : "))

# rectangle = Rectangle(length,breadth)

# rectangle.perimeter()
# rectangle.area()



# A simple Calculator Program using classes and objects

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2

#     def addition(self):
#         add = self.num1 + self.num2
#         print(f"The sum of the numbers {self.num1} and {self.num2} is : {add}")

#     def subtraction(self):
#         subtract = self.num1 - self.num2
#         print(f"The difference of the numbers {self.num1} and {self.num2} is : {subtract}")

#     def multiplication(self):
#         multiply = self.num1 * self.num2
#         print(f"The product of the numbers {self.num1} and {self.num2} is : {multiply}")

#     def division(self):
#         div = self.num1 / self.num2
#         print(f"The division of the numbers {self.num1} and {self.num2} is : {div}")


# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# calculator = Calculator(num1,num2)

# ans = "y"

# while ans == "y":
#     print("What operation you want to perform ? ")
#     op = input("Enter the operation : ")

#     if op == "+":
#         calculator.addition()
#     elif op == "-":
#         calculator.subtraction()
#     elif op == "*" or op == "X" or op == "x":
#         calculator.multiplication()
#     elif  op == "/":
#         calculator.division()
#     else:
#         print("Invalid Operator !!")

#     ans = input("Want to perform again? (y/n) : ")

#     if ans != "y":
#         break





# A Number Guessing Game using classes and objects 

# import random

# class NumberGuessingGame:
#     def __init__(self,numberGuessed):
#         self.numberGuessed = numberGuessed

#     def numberGuessing(self):
#         randomNumber = random.randint(0,3)

#         if randomNumber == numberGuessed:
#             return 1
#         else:
#             return 0

# ans = "y"
# while ans == "y":
#     numberGuessed = int(input("Guess the number : "))

#     if NumberGuessingGame(numberGuessed).numberGuessing() == 1:
#         print("Bravo!! You Guessed it correct!!")
#         ans = input("Wanna try again (y/n) : ")
#         if ans != "y":
#             break
#     else:
#         print("Better Luck Next Time !")
#         ans = input("Wanna try again !! (y/n) : ")
#         if ans != "y":
#             break



# Rock Paper Scissors Game

class RockPaperScissorsGame:
    def __init__(self):
        pass



print("==========Welcome to Rock Paper Scissors Game==========")
print()
print("Instructions - Choose ")
print("1. for Rock")
print("2. for Paper")
print("3. for Scissors")
print("4. to Exit")


choice = None

while choice != "4":
    print()
    choice = input("Enter your choice :")
    
























