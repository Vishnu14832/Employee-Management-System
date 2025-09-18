from customtkinter import *
from PIL import Image
from tkinter import messagebox
import ems

def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error","Fill all the details")
    elif usernameEntry.get() == "Vishnu" and passwordEntry.get() == "1234":
        messagebox.showinfo("Success","Login Successful")
        root.destroy()
        ems.run_ems()
    else:
        messagebox.showerror("Error","Wrong credentials")

root = CTk()
root.geometry("930x478")
root.resizable(0,0)

root.title("Login Page")
root.configure(fg_color="#161C30")

image = CTkImage(Image.open("bg.jpg"),size=(474,500))
imageLabel = CTkLabel(root,image=image,text="")
imageLabel.place(x=500,y=0)

headingLabel = CTkLabel(root, text='Employee Management System',text_color = "dark blue",
font=("Goudy Old Style",30,"bold"))
headingLabel.place(x=30,y=100)

usernameEntry = CTkEntry(root,placeholder_text="Enter Username",text_color = "white",width=200)
usernameEntry.place(x=100,y=160)

passwordEntry = CTkEntry(root,placeholder_text="Enter Password",text_color = "white",show="*",width=200)
passwordEntry.place(x=100,y=200)

loginButton = CTkButton(root,text="Login",cursor="hand2",corner_radius=10,command=login)
loginButton.place(x=130,y=250)
root.mainloop()
