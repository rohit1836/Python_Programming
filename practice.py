
# from os import read


# a = input("Enter the name of file 1 : ")
# b = input("Enter the name of file 2 : ")

# f1 = open(a,"r")
# f2 = open(b,"w")

# l = f1.read()
# f2.write(l)

# f1.close()
# f2.close()

# f = open(b)
# print(f.read())
# # f.read()
# f.close()


# mainstring = input("ENtr the main string : ")
# encryptstring = input("Enter the encryption key : ")

# print("String after encryption is : ",encryptstring.join(mainstring))
# print("String after decryption is : ",mainstring)


# file = open("temp.txt", "r")
# rd = file.read()
# rdsp = rd.split()
# for i in rdsp:
#     if len(i) < 4:
#         print(i)

# file.close()
# with open(r"C:\Users\Jarvis\Desktop\aur hum.txt","r") as f:
#     while f.read():
#         print(f.read(),end="")

# with open("student.txt","w") as f:
#     for i in range(5):
#         name = input("Enter name of student : ")
#         f.write(name)
#         f.write("\n")

# with open("student.txt") as f:
#     print(f.read())


# Program to read a text file and display the number of vowels and consonats, uppercase and lowercase letters
# with open("temp.txt") as f:
#     fread = f.read()
#     vowel = consonants = upper = lower = 0
#     for i in fread:
#         if i in "aeiou":
#             vowel += 1
#         elif i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#         else:
#             consonants += 1
#     print(f'''Number of vowels : {vowel}
# Number of consonats : {consonants}
# Number of uppercase letters : {upper}
# Number of lowercase letters : {lower}''')


# Program to read a text file line by line and display each word separated by "#"
# with open("temp.txt") as f:
#     line = f.read()
#     for i in line.split("\n"):
#         word = i.split()
#         for x in word:
#             print(x,end="#")
#         print()

# ALITER
# with open("temp.txt") as f:
#     s = " "
#     while s:
#         s = f.readline()
#         for i in s.split():
#             print(i,end="#")
#         print()


# with open("ex.dat","rb") as f:
#     print(f.read())

# import pickle

# with open("ex.dat","rb") as f:
#     print(pickle.load(f))

# with open("tmp.txt","w") as f:
#     f.write("Yeh duniya pittal di")
#     f.write("Iss jagah aa gye")
#     f.write(42)

# with open("tmp.txt","w") as f:
#     print(f.writeline("hello duniya"))   ----->  writeline function doesnot exist


# Program to input a number and print its table in a file
# num = int(input("Enter a number : " ))
# with open("table.txt","w+") as object :
#     for i in range(1,11):
#         object.write(f"{num} X {i} = {num * i}\n")
#     object.seek(0)
#     print(object.read())


# import sys

# sys.stdin.readline()
# sys.stdout.write("Hello this is great")


# print("Yeh duniya pittal di, baby doll mei sone di")


# import csv
# with open("birth.txt","r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ",")
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print("COLUMNS ")#,row[0],row[1],row[2])
#             print(",".join(row))
#         else:
#             #print('\t',row[0],row[1],row[2])
#             print(",".join(row))
#     line_count += 1
#     print('Processed lines.', line_count)


# Program to encrypt a string entered by the user
# from random import randint
# user_string = input("Enter the characters/string you want to encrypt : ")
# splitted_string = []
# for i in user_string:
#     splitted_string.append(i)
# # print(splitted_string)
# encrypted_string = ""
# for i in user_string:
#     encrypted_string = i.replace(i,chr(randint(65,90)) + encrypted_string


# l =[15,215,55,"sjvjh",5345,"jsdg",6515,"sdhv","dhcb","dshf",3515]
# for index in range(len(l)):
#     if str(l[index]).isdigit():
#         print(l[index]*3)
    
#     elif str(l[index]).isalpha():
#         print(l[index],end="#")
#         print()


# l = ["arigatou","welcome","hai","ohayo gozaimasu","scoundral"]

# print("a" or "0")
# print("a" or 1)
# print("a" or "c")
# print(1 or "c")
# print(0 or "c")

# print("a" and "B")
# print("a" and "1")
# print("a" and "0")

# print(0 or 1 )
# with open("birth.txt") as f:
#     print(f.read(6))
#     print(f.read(3))



# PROGRAM 1
# Program to receive an octal number and convert it into other bases, i.e., hexadecimal, decimal and binary
# def convert(octnum):
#     numString = str(octnum)
#     decnum = int(numString,8)
#     hexnum = hex(decnum)
#     binnum = bin(decnum)
#     print(f"The number in decimal is : {decnum}")
#     print(f"The number in hexadecimal is : {hexnum}")
#     print(f"The number in binary is : {binnum}")
# octnum = int(input("Enter the number in decimal system: "))
# convert(octnum)




# PROGRAM 2
# Program that generates 4 terms of an AP 
# def AP(init,step):
#     return init, init + step, init + 2*step
# init = int(input("Enter the initial value : "))
# step = int(input("Enter the step value : "))
# a1, a2, a3 = AP(init,step)
# print(f"The series is : {a1}, {a2}, {a3} .......")

    

# PROGRAM 3
# Program to read the first three lines of a file line by line
# with open(r"poem.txt","r") as f:
#     for i in range(3):
#         print(f.readline(), end="")



# PROGRAM 4 
# Program to display the size of the file in bytes
# with open(r"poem.txt") as f:
#     print(f"The size of the file is {len(f.read())} bytes")



# PROGRAM 5
# Program to display the number of lines in a file
# with open(r"poem.txt") as f:
#     lines = f.readlines()
#     linecount = len(lines)
#     print(f"The number of lines in the file is : {linecount}")
    
    

# PROGRAM 6
# Program to get roll no, names and marks of the students of a class and store these details in a file called "Marks.txt"
# noofstudents = int(input("How many students are there in the class ? "))
# with open(r"Marks.txt","w") as f:
#     for i in range(noofstudents):
#         print(f"Enter details for student {i+1} below : ")
#         rollno = int(input("Enter the roll number :"))
#         name = input("Enter name : ")
#         marks = float(input("Enter the marks : "))
#         rec = str(rollno) + "," + name + "," + str(marks) + "\n"
#         f.write(rec)

# with open(r"Marks.txt","r") as f:
#     print(f.read())




# PROGRAM 7                             # Not Working
# with open(r"poem.txt") as fh:
#     line = ""
#     while line:
#         line = fh.readline()
#         for word in line.split():
#             print(word,end = "#")
#         print()






# PROGRAM 8
# Program to get the count of vowels and consonants in a file
# with open(r"poem.txt") as f:
#     vowels = 0
#     consonants = 0
#     data = f.read()
#     for letter in data:
#         if letter in ['a','e','i','o','u',"A","E","I","O","U"]:
#             vowels += 1
#         else:
#             consonants += 1
#     print(f"Vowels : {vowels}")
#     print(f"Consonants : {consonants}")



# PROGRAM 9
# Program to write data of students in a binary file
# import pickle
# with open(r"stu.dat","wb") as f:
#     data = {}
#     rno = int(input("Enter roll number : "))
#     name = input("Enter name : ")
#     marks = int(input("Enter the marks : "))
#     data["Rollno"] = rno
#     data['Name'] = name
#     data['Marks'] = marks
#     pickle.dump(data,f)
# with open(r"stu.dat","rb") as f:
#     print(pickle.load(f))



# PROGRAM 11
# with open("poem.txt") as fh:
#     lowercase = 0
#     uppercase = 0
#     data = fh.read()
#     for letter in data:
#         if letter.isupper():
#             uppercase += 1
#         elif letter.islower():
#             lowercase += 1
#     print(f"Number of uppercase letters in the file are {uppercase}")
#     print(f"Number of lowercase letters in the file are {lowercase}")



# PROGRAM 12
# with open(r"india.txt") as fh:
#     count = 0
#     data = fh.read()
#     # print(data.split())
#     list_data = data.split()
#     for i in list_data:
#         if i == "India":
#             count += 1
#     print(f"Word India occurred {count} times")



# PROGRAM 13
# with open("poem.txt") as fh:
#     data = fh.read()
#     for letter in data:
#         print(letter.upper(),end="")



# PROGRAM 14 
# with open("poem.txt") as fh:
#     data = fh.read()
#     data_split = data.split()
#     for word in data_split:
#         if len(word) < 4:
#             print(word, end=" ")



# PROGRAM 15 
# with open("poem.txt") as fh:
#     data = fh.read()
#     print(data[::-1])




# Program to read a text file line by line and display each word separated by #

# with open("poem.txt") as fh:
#     data = fh.read()
#     data_split = data.split(" ")
#     for word in data_split:
#         print(word,end="#")
#     print()



# print("jsdfc","hello")
# tuple1 = tuple("a","b")
# print(type(tuple1))

# print(ord("a"))
# print(ord("A"))
# print(chr(69))
# print()

# l = ["A","a","Aa","aA"]
# print(max(l))
# print(len((1,2,(3,4,5))))


with open("poem.txt",newline="") as fh:
    rd = fh.read(5)
    print(rd)
    # rn = fh.read()
    # print(rn)
    # rm = fh.readlines()
    # print(rm)
    rm = fh.readline()
    print(rm)


