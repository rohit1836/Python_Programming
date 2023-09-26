from tkinter import *



root = Tk()
root.title("Simple Calculator")


def button_click(number):
    input_field.insert(0,str(input_field.get()) + str(number))
    # input_field.delete(0,END)

def button_clear():
    input_field.delete(0,END)












input_field = Entry()
input_field.grid(row=0,column=0,columnspan=4)

button_1 = Button(text="1",padx=10,pady=10,command=lambda : button_click(1))
button_2 = Button(text="2",padx=10,pady=10,command=lambda : button_click(2))
button_3 = Button(text="3",padx=10,pady=10,command=lambda : button_click(3))
button_4 = Button(text="4",padx=10,pady=10,command=lambda : button_click(4))
button_5 = Button(text="5",padx=10,pady=10,command=lambda : button_click(5))
button_6 = Button(text="6",padx=10,pady=10,command=lambda : button_click(6))
button_7 = Button(text="7",padx=10,pady=10,command=lambda : button_click(7))
button_8 = Button(text="8",padx=10,pady=10,command=lambda : button_click(8))
button_9 = Button(text="9",padx=10,pady=10,command=lambda : button_click(9))
button_0 = Button(text="0",padx=10,pady=10,command=lambda : button_click(0))
button_period = Button(text=".",padx=10,pady=10,command=button_click)

button_add = Button(text="+",padx=10,pady=10,command=button_click)
button_subtract = Button(text="-",padx=10,pady=10,command=button_click)
button_result = Button(text="=",padx=10,pady=10,command=button_click)
button_clear = Button(text="C",padx=10,pady=10,command=button_clear)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_subtract.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_clear.grid(row=3,column=3)

button_0.grid(row=4,rowspan=2,column=0)
button_period.grid(row=4,column=2)
button_result.grid(row=4,column=3)









root.mainloop()






