import mysql.connector
from tkinter import *

class UniversityAdmin():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master

    def add_student(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Add Student')
        new_win.geometry(self.master.geometry())

        stu_name = Label(new_win, text='Name:', foreground='green')
        stu_name.grid(row=0, column=0, pady=5)

        e_name = Entry(new_win, width=25)
        e_name.grid(row=0, column=1, pady=5)

        stu_ID = Label(new_win, text='ID:', foreground='green')
        stu_ID.grid(row=1, column=0, pady=5)

        e_ID = Entry(new_win, width=25)
        e_ID.grid(row=1, column=1, pady=5)

        stu_dept = Label(new_win, text='Department:', foreground='green')
        stu_dept.grid(row=2, column=0, pady=5)

        e_dept = Entry(new_win, width=25)
        e_dept.grid(row=2, column=1, pady=5)

        stu_DOB = Label(new_win, text='DOB:', foreground='green')
        stu_DOB.grid(row=3, column=0, pady=5)

        e_DOB = Entry(new_win, width=25)
        e_DOB.grid(row=3, column=1, pady=5)


    def remove_student():
        pass
    
    
    