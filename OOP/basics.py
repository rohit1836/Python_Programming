

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def display(self):
#         print("Hello", self.name)
#         print(" you", self.name)

# p = Person("Tony")
# p.display()

# Program to get the configurations of two computers and display it to the user

# class Computer:

#     def __init__(self,processor,ram,graphics,storage):
#         self.processor = processor
#         self.ram = ram
#         self.graphics = graphics
#         self.storage = storage

#     def configuration(self):
#         print("Processor : ",self.processor)
#         print("RAM : ", self.ram)
#         print("Graphics : ", self.graphics)
#         print("Storage : ",self.storage)
    

# comp1 = Computer("Ryzen 5 3500U", "8 GB", "Vega 8 Mobile Graphics", "1 TB")
# comp2 = Computer("i5 11th gen", "16 GB", "NVIDIA RTX 3050Ti", "1 TB SSD")

# print(".........Configurations of Computer 1 are ........")
# comp1.configuration()
# print()
# print(".........Configurations of Computer 2 are ........")
# comp2.configuration()


# comp1.mouse = "logitech"
# print()
# print(comp1.mouse)
# print(type(comp1))



# Basic Calculator program

# class Calculator:
#     def __init__(self,n1,n2) -> None:
#         self.n1 = n1
#         self.n2 = n2
    
#     def addition(self):
#         return self.n1 + self.n2

#     def subtraction(self):
#         return self.n1 - self.n2

#     def multiplication(self):
#         return self.n1 * self.n2

#     def division(self):
#         return self.n1 / self.n2

    
# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))

# calc = Calculator(number1,number2)

# print(f"The sum of {number1} and {number2} is {calc.addition()}")
# print(f"The difference of {number1} and {number2} is {calc.subtraction()}")
# print(f"The product of {number1} and {number2} is {calc.multiplication()}")
# print(f"The division of {number1} and {number2} is {calc.division()}")



# create a class programmer for storing information of few workers working at microsoft

# class Programmer:
#     company = "Microsoft"

#     def __init__(self,name,product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"The name of the programmer is {self.name} and is working for product {self.product} at {self.company}")

    
# rohan = Programmer("Rahul","VS Code")
# anjali = Programmer("Anjali", "MS Office")

# rohan.getInfo()
# anjali.getInfo()


# Create a class from a book you would read

class Book:
    def __init__(self,name_of_book,publisher_of_book,category_of_book,author_of_book):
        self.name_of_book = name_of_book
        self.publisher_of_book = publisher_of_book
        self.category_of_book = category_of_book
        self.author_of_book = author_of_book

    def description(self):
        print(f"Name : {self.name_of_book}")
        print(f"Author : {self.author_of_book}")
        print(f"Publisher : {self.publisher_of_book}")
        print(f"Category : {self.category_of_book}")

    

book1 = Book("Think and Grow Rich","Fingerprint Classics","Self-Growth","Napolean Hill")
print("..... Description of Book 1 is .....")
# print(book1.name_of_book)
# print(book1.author_of_book)
# print(book1.publisher_of_book)
# print(book1.category_of_book)
print(book1.description())
# print()
print("..... Description of Book 2 is .....")
book2 = Book("The Alchemist","Harper Collins Publications","Self-Growth, Fictional","Paulo Coelho")
# print(book2.name_of_book)
# print(book2.author_of_book)
# print(book2.publisher_of_book)
# print(book2.category_of_book)
print(book2.description())










