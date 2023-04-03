from tkinter import *
from admin_utils import UniversityAdmin

class InterfaceWindow(Toplevel):
    
    def __init__(self, master, connection):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry(master.geometry())
        self.master = master
        self.connection = connection

        Label(self, text='Welcome', font='ar 15 bold', foreground='red').pack(side=TOP, pady=10)

        Button(self, text='Admin', command=self.admin_win).pack(pady=15)
        Button(self, text='Faculty', command=self.faculty_win).pack(pady=15)
    

    def admin_win(self):

        new_win = Toplevel(master=self)
        new_win.title('Admin functions')
        new_win.geometry(self.geometry())
        
        admin = UniversityAdmin(self.connection, self.master)
        Button(new_win, text='Add Student', command=admin.add_student).pack(pady=15)
        Button(new_win, text = 'Remove Student', command = admin.remove_student).pack(pady=15)
        Button(new_win, text='Show Info', command=admin.show_student_info).pack(pady=15)
        Button(new_win, text = 'Register Student in Course', command = admin.register_student_course).pack(pady=15)

    def faculty_win(self):
        pass

        
