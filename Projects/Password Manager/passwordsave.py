import random
from typing import BinaryIO
from cryptography.fernet import Fernet
def welcome_screen():
    print()
    print("*-------------|*****************************|-------------*")
    print("**-*-*-*-*-*-*|  Welcome to Password Saver  |*-*-*-*-*-*-**")
    print("*-------------|_____________________________|-------------*")
    print()
    print("It will store your passwords using strong encryption")
    print()


# def savePassword():
    # email = input("Enter your email Id used in the website/application : ")
password = input("Enter the password : ")
key = Fernet.generate_key()
f = Fernet(key)
encryptedpassword = f.encrypt()
# print(key)
print(encryptedpassword)



# savePassword()






























