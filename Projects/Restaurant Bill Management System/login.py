
from collections import UserList
from random import randint
from tkinter import *
import mysql.connector as msc
from tkinter import messagebox as tmsg

root = Tk()


def checkLogin():
    Label(text="Logged In").pack()


root.geometry("800x500")
root.resizable(0,0)
root.title("Login Page")

# header_frame = Frame(root,borderwidth=5,bg="pink",relief=SUNKEN,padx=10,pady=10)
# header_frame.pack(fill=X,side=TOP)

# header_label = Label(header_frame,text="Log In",font="30",bg="pink",fg="black")
# header_label.pack()

# form_frame = Frame(root,border="5",relief=GROOVE,bg="yellow")
# form_frame.pack(fill=X,anchor=CENTER)

# username_label = Label(form_frame,text="Username : ",font="20",anchor=CENTER)
# # username_label.grid(row=0,column=0,sticky=N+E+S+W)
# username_label.pack(anchor=CENTER)

# v = IntVar(value=randint(0,100))

# username_entry = Entry(form_frame,font="20",textvariable=v)
# username_entry.pack(anchor=CENTER)

# password_label = Label(form_frame,text="Password : ",font="20")
# password_label.pack(anchor=CENTER)

# password_entry = Entry(form_frame,font="20",show="*")
# password_entry.pack(anchor=CENTER)


# password_label.grid(row=1,column=0,sticky=N+E+S+W)


# username_entry.grid(row=0,column=1,sticky=N+E+S+W)
# password_entry.grid(row=1,column=1,sticky=N+E+S+W)

# log_in_button = Button(form_frame,text="Log In",command=checkLogin)
# # log_in_button.grid(sticky=N+E+S+W)
# log_in_button.pack(anchor=CENTER)


window_width = 800
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.minsize(800,500)
root.resizable(0,0)




def createAccountWindow():

    create_account_window = Toplevel()
    create_account_window.title("Create Account")

    create_window_width = 800
    create_window_height = 500
    create_account_window.geometry(f"{create_window_width}x{create_window_height}")
    create_account_window.minsize(800,500)
    create_account_window.resizable(0,0)

    create_account_frame = Frame(create_account_window,bg="pink",border=5,relief=GROOVE,padx=10,pady=10)
    create_account_frame.pack(side=TOP,anchor=N,fill=X)

    Label(create_account_frame,text="Create Account",bg="yellow",fg="black",width=3,height=3,font="obelixpro 18").pack(fill=X)

    create_account_details_frame = Frame(create_account_window,padx=10,pady=10,bg="pink")
    create_account_details_frame.pack(ipadx=10,ipady=10)

    Label(create_account_details_frame,text="Username : ",font="cambria 20",bg="pink").grid(row=0,column=0,sticky=N+E+W+S,padx=10,pady=10)

    create_username = StringVar()
    create_username_entry = Entry(create_account_details_frame,textvariable=create_username,font="cambria 20")
    create_username_entry.grid(row=0,column=1,sticky=N+E+W+S,padx=10,pady=35,ipadx=10,ipady=5)

    
    Label(create_account_details_frame,text="Password : ",font="cambria 20",bg="pink").grid(row=1,column=0,sticky=N+E+W+S,padx=10,pady=10)
    create_password = StringVar()
    create_password_entry = Entry(create_account_details_frame,textvariable=create_password,font="cambria 20",show="*")
    create_password_entry.grid(row=1,column=1,sticky=N+E+W+S,padx=10,pady=35,ipadx=10,ipady=5)

    Button(create_account_details_frame,text="Create",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=lambda : createAccount(create_username.get(),create_password.get(),create_account_window)).grid(row=2,column=0,columnspan=2,ipadx=5,ipady=5,padx=10,pady=10,sticky=N+E+W+S)






def createAccount(create_usr,create_pass,create_account_window):
    db = msc.connect(host="localhost",user="root",passwd="0000")

    db_cursor = db.cursor()
    
    db_cursor.execute("create database if not exists restaurant")
    db_cursor.execute("use restaurant")
    db_cursor.execute("create table if not exists logindetails (username varchar(50),password varchar(50))")

    db_cursor.execute("select username from logindetails")
    
    username_list = []
    value = (create_usr,create_pass)
    for x in db_cursor:
        username_list.append(x[0])

    cmd = "insert into logindetails values(%s,%s)"

    if create_usr in username_list:
        tmsg.showerror("Error","Username Exists! Choose another..")
    else:
        tmsg.showinfo("Congratulations!","Account Created!")
        db_cursor.execute(cmd,value)
        db.commit()
        create_account_window.destroy()








def loginAccount(log_usr,log_pass):
    db = msc.connect(host="localhost",user="root",passwd="0000")

    db_cursor = db.cursor()
    
    val = (log_usr,log_pass)

    db_cursor.execute("use restaurant")

    db_cursor.execute("select * from logindetails")
    # login_details_list = []
    # for x in db_cursor:
    #     login_details_list.append(x)
    records = db_cursor.fetchall()

    try:
        if val[0]==records[records.index(val)][0] and val[1]==records[records.index(val)][1]:
            tmsg.showinfo("Logged In","Logged In Successfully!")
    except:
        tmsg.showerror("Error","Username or password is incorrect!")








login_frame = Frame(root,bg="pink",border=5,relief=GROOVE,padx=10,pady=10)
login_frame.pack(side=TOP,anchor=N,fill=X)

Label(login_frame,text="Log In",font="obelixpro 18",bg="yellow",fg="black",width=3,height=3).pack(fill=X)

login_details_frame = Frame(root,padx=10,pady=10,bg="pink")
login_details_frame.pack(ipadx=10,ipady=10)

Label(login_details_frame,text="Username : ",font="cambria 20",bg="pink").grid(row=0,column=0,sticky=N+E+W+S,padx=10,pady=10)
username = StringVar()
username_entry = Entry(login_details_frame,textvariable=username,font="cambria 20").grid(row=0,column=1,sticky=N+E+W+S,padx=10,pady=35,ipadx=10,ipady=5)

Label(login_details_frame,text="Password : ",font="cambria 18",bg="pink").grid(row=1,column=0,sticky=N+E+W+S,padx=10,pady=10)
password = StringVar()
password_entry = Entry(login_details_frame,textvariable=password,font="cambria 20",show="*").grid(row=1,column=1,padx=10,pady=10,ipadx=10,ipady=5)

# LogIn Account
login_button = Button(login_details_frame,text="Log In",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=lambda : loginAccount(username.get(),password.get()))
login_button.grid(row=2,column=0,ipadx=5,ipady=5,padx=10,pady=20)

# Create Account
create_account_button = Button(login_details_frame,text="Create Account",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=createAccountWindow)
create_account_button.grid(row=2,column=1,ipadx=5,ipady=5,padx=10,pady=20)









































# def show():
#     value = values.get()
#     Label(root,text=value).pack()


# options = ["Coco Cola","Limeca","Sprite","Aalo Bhujia","Sunday","Monday","Tuesday","Wednesday","thursday","Friday","Saturday","Sunday"]
# values = StringVar()
# values.set("lime")
# drop = OptionMenu(root,values,*options)
# drop.pack()
# drop.config(font="cambria 18",width=10)
# Button(root,text="Click Me!",command=show).pack()
















root.mainloop()