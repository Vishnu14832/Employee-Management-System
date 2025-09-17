import pymysql
from tkinter import messagebox

def connect_database():
    try:
        global mycursor, conn
        conn = pymysql.connect(host='localhost', user='root', password='1234')
        mycursor = conn.cursor()

    except Exception as e:
        messagebox.showerror("Error", f"Database connection failed: {e}")
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute("USE employee_data")
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            Id VARCHAR(20),
            Name VARCHAR(50),
            Contact VARCHAR(15),
            Salary VARCHAR(20),
            Gender VARCHAR(20),
            Role VARCHAR(20)
        )
    """)
    conn.commit()

connect_database()

def insert(id, name, contact, salary, gender, role):
    mycursor.execute('INSERT INTO data values (%s, %s, %s, %s, %s, %s)', (id, name, contact, salary, gender, role))
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id = %s',id)
    result = mycursor.fetchone()
    return result[0] > 0

def fetch_employee():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result


