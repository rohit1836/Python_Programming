
# import mysql.connector as c

# connection = c.connect(
#   host="localhost",
#   user="root",
#   password="0000",
#   database="sample"
# )

# if connection.is_connected():
#   print("Connection established")


# if connection.is_connected():
#   print("Successfully connected")

# cursor_object = connection.cursor()

# cursor_object.execute("select * from employee")

# records = cursor_object.fetchall()
# print(records)
# for item in records:
#   print(item)

# print(type(records))

# print(cursor_object.column_names)
# print(type(cursor_object.column_names))

# print(cursor_object.fetchone())


# query = cursor_object.execute("show databases like 'resta'")

# print(type(query))

# if query == None:
#   cursor_object.execute("create database resta")
#   cursor_object.execute("use resta")
# elif query != None:
#   cursor_object.execute("use resta")
#   print(cursor_object.execute("show tables"))




# query = cursor_object.execute("show databases")

# print(type(query))

# for x in query:
#   print(x)





# =========================================================================================




# import mysql.connector as msc

# db = msc.connect(host="localhost",user="root",passwd="0000")

# if db.is_connected():
#   print("Successfully connected.....")

# db_cursor = db.cursor()

# db_cursor.execute("show databases")

# # print(db_cursor)
# # databases = []
# # for x in db_cursor:
# #   databases.append(x[0])

# # print(databases)


# while True:
#   usrname = input("Enter username : ")
#   password = input("Enter password : ")

#   db_cursor.execute("create database if not exists resta")
#   db_cursor.execute("use resta")
#   db_cursor.execute("create table if not exists logindetails (username varchar(50), password varchar(50))")
#   db_cursor.execute(f'''insert into logindetails values("{usrname}","{password}")''')

#   choice = input("1->Enter more\n2->Exit\nEnter Choice : ")
#   if choice == "2":
#     break
#   else:
#     db.commit()


# def check():
#   usrname = input("Enter username : ")
#   password = input("Enter password : ")

#   db_cursor.excute("")



# db_cursor.execute("use resta")


# table_data = db_cursor.execute("select * from employee")
# print(table_data)

# for x in db_cursor:
#   print(x)

# db_cursor.execute("select Ename from employee")
# ename = []
# for x in db_cursor:
#   print(x)
#   ename.append(str(x))

# print(ename)






# query = db_cursor.execute("select username from logindetails where username = 'Mohit'")
# print(query)
# print(db_cursor)
# ex = []
# for x in db_cursor:
#   print(x)
#   ex.append(x[0])
# print(ex)


# usrname = input("Enter username : ")
# # password = input("Enter password : ")
# cmd = "insert into logindetails values(%s)"
# db_cursor.execute(f"select username from logindetails where username = '{usrname}'")

# try:
#   db_cursor.execute(f"insert into logindetails values({usrname})")
#   # db.commit()

# except:
#   print("Username Exists! Choose another")
#   # db.rollback()
# else:
#   db_cursor.execute(f"insert into logindetails values({usrname})")
#   db.commit()





# ========================LogIn Account==========================

# username = input("Enter username : ")
# password = input("Enter password : ")
# val = (username,password)


# db_cursor.execute("select * from logindetails")
# log_details = []
# for x in db_cursor:
#   log_details.append(x)

# print(log_detais)

# if val in log_details:
#   print("username and password present")
#   print(log_details.index(val))
# else:
#   print("Not present")
  
# try:
#   if val[0] == log_details[log_details.index(val)][0] and val[1] == log_details[log_details.index(val)][1]:
#     print("Username and Password are correct!")
# except:
#   print("Username or password is incorrect!")


# =========================Create Account==============================
# db_cursor.execute("select username from logindetails")
# db_cursor.execute("select column_names")
# e = db_cursor.fetchall()
# username_column = []
# for x in db_cursor:
#   username_column.append(x)
#   print(x)
# print(e)
# print(username_column)

# e = db_cursor.column_names
# f = db_cursor.fetchall()
# print(e)
# print(f)

# Using fetchall method
# records = db_cursor.fetchall()

# usrname = input("Enter username : ")
# password = input("Enter password : ")
# val = (usrname,password)
# cmd = "insert into logindetails values(%s,%s)"
# try:
#   if val[0]!=records[records.index(val)][0]:
#       print("Congratulations! Account Created..")
# except:
#   db_cursor.execute(cmd,val)
#   print("Username exists! Choose another..")




# username_column = []
# for x in db_cursor:
#   username_column.append(x)

# usrname = input("Enter username : ")
# password = input("Enter password : ")
# val = (usrname,password)
# cmd = "insert into logindetails values(%s,%s)"

# try:
#   if val[0]!=username_column[username_column.index(val)][0]:
#     print("Congratulations! Account Created..")
#     db_cursor.execute(cmd,val)
# except:
#   print("Username exists! Choose another..")



# Extra Primitive Method
# username_column = []
# for x in db_cursor:
#   username_column.append(x[0])
# print(username_column)

# username = input("Enter username : ")
# password = input("Enter password : ")
# cmd = "insert into logindetails values(%s,%s)"
# value = (username,password)

# try:
#   if username in username_column:
#     print("Username Exists! Try another...")
# except:
#   db_cursor.execute(cmd,value)
#   print("Account created...")
#   db.commit()


# if username in username_column:
#     print("Username Exists! Try another...")
# else:
#   db_cursor.execute(cmd,value)
#   print("Account created...")
#   db.commit()







# usrname_list = []
# cms = "insert into logindetails values(%s,%s)"
# val = (username,password)
# for x in db_cursor:
#   usrname_list.append(x[0])

# if username in usrname_list:
#   print("Username Exists! Choose another..")
# else:
#   db_cursor.execute(cms,(username,password))
#   db.commit()
#   print("Username added....")




# Calculator program with ultra pro max logic

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
op = input("Enter the operation (+,-,*,/) : ")

opList = ['+','-','*','/']

ans = "y"

while ans == "y":
    for  i in opList:
        if op in opList:
            print(f"The result is : {num1}")

# while ans == "n":
#     for o in ls



















