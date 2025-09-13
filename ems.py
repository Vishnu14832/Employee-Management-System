from customtkinter import *
from PIL import Image

window = CTk()
window.title("Employee Management System")
window.geometry("930x600")
window.resizable(False,False)
window.configure(fg_color="#161C30")

logo=CTkImage(Image.open("header.jpg"),size=(930,158))
logoLabel = CTkLabel(window,image=logo,text="")
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame = CTkFrame(window,fg_color="#161C30")
leftFrame.grid(row=1,column=0)

idLabel = CTkLabel(leftFrame,text="Id",font=("Arial",18,"bold"))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry = CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
idEntry.grid(row=0,column=1)

nameLabel = CTkLabel(leftFrame,text="Name",font=("Arial",18,"bold"))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry = CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel = CTkLabel(leftFrame,text="Contact",font=("Arial",18,"bold"))
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry = CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel = CTkLabel(leftFrame,text="Role",font=("Arial",18,"bold"))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Web Developer','Data Scientist','Ai Engineer','Network Engineer','IT Consultant','UI UX Designer','Cloud Architect','Technical Writer']

roleBox = CTkComboBox(leftFrame,values=role_options,width=180,font=("Arial",18,"bold"))
roleBox.grid(row=3,column=1)

genderLabel = CTkLabel(leftFrame,text="Gender",font=("Arial",18,"bold"))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female']
genderBox = CTkComboBox(leftFrame,values=gender_options,width=180,font=("Arial",18,"bold"))
genderBox.grid(row=4,column=1)

salaryLabel = CTkLabel(leftFrame,text="Salary",font=("Arial",18,"bold"))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry = CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
salaryEntry.grid(row=5,column=1)


rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)
window.mainloop()