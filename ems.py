from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

def clear():
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('web developer')
    genderBox.set('Male')
    salaryEntry.delete(0, END)

def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])


def treeview_data():
    employees = database.fetch_employee()
    tree.delete(*tree.get_children())

    for employee in employees:
        tree.insert('',END,values=employee)

def add_employee():
    if nameEntry.get() == "" or phoneEntry.get() == "" or roleBox.get() == "" or genderBox.get() == "" or salaryEntry.get() == "" or idEntry.get() == "":
        messagebox.showerror("Error", "Please fill all fields")

    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error", "id already exists")

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data Added Successfully")

window = CTk()
window.title("Employee Management System")
window.geometry("930x600+100+100")
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

search_options = ['Id','Name','Contact','Role','Gender','Salary']
searchBox = CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.set('Search By')
searchBox.grid(row=0,column=0)

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton = CTkButton(rightFrame,text='Search',width=100)
searchButton.grid(row=0,column=2)

showallButton = CTkButton(rightFrame,text='Show All',width=100)
showallButton.grid(row=0,column=3,pady=5)

tree = ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns'] = ('Id','Name','Contact','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Contact',text='Contact')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Contact',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=140)

style = ttk.Style()
style.configure('Treeview.Heading',font=("Arial",18,"bold"))
style.configure('Treeview',font=("Arial",18,"bold"),rowheight=30,background="#161C30",foreground="white")

scrollbar = ttk.Scrollbar(rightFrame,orient=VERTICAL)
scrollbar.grid(row=1,column=4,sticky='ns')

buttonFrame = CTkFrame(window,fg_color="#161C30")
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton = CTkButton(buttonFrame,text="New Employee",font=("Arial",15,"bold"),width=160,corner_radius=15)
newButton.grid(row=0,column=0,pady=5,padx=5)

updateButton = CTkButton(buttonFrame,text="Update Employee",font=("Arial",15,"bold"),width=160,corner_radius=15)
updateButton.grid(row=0,column=1,pady=5,padx=5)

deleteButton = CTkButton(buttonFrame,text="Delete Employee",font=("Arial",15,"bold"),width=160,corner_radius=15)
deleteButton.grid(row=0,column=2,pady=5,padx=5)

addButton = CTkButton(buttonFrame,text="Add Employee",font=("Arial",15,"bold"),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton = CTkButton(buttonFrame,text="Delete All",font=("Arial",15,"bold"),width=160,corner_radius=15)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()
window.bind('<ButtonRelease>',selection)

window.mainloop()
