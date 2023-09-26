
from cgitb import text
from tkinter import *

root = Tk()

window_width = 900
window_height = 500
root.title("Notepad")
root.geometry(f"{window_width}x{window_height}")

mainmenu = Menu(root)
mainmenu.pack()

text_box = Text(root,height=window_height,width=window_width)
text_box.pack(fill=BOTH)

barScroll = Scrollbar(root)
barScroll.pack(side=RIGHT,anchor=E)



























root.mainloop()
















































