from tkinter import *

from calculator import button_clear

root = Tk()

# Width x Height
root.geometry("700x500")

# width,height
# root.minsize(500,300)

# width,height
# root.maxsize(1100,900)

# Sets the title bar name 
root.title("First GUI")

# frame = Frame(root,bg="blue",border="15",relief="sunken")
# frame.pack(side = TOP,fill="x")

# label = Label(frame,text="Hello This is Frame",relief=GROOVE,border=10)
# label.pack(pady="5",padx="5")



# To change size of the window as required by the user
# def changeSize():
#     root.geometry(f"{width_entry.get()}x{height_entry.get()}")

# width = Label(text="Enter width : ")
# height = Label(text="Enter height : ")
# width.grid(row=0,column=0)
# height.grid(row=1,column=0)

# width_entry =Entry()
# height_entry =Entry()
# width_entry.grid(row=0,column=1)
# height_entry.grid(row=1,column=1)

# size_button = Button(text="Click Here to change size",command=changeSize)
# size_button.grid(row=2,column=0)


root.mainloop()























