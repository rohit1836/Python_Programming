from tkinter import *
from turtle import right


root = Tk()

root.geometry("500x400")
root.title("Simple dialogue box")




def displayText():
    Label(root, text="Hello Buddy! Wanna know more, Click me again!!").pack()

def joginderText():
    Label(root, text="Yo Joginder!! Thaara Bhai Joginder!! Itte ..... Itte...... Kisi ne socchi na hoggi!!").pack()

def tgText():
    Label(root, text="Welcome to TG!! Aap sabhi ka swagat hai!!").pack()


def tbText():
    Label(root, text="Swagat hai aap sabhi ka!!").pack()


simpleButton = Button(root, height=3, width= 15, text="Click Me", border=5, bg="yellow", fg="black", command=displayText)
simpleButton.pack()

joginderButton = Button(root, text="Yo Joginder", command=joginderText)
joginderButton.pack()

tgButton = Button(root, text="TG", command=tgText)
tgButton.pack()

tbButton = Button(root, text="Tech Burner", command=tbText, bg="Orange", fg="white")
tbButton.pack()

mythpatButton = Button

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)










root.mainloop()










