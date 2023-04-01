from tkinter import *
import mysql.connector
from admin_utils import UniversityAdmin

class InterfaceWindow(Toplevel):
    
    def __init__(self, master, connection):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry(master.geometry())
        self.master = master
        self.connection = connection

        Label(self, text='Welcome', font='ar 15 bold', foreground='red').pack(side=TOP, pady=10)

        admin = UniversityAdmin(self.connection, self.master)

        Button(self, text='Add Student', command=admin.add_student).pack(pady=15)
        Button(self, text = 'Remove Student', command = admin.remove_student).pack(pady=15)
        Button(self, text='Show Info', command=admin.show_student_info).pack(pady=15)





        
