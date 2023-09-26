# # Separate function for both number and special character in password
# def want_numbers_and_sp_char():
#     sp_char = input("Enter the special character(s) you want in your password : ")
#     numbers = input("Enter the number(s) you want in your password : ")

#     sp_character_check(sp_char)
#     numbers_check(numbers)

#     list_sp_characters = ""
#     list_numbers = ""
#     for i in sp_char:
#         for x in i:
#             list_sp_characters += x + " "
#     for i in numbers:
#         for x in i:
#             list_numbers += x + " "

#     list_characters = fname.split() + lname.split() + wbname.split() + list_sp_characters.split() + list_numbers.split()



# # Special function for only numbers 
# def want_numbers():
#     numbers = input("Enter the number(s) you want in your password : ")
#     numbers_check(numbers)
#     list_numbers = ""
#     for i in numbers:
#         for x in i:
#             list_numbers += x + " "

#     list_characters = fname.split() + lname.split() + wbname.split() + list_numbers.split()



# # Special function for only special characters
# def want_sp_characters():
#     sp_char = input("Enter the special character(s) you want in your password : ")
#     sp_character_check(sp_char)
#     for i in sp_char:
#         for x in i:
#             list_sp_characters += x + " "
#     list_characters = fname.split() + lname.split() + wbname.split() + list_sp_characters.split()






# # Special Charcater check function 
# def sp_character_check(sp_char):
#     while True:
#         if sp_char in '''~`!@#$%^&*()_-+=}]{[\|;:'"/?.>,<''':
#             break
#         else:
#             print("Invalid Input \nTry Again!!")
#             sp_char = input("Enter the special character(s) you want in your password : ")
            




# # Numbers check function
# def numbers_check(numbers):
#     while True:
#         if numbers.isdigit():
#             break
#         else:
#             print("Invalid Input \nTry Again!!")
#             numbers = input("Enter the number(s) you want in your password : ")





# # Yes or No check function for the pass_generator_algorithm() function
# def yes_no(special_characters,num):
#     while True:
#         if (special_characters == "y" or special_characters == "Y") and (num == "y" or num == "Y"):
#             break
#         else:
#             print("Invalid Input \nTry Again!!")
#             special_characters = input("Want special characters in your password ? (Y or N) : ")
#             num = input("Want numbers in your password ? (Y or N) :")    

from random import *

min_len = 8
max_len = 16
password = ""
lst = ["rajesh","arora","epic","games","369","@","#","17","08","2004"]
random_choice = ""
check = ""
temp_pass = ""
# for i in range(2):
#     random_choice = choice(lst)
#     temp_pass = temp_pass + random_choice
#     check = check + random_choice 
#     if random_choice in check:
#         random_choice = choice(lst)
#         while random_choice in check:
#             check = check + random_choice

for i in range(2):
    random_choice = choice(lst)
    check += random_choice
    temp_pass += random_choice

def less_than(temp_pass):
    if len(temp_pass) < min_len:
        for i in range(4):
            random_choice = choice(lst)
            temp_pass += random_choice


def greater_than(temp_pass):
    if len(temp_pass) > max_len:
        for i in range(3):
            random_choice = choice(lst)
            temp_pass += random_choice


print("The Password is : ", password)
print(temp_pass)
print(random_choice)
print(check)



















