# ----------------Mujhe kuch nhi aata----------------

# class People:
#     def __init__(self,name):
#         self.name = name
    
#     def description(self):
#         print("Name : ",self.name)

# People("fuck").description()

# peopleClassobject = People("Soham")
# peopleClassobject.description()

# People("Nice").description()

# p = People("Good")
# p.description()





# ----------------------------------Get the congigurations of a computer and display it--------------------------


# class Computer:
#     def __init__(self,processor,ram,graphics,storage):
#         self.processor = processor
#         self.ram = ram
#         self.storage = storage
#         self.graphics = graphics

#     def description(self):
#         print("Processor : ",self.processor)
#         print("RAM : ",self.ram)
#         print("Graphics : ",self.graphics)
#         print("Storage : ",self.storage)


# comp1 = Computer("Ryzen 5 3500U", "8 GB", "Vega 8 Mobile Graphics", "1 TB")
# Comp2 = Computer("i5 11th gen", "16 GB", "NVIDIA RTX 3050Ti", "1 TB SSD")

# comp1.description()
# Comp2.description()




# -------------------get the details of car and display it---------------------------

# class Car:
#     def __init__(self,company,name,variant) -> None:
#         self.company = company
#         self.name = name
#         self.variant = variant

#     def show(self):
#         print("Brand : ",self.company)
#         print("Name : ",self.name)
#         print("Variant : ",self.variant)


# car = Car("Ford","Mustang","Petrol")
# car.show()
        



# -----------------Calculator Program-------------------

# class Calculator:
#     def __init__(self,num1,num2) -> None:
#         self.num1 = num1
#         self.num2 = num2

#     def multiplication(self):
#         print("Product is : ",self.num1 * self.num2)

#     def subtraction(self):
#         print("Difference is :",self.num1 - self.num2)

#     def addition(self):
#         print("Sum is : ",self.num1 + self.num2)

#     def division(self):
#         print("Division is : ",self.num1 / self.num2)


# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# cal = Calculator(num1,num2)

# op = input("Enter operation (+,-,*,/) : ")

# if op == '+':
#     cal.addition()

# elif op == '-':
#     cal.subtraction()

# elif op == '*':
#     cal.multiplication()

# elif op == '/':
#     cal.division()

# else:
#     print("Invalid operator!!")






# -----------------------------Program to calculate area of different shapes-----------------------
import math
class Shapes:
    class Rectangle:
        def __init__(self,length,breadth) -> None:
            self.length = length
            self.breadth = breadth
        
        def area(self):
            return self.length * self.breadth

        def perimeter(self):
            return 2 * (self.length + self.breadth)

    class Circle:
        def __init__(self,radius) -> None:
            self.radius = radius

        def area(self):
            return math.pi * self.radius * self.radius

        def circumference(self):
            return 2 * math.pi * self.radius

    class Square:
        def __init__(self,side) -> None:
            self.side = side

        def area(self):
            return self.side * self.side

        def perimeter(self):
            return 4 * self.side

    class Cube:
        def __init__(self,edge) -> None:
            self.edge = edge

        def tsa(self):
            return 6 * self.edge *self.edge
        
        def csa(self):
            return 4 * self.edge * self.edge

        def volume(self):
            return self.edge * self.edge * self.edge

    class Cuboid:
        pass

    class Cone:
        pass

    class Cylinder: 
        pass

    class Sphere:
        pass














