from tkinter import *

root = Tk()
root.geometry("320x350")
root.minsize(320,350)
root.maxsize(320,350)
root.title("Calculator")


# def n1():
#     uservalue.set(1)
# def n2():
#     uservalue.set(2)



# uservalue = IntVar()
# uservalue.set("")

# userinput = Entry(font="timesnewroman 15",width=25,textvariable=uservalue)
# userinput.grid(row=0,column=0,columnspan=4,padx=15,pady=20,ipady=5,ipadx=5)

# num1 = Button(text="1",font="25",width=5,height=2,command=n1)
# num2 = Button(text="2",font="25",width=5,height=2,command=n2)
# num3 = Button(text="3",font="25",width=5,height=2)
# num4 = Button(text="4",font="25",width=5,height=2)
# num5 = Button(text="5",font="25",width=5,height=2)
# num6 = Button(text="6",font="25",width=5,height=2)
# num7 = Button(text="7",font="25",width=5,height=2)
# num8 = Button(text="8",font="25",width=5,height=2)
# num9 = Button(text="9",font="25",width=5,height=2)
# num0 = Button(text="0",font="25",width=5,height=2)

# period = Button(text=".",font="25",width=5,height=2)
# result = Button(text="=",font="25",width=5,height=2)
# add = Button(text="+",font="25",width=5,height=2)
# subtract = Button(text="-",font="25",width=5,height=2)
# divide = Button(text="/",font="25",width=5,height=2)
# multiply = Button(text="X",font="25",width=5,height=2)


# num1.grid(row=1,column=0)
# num2.grid(row=1,column=1)
# num3.grid(row=1,column=2)
# num4.grid(row=2,column=0)
# num5.grid(row=2,column=1)
# num6.grid(row=2,column=2)
# num7.grid(row=3,column=0)
# num8.grid(row=3,column=1)
# num9.grid(row=3,column=2)
# num0.grid(row=4,column=0)

# period.grid(row=4,column=1)
# result.grid(row=4,column=2)
# add.grid(row=2,column=3)
# subtract.grid(row=1,column=3)
# divide.grid(row=3,column=3)
# multiply.grid(row=4,column=3)

num = ["1","2","3","4","5","6","7","8","9","0"]

for rws in range(3):
    for clmns in range(3):
        Button(text=num[clmns],font="25",width=5,height=2).grid(row=rws,column=clmns)
        # num.pop(clmns)
    




root.mainloop()


