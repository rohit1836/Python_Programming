from random import *
import string


'''
Variable names used - min_len, max_len, dob, full_name, website_name, special_characters, num, lst, passwrd, sp_char, numbers, list_sp_characters, list_characters, 
'''



# Displays the welcome screen for the password generator
def welcome_screen():
    print()
    print("*-------------|*****************************|-------------*")
    print("**-*-*-*-*-*-*|Welcome to Password Generator|*-*-*-*-*-*-**")
    print("*-------------|_____________________________|-------------*")
    print()
    print("Select the password generator you want...")
    print()
    print("1. Random Password Generator")
    print("2. Input Based Password Generator")
    print()
    generator_type = int(input("Enter the choice (1 or 2) : "))
    while True:
        if generator_type == 1:
            print()
            random_password_generator_with_logic()
            input("Press Enter key to exit......")
            break
        elif generator_type == 2:
            print()
            print("It will generate password based on your input in the following required fields")
            input_based_password_generator()
            input("Press Enter key to exit......")
            break
        else:
            print("Wrong Input!! Try again!!")




# Random Password Generator function
def random_password_generator_with_logic():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    symbols = string.punctuation
    all = upper + lower + digit + symbols
    random_password = ""
    
    global min_len, max_len
    min_len = input("Enter the minimum length of password you want : ")
    max_len = input("Enter the maximum length of password you want : ")
    global full_name

    for i in range(min_len,max_len):
        random_password = choice(all) + random_password
    print("The random password generated is : ",random_password)




# Input based Password Generator Function
def input_based_password_generator():    
    global min_len, max_len
    min_len = input("Enter the minimum length of password you want : ")
    max_len = input("Enter the maximum length of password you want : ")
    global full_name
    full_name = input("Enter full name : ")
    global dob
    dob = input("Enter your Date of Birth in format DD/MM/YYYY : ")

    print()
    print("Note : In the follwing field you'll have to enter the fullname of the website for which you\n are generating password, i.e, you'll have have to enter each word.\n For example, if the name of the website is 'www.learnpython.com' then you'll enter 'learn python'.")
    print()

    global website_name 
    website_name = input("Enter the name of the website : ")

    special_characters = input("Want special characters in your password ? (Y or N) : ")
    num = input("Want numbers in your password ? (Y or N) :")

    if (special_characters == "y" or special_characters == "Y") and (num == "y" or num == "Y"):
        lst = want_numbers_and_sp_char()

    elif (special_characters == "n" or special_characters == "N") and (num == "y" or num == "Y"):
        lst = want_numbers()
    
    elif (special_characters == "n" or special_characters == "Y") and (num == "n" or num == "N"):
        lst = want_sp_characters()
    
    passwrd = input_based_password_generator_logic(lst,min_len, max_len)

    print()
    print("The password generated is : ", passwrd)



# If the user wants both special charcaters and numbers along with strings
def want_numbers_and_sp_char():
    sp_char = input("Enter the special character(s) you want in your password : ")
    numbers = input("Enter the number(s) you want in your password : ")

    sp_character_check(sp_char)
    numbers_check(numbers)

    list_sp_characters = ""

    for i in sp_char:
        for x in i:
            list_sp_characters += x + " "
    
    list_characters = full_name.split() + website_name.split() + numbers.split() + list_sp_characters.split() + dob.split("/")

    return list_characters



# If the user wants only numbers along with strings
def want_numbers():
    numbers = input("Enter the number(s) you want in your password : ")
    numbers_check(numbers)
    
    list_characters = full_name.split() + website_name.split() + numbers.split() + dob.split("/")

    return list_characters



# If the user wants only special chracters along with strings
def want_sp_characters():
    sp_char = input("Enter the special character(s) you want in your password : ")
    sp_character_check(sp_char)
    list_sp_characters = ""
    for i in sp_char:
        for x in i:
            list_sp_characters += x + " "
    
    list_characters = full_name.split() + website_name.split() + list_sp_characters.split() + dob.split("/")

    return list_characters



# Special Charcater check function 
def sp_character_check(sp_char):
    while True:
        if sp_char in string.punctuation:
            break
        else:
            print("Invalid Input \nTry Again!!")
            sp_char = input("Enter the special character(s) you want in your password : ")
     


# Numbers check function
def numbers_check(numbers):
    while True:
        if numbers.isdigit():
            break
        else:
            print("Invalid Input \nTry Again!!")
            numbers = input("Enter the number(s) you want in your password : ")



# Less than minimum length logic
def less_than(temp_pass,lst,min_len,random_choice):
    if len(temp_pass) < int(min_len):
        for i in range(2):
            random_choice = choice(lst)
            temp_pass += random_choice
    return temp_pass



# Greater than maximum length logic
def greater_than(temp_pass,lst,max_len,random_choice):
    if len(temp_pass) > int(max_len):
        for i in range(3):
            random_choice = choice(lst)
            temp_pass += random_choice
    return temp_pass



# Main logic of the password_generator
def input_based_password_generator_logic(lst,min_len,max_len):
    temp_pass = ""
    random_choice = ""
    for i in range(3):
        random_choice = choice(lst)
        temp_pass += random_choice
    
    if len(temp_pass) < int(min_len):
        password = less_than(temp_pass,lst,min_len,random_choice)

    elif len(temp_pass) > int(max_len):
        password = greater_than(temp_pass,lst,max_len,random_choice)

    elif (int(max_len) > len(temp_pass) > int(min_len)) or (int(max_len) >= len(temp_pass) >= int(min_len)) or (int(max_len) >= len(temp_pass) > int(min_len)) or (int(max_len) > len(temp_pass) >= int(min_len)):
        password = temp_pass
        
    return password

    

#Execution of the program
welcome_screen()







