

# tup = (12,"dfg")

# print(tup)
# print(type(tup))



# lst = [1,]

# print(lst)
# print(type(lst))


from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()

mainmenu = Menu(root)



def about():
    tmsg.showinfo("About","This is a simple Notepad created by the great Rohit Das")



filemenu = Menu(mainmenu,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_checkbutton(label="Auto-Save")
filemenu.add_command(label="Exit",command=quit)
mainmenu.add_cascade(label="File",menu=filemenu)


editmenu = Menu(mainmenu,tearoff=0)
editmenu.add_radiobutton(label="hello")
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
mainmenu.add_cascade(menu=editmenu,label="Edit")

helpmenu = Menu(mainmenu,tearoff=0)
helpmenu.add_command(label="Get Started")
helpmenu.add_command(label="Documentation")
helpmenu.add_command(label="Report Issue")
helpmenu.add_separator()
helpmenu.add_command(label="Check for Updates")
helpmenu.add_checkbutton(label="Auto-Check For Updates")
helpmenu.add_separator()
helpmenu.add_command(label="About",command=about)

mainmenu.add_cascade(menu=helpmenu,label="Help")








root.configure(menu=mainmenu)



root.mainloop()












