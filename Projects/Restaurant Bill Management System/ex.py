# import tkinter as tk

# width = 10

# def strip_str(val):
#     selected_value = var.get()
#     var.set(selected_value[:width] + ("" if len(selected_value) <= width else "..."))
#     print(val)


# r = tk.Tk()
# r.option_add("*font", ("Consolas", 10))
# value_list = ["arc (arc, chord, or pieslice)","bitmap (built-in or read from XBM file)","image (a BitmapImage or PhotoImage instance)","line","oval (a circle or an ellipse)","polygon","rectangle","text","window"]
# var = tk.StringVar()
# menu = tk.OptionMenu(r, var, *value_list, command=strip_str)
# menu.pack()

# r.mainloop()




# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# cmb = ttk.Combobox(root, values=['Hello World!', 'Goodbye World!'])
# cmb.grid()

# root.mainloop()


# python program demonstrating
# Combobox widget using tkinter


# import tkinter as tk
# from tkinter import ttk

# # Creating tkinter window
# window = tk.Tk()
# window.title('Combobox')
# window.geometry('500x250')

# # label text for title
# ttk.Label(window, text = "GFG Combobox Widget",
# 		background = 'green', foreground ="white",
# 		font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# # label
# ttk.Label(window, text = "Select the Month :",
# 		font = ("Times New Roman", 10)).grid(column = 0,
# 		row = 5, padx = 10, pady = 25)

# # Combobox creation
# n = tk.StringVar()
# monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# # Adding combobox drop down list
# monthchoosen['values'] = (' January',
# 						' February',
# 						' March',
# 						' April',
# 						' May',
# 						' June',
# 						' July',
# 						' August',
# 						' September',
# 						' October',
# 						' November',
# 						' December')

# monthchoosen.grid(column = 1, row = 5)
# monthchoosen.current()
# window.mainloop()


# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox as tmsg

# # from tkinter.ttk import Combobox

# root = Tk()
# root.geometry("300x200")
# value = StringVar()
# value.set("Sunday")
# combobox = ttk.Combobox(root,textvariable=value)
# combobox.pack()
# combobox['values'] = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# combobox['state'] = 'readonly'

# numbers = []
# for i in range(100):
#     numbers.append(i)
# number = IntVar() 
# number.set(1)
# numbers = []
# for i in range(1,101):
#     numbers.append(i)
# combobox2 = ttk.Combobox(root,textvariable=number)
# combobox2['values'] = numbers
# combobox2.pack()
# combobox2['state'] = 'normal'

# def show():
#     tmsg.showinfo("Value Selected",f"You selected {value.get()}")


# Button(root,text="Show selected value",command=show).pack()








# root.mainloop()


# dic = {"sunday":1,"monday":2,"tuesday":3}
# print(dic.keys())
# print(dic.values())




# from tkinter import *

# root = Tk()

# root.title("My textbox")



# root.mainloop()




from random import choice


menu = {"Normal thali" : 60,
"Special Thali" : 80,
"Aaloo Parantha" : 50,
"Gobhi Parantha": 50,
"Rajma" : 60,
"Shahi Paneer" : 100,
"Mutter Paneer" : 80,
"Cholley" : 60,
"Jeera Rice" : 40,
"Roti" : 5,
"Parantha" : 15,
"Veg. Manchurian" : 100,
"Veg. Soup" : 40,
"Veg. Fried Rice" : 70,
"Veg. Chowmein" : 80,
"Paneer Chowmien" : 80,
"Momos" : 50,
"Normal Maggi" : 30,
"Masala Maggi" : 35,
"Boil Egg Maggi" : 40,
"Butter Maggi" :50,
"Paneer Maggi" : 55,
"Cheese Maggi" : 60,
"Red Pasta" : 45,
"White Pasta" : 55,
"Pasta With Cheese" : 100,
"Veg. Macroni" : 80,
"Cheese Macroni" : 100,
"Veg. Sandwich" : 25,
"Sandwich Tomato Cheese" : 60,
"Grilled Veg. Sandwich" : 35,
"Cheese Sandwich" : 60,
"Veg. Burger" : 40,
"Tikki Burger" : 50,
"Egg Burger" : 55,
"Cheese Burger" : 60,
"Tea" : 15,
"Coffee" : 20,
"Buttermilk" : 15,
"Pineapple Buttermilk" : 20,
"Nimbu Paani" : 20,
"Nimbu Soda" : 25,
"Pineapple Jal Jeera" : 25,
"Rose Lemonade" : 25,
"Mango Shake" : 30,
"Pineapple Shake" : 30,
"Vanilla Shake" : 30,
"Chocolate Shake" : 35,
"Oreo Vanilla Shake" : 40,
"Oreo Chocolate Shake" : 45
}





# print(menu.keys())
# print(menu.values())
menu_list = []
for items in menu.keys():
    menu_list.append(items)

value = choice(menu_list)
print(value)
print(type(value))
print(menu[value])

# item_price = menu.get(value)
# print(item_price)
# print(type(item_price))


# print(type(menu.values()))
# v = []
# for i in menu.values():
#     v.append(i)
# print(v)

# print(menu.items())















