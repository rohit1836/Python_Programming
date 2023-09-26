from tkinter import *
from tkinter import font

root = Tk()

window_width = 800
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.minsize(800,500)
root.resizable(0,0)
root.title("Log In")


def passwordManagerWindow():
    password_manager_window = Toplevel()
    password_manager_window.title("Password Manager")
    password_manager_window_width = 900
    password_manager_window_height = 700
    password_manager_window.geometry(f"{password_manager_window_width}x{password_manager_window_height}")
    password_manager_window.resizable(0,0)

    heading_frame = Frame(password_manager_window,bg="light green",relief=GROOVE,border=5)
    heading_frame.pack(ipadx=5,ipady=5,fill=X)

    Label(heading_frame,text="Password Manager",font="Cambria 30",fg="black",bg="yellow").pack(fill=X,padx=5,pady=10,ipadx=5,ipady=10)

    body_frame = Frame(password_manager_window,border=3,bg="light green")
    body_frame.pack(ipadx=10,ipady=15,fill=X)
    
    # The four buttons in the main window
    Button(body_frame,text="Generate Password",border=5,relief=RAISED,padx=5,pady=5,width=25,font="Cambria 20",bg="pink",activebackground="light pink",command=generatePasswordWindow).pack(ipadx=5,ipady=5,pady=15)
    Button(body_frame,text="Save Password",border=5,relief=RAISED,padx=5,pady=5,width=25,font="Cambria 20",bg="pink",activebackground="light pink",command=savePasswordWindow).pack(ipadx=5,ipady=5,pady=15)
    Button(body_frame,text="Saved Passwords",border=5,relief=RAISED,padx=5,pady=5,width=25,font="Cambria 20",bg="pink",activebackground="light pink",command=showSavedPasswordsWindow).pack(ipadx=5,ipady=5,pady=15)
    Button(body_frame,text="Update Saved Passwords",border=5,relief=RAISED,padx=5,pady=5,width=25,font="Cambria 20",bg="pink",activebackground="light pink").pack(ipadx=5,ipady=5,pady=15)
    Button(body_frame,text="Exit",border=5,relief=RAISED,padx=5,pady=5,width=25,command=quit,font="Cambria 20",bg="pink",activebackground="light pink").pack(ipadx=5,ipady=5,pady=15)


def generatePasswordWindow():
    generate_password_window = Toplevel()
    generate_password_window.title("Password Generator")
    generate_password_window_width = 900
    generate_password_window_height = 700
    generate_password_window.geometry(f"{generate_password_window_width}x{generate_password_window_height}")
    generate_password_window.resizable(0,0)


def randomGeneratorWindow():
    random_generator_window = Toplevel()
    random_generator_window.title("Random Password Generator")
    random_generator_window_width = 900
    random_generator_window_height = 700
    random_generator_window.geometry(f"{random_generator_window_width}x{random_generator_window_height}")
    random_generator_window.resizable(0,0)

def definedGeneratorWindow():
    defined_generator_window = Toplevel()
    defined_generator_window.title("User-Defined Password Generator")
    defined_generator_window_width = 900
    defined_generator_window_height = 700
    defined_generator_window.geometry(f"{defined_generator_window_width}x{defined_generator_window_height}")
    defined_generator_window.resizable(0,0)

def savePasswordWindow():
    save_password_window = Toplevel()
    save_password_window.title("Save Password")
    save_password_window_width = 900
    save_password_window_height = 700
    save_password_window.geometry(f"{save_password_window_width}x{save_password_window_height}")
    save_password_window.resizable(0,0)

def showSavedPasswordsWindow():
    saved_passwords_window = Toplevel()
    saved_passwords_window.title("Saved Passwords")
    saved_passwords_window_width = 900
    saved_passwords_window_height = 700
    saved_passwords_window.geometry(f"{saved_passwords_window_width}x{saved_passwords_window_height}")
    saved_passwords_window.resizable(0,0)

















# Log In Window

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
password_entry = Entry(login_details_frame,textvariable=password,font="cambria 20",show="*")
password_entry.grid(row=1,column=1,padx=10,pady=10,ipadx=10,ipady=5)


login_button = Button(login_details_frame,text="Log In",font="cambria 18",border=3,relief=RAISED,width=15,bg="light green",activebackground="light green",command=passwordManagerWindow)
login_button.grid(row=2,column=0,columnspan=2,ipadx=5,ipady=5,padx=10,pady=20)


























root.mainloop()

