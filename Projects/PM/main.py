
from tkinter import *



root = Tk()

root.title("LogIn Window")
window_height = 500
window_width = 800
root.geometry(f"{window_width}x{window_height}")




def came():
    print(username.get()," ",password.get())


# ------------------------------ LogIn Window-----------------------------

def logInWIndow():

    logInLabelFrame = Frame(root,bg="pink",relief=GROOVE,padx=10,pady=10,border=5)
    logInLabelFrame.pack(fill=X)

    Label(logInLabelFrame, text="Log In Window",font="Arvo 25",bg="yellow",fg="black",height=2).pack(fill=X)

    logInDetailsFrame = Frame(root,padx=10,pady=10,bg="pink")
    logInDetailsFrame.pack(ipadx=10,ipady=10)

    Label(logInDetailsFrame,text="Username : ",font="cambria 18",fg="black",bg="pink").grid(row=0,column=0)
    global username 
    username = StringVar()
    Entry(logInDetailsFrame,font="cambria 15",textvariable=username).grid(row=0,column=1)

    Label(logInDetailsFrame,text="Password : ",font="cambria 18",bg="pink",fg="black").grid(row=1,column=0)
    global password 
    password = StringVar()
    Entry(logInDetailsFrame,font="cambria 15",textvariable=password).grid(row=1,column=1)

    Button(logInDetailsFrame,text="Log In",font="cambria 18",command=passwordManagerMainMenu).grid(row=2,column=0,columnspan=2,sticky=N+E+W+S,padx=10,pady=20)







# --------------------------------- Main Menu Windwow ----------------------------------------


def passwordManagerMainMenu():
    mainMenu = Toplevel()
    mainMenuWindowHeight = 900
    mainMenuWindowWidth = 700
    mainMenu.geometry(f"{mainMenuWindowHeight}x{mainMenuWindowWidth}")

    passwordManagerLabelFrame = Frame(mainMenu,bg="light green",border=5,relief=GROOVE)
    passwordManagerLabelFrame.pack(fill=X)

    Label(passwordManagerLabelFrame,bg="light green",fg="black",text="Password Manager",font="Cambria 25",padx=10,pady=10).pack(fill=X)

    passwordManagerButtonsFrame = Frame(mainMenu,bg="light green",border=5)
    passwordManagerButtonsFrame.pack(fill=BOTH,ipadx=10,ipady=15)

    Button(passwordManagerButtonsFrame,text="Generate Password",font="Cambria 18",fg="black",bg="pink",border=5,relief=RAISED,padx=5,pady=5,width=25).pack(ipadx=5,ipady=5,pady=15)
    Button(passwordManagerButtonsFrame,text="Save Password",font="Cambria 18",fg="black",bg="pink",border=5,relief=RAISED,padx=5,pady=5,width=25).pack(ipadx=5,ipady=5,pady=15)
    Button(passwordManagerButtonsFrame,text="Get Password",font="Cambria 18",fg="black",bg="pink",border=5,relief=RAISED,padx=5,pady=5,width=25).pack(ipadx=5,ipady=5,pady=15)
    Button(passwordManagerButtonsFrame,text="Update Id-Password",font="Cambria 18",fg="black",bg="pink",border=5,relief=RAISED,padx=5,pady=5,width=25).pack(ipadx=5,ipady=5,pady=15)






















































logInWIndow()



root.mainloop()

