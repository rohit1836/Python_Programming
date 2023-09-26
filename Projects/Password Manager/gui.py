from tkinter import *


window = Tk()

window.geometry("600x500")
window.minsize(500,400)
window.maxsize(600,500)
window.title("Password Manager")
window.configure(background="#FF9933")

welcome = Label(text="Password Manager",font=("Helvetica",30,"bold","underline"),fg="yellow",background="#FF9933")
welcome.pack(pady=25)

generate_button = Button(text="Generate Password",font=("Arial",20),relief="raised",borderwidth=10)
generate_button.configure(bg="#45CAE5")
generate_button.pack(pady=20)

save_button = Button(text="Save Password",font=("Arial",20),relief="raised",borderwidth=10,padx=20)
save_button.configure(bg="#FFD500")
save_button.pack(pady=10)

exit_button = Button(text="Exit",font=("Arial",15),relief="groove",borderwidth=10)
exit_button.configure(bg="red",command=quit)
exit_button.pack(pady=20)


window.mainloop()























