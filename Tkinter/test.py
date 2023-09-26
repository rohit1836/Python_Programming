
# from tkinter import *   

# def show():
#     print("The Button is being clicked!!!")



# =================================================Login Form====================================
# window = Tk()
# window.geometry("600x500")
# window.resizable(0,0)

# email_label = Label(window,text = "Enter your E-mail ID : ",font=("Arial",15),padx=10)
# email_label.grid(row=0,column=0,pady=25,sticky=W)

# email_entry = Entry(font=("Arial",15))
# email_entry.grid(row=0,column=1,pady=25,ipadx=5,ipady=5)

# password_label = Label(text="Enter your password : ",font=("Arial",15))
# password_label.grid(row=1,column=0,pady=15,sticky=W)

# password_entry = Entry(show="*",font=("Arial",15))
# password_entry.grid(row=1,column=1,pady=15,ipadx=5,ipady=5)

# login_button = Button(text="Login",font=("Arial",15),command=show)
# login_button.grid(row=2,column=0,columnspan=3,pady=20)

# window.mainloop()


#  ====================================================================================
# window = Tk()
# window.geometry("600x500")

# def button1():
#     print("Button 1 is clicked!!!")
# def button2():
#     print("Button 2 is clicked!!!")
# def button3():
#     print("Button 3 is clicked!!!")
# def button4():
#     print("Button 4 is clicked!!!")

# frame = Frame(border=5,bg="red",relief=GROOVE)
# frame.pack(anchor=NW)

# b1 = Button(frame,border=5,bg="yellow",relief=RAISED,text="Button 1",command=button1)
# b1.pack(side=LEFT)
# b2 = Button(frame,border=5,bg="yellow",relief=RAISED,text="Button 2",command=button2)
# b2.pack(side=LEFT)
# b3 = Button(frame,border=5,bg="yellow",relief=RAISED,text="Button 3",command=button3)
# b3.pack(side=LEFT)
# b4 = Button(frame,border=5,bg="yellow",relief=RAISED,text="Button 4",command=button4)
# b4.pack(side=LEFT)

# window.mainloop()

 


# =================================================GYM form==============================================
from tkinter import *
window = Tk()
window.geometry("600x500")
window.minsize(600,500)

frame = Frame(border=5,relief="groove",bg="red").grid(row=0,column=0)

def userinput():
    with open("id.txt","a") as f:
        f.write(f"The email is : {email_input.get()}\n")
        f.write(f"The password is : {password_input.get()}\n\n")

email_input = StringVar()
password_input = StringVar()

welcome = Label(text="The Rock GYM",font="Constantia 20").grid(row=0,column=1,pady=25)

email_label = Label(text="Enter your e-mail : ",font="Constantia 20").grid(row=1,column=0)
email_entry = Entry(textvariable=email_input,font="Constantia 20").grid(row=1,column=1)

pass_label = Label(text="Enter your password : ",font="Constantia 20").grid(row=2,column=0)
pass_entry = Entry(textvariable=password_input,show="*",font="Constantia 20").grid(row=2,column=1)

button = Button(text="Submit",font="Constantia 20",relief="raised",command=userinput)
button.grid(row=3,column=0,padx=10,pady=20)

window.mainloop()





# ====================================Tours and Travels form====================================

# from tkinter import *

# window = Tk()

# def showvalue():
#     print("It works!!")


# window.geometry("700x400")
# window.minsize(700,400)


# Label(text="Welcome to Tours and Travels",font="comicsansms 20",pady=10).grid(row=0,column=3)

# namelabel = Label(text="Name",font="10",pady=5)
# phonelabel = Label(text="Phone Number",font="10",pady=5)
# genderlabel = Label(text="Gender",font="10",pady=5)
# paymentlabel = Label(text="Payment Mode",font="10",pady=5)

# namelabel.grid(row=1,column=2)
# phonelabel.grid(row=2,column=2)
# genderlabel.grid(row=3,column=2)
# paymentlabel.grid(row=4,column=2)



# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# paymentvalue = StringVar()
# foodservicevalue = BooleanVar()


# nameentry = Entry(textvariable=namevalue)
# phoneentry = Entry(textvariable=phonevalue)
# genderentry = Entry(textvariable=gendervalue)
# paymententry = Entry(textvariable=paymentvalue)

# nameentry.grid(row=1,column=3)
# phoneentry.grid(row=2,column=3)
# genderentry.grid(row=3,column=3)
# paymententry.grid(row=4,column=3)


# foodservice = Checkbutton(text="Want to prebook your meal ?",variable=foodservicevalue)
# foodservice.grid(row=5,column=3)


# Button(text="Submit",command=showvalue).grid(row=6,column=2)


# window.mainloop()



# ================================Take width and height as input from the user and change its size accordingly==================
# from tkinter import * 

# root = Tk()
# root.geometry("400x300")

# def changeSize():
#     root.geometry(f"{width.get()}x{height.get()}")

# widthlabel = Label(text="Enter the width : ",font="comicsansms 15",padx=10,pady=15)
# heightlabel = Label(text="Enter the height : ",font="comicsansms 15",padx=10,pady=15)
# widthlabel.grid(row=0,column=0)
# heightlabel.grid(row=1,column=0)

# width = StringVar()
# height = StringVar()

# widthentry = Entry(font="comicsansms 15",textvariable=width)
# heightentry = Entry(font="comicsansms 15",textvariable=height)
# widthentry.grid(row=0,column=1,ipadx=5,ipady=5)
# heightentry.grid(row=1,column=1,ipadx=5,ipady=5)

# button = Button(text="Click Me!",font="comicsansms 15")
# button.grid(row=2,column=0,padx=10,pady=10)
# button.configure(command=changeSize)

# root.mainloop()





# ==============================================Menu and Message Box tutorial================================================
# from tkinter import *
# import tkinter.messagebox as tmsg

# root = Tk()
# root.geometry("556x453")

# def myFunc():
#     print("File is clicked")

# def Help():
#     tmsg.showinfo("Help","I will help you !!")
#     tmsg.askyesnocancel("kjdbv","yes or no")
#     tmsg.askquestion("kjbd","askquestion")

# mainmenu = Menu(root)

# filemenu = Menu(mainmenu,tearoff=0,background="yellow")
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_checkbutton(label="Hello")
# filemenu.add_radiobutton(label="People")
# filemenu.add_command(label="Save")
# filemenu.add_command(label="Save As")
# filemenu.add_separator()
# filemenu.add_command(label="Settings")

# mainmenu.add_cascade(label="File",menu=filemenu)

# edit = Menu(mainmenu,tearoff=0)
# edit.add_command(label="Cut")
# edit.add_command(label="Copy")
# edit.add_command(label="Paste")

# mainmenu.add_cascade(label="Edit",menu=edit)


# help = Menu(mainmenu,tearoff=0)
# help.add_command(label="Help",command=Help)

# mainmenu.add_cascade(label="Help",menu=help)



# root.config(menu=mainmenu)

# root.mainloop()






# ========================================Sliders Tutorial=======================================
# from tkinter import *
# import tkinter.messagebox as tmsg

# root = Tk()
# root.geometry("500x400")
# scrollbar = Scale(from_ = 0, to= 100,tickinterval=50 ,orient=HORIZONTAL,sliderlength=10)
# scrollbar.set(20)
# scrollbar.pack()

# def order():
#     tmsg.showinfo("Order Received",f"The oder received is of {var.get()}")


# var =StringVar()
# var.set("Radio")
# radio = Radiobutton(text="Paratha",variable=var,value="Paratha")
# radio.pack()


# Button(text="Order",command=order).pack()


# root.mainloop()
























