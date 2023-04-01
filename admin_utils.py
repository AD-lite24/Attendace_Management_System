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

        Label(new_win, text='Add Student here', foreground='blue').pack(side= TOP)

        stu_name = Label(new_win, text='Name:', foreground='green').place(relx = 0.1, rely = 0.15, anchor=CENTER)
        stu_ID = Label(new_win, text='ID:', foreground='green').place(relx = 0.1, rely = 0.24, anchor=CENTER)

        e_name = Entry(new_win, width=25).pack(pady = 1)
        e_ID = Entry(new_win, width=25).pack(pady=1)

        # e_name.place(relx=0.3, rely=0.15, anchor=CENTER)
        # e_ID.place(relx=0.3, rely=0.24, anchor=CENTER)


    def remove_student():
        pass
    
    
    