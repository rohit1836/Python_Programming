from tkinter import *

root = Tk()
root.geometry("600x500")


def click():
    mylabel = Label(root,text=myentry.get())
    mylabel.pack()


myentry = Entry(root,bg="yellow",fg="red",borderwidth=4)
myentry.pack()


mybutton = Button(root,text="Enter your name",padx=15,pady=15, command=click,fg="red",bg="light blue")
mybutton.pack()



# mylabel1 = Label(root,text="Hello Gui")
# mylabel1.pack()
# mylabel.grid(row=0,column=0)
# mylabel1.grid(row=1,column=0)



root.mainloop()








