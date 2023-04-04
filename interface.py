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

        Button(self, text='Admin', command=self.admin_login_win).pack(pady=15)
        Button(self, text='Faculty', command=self.facult_login_win).pack(pady=15)
    

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

    def admin_login_win(self):
        
        new_win = Toplevel(master=self)
        new_win.title('Admin login')
        new_win.geometry(self.geometry())

        Label(new_win, text='Login to admin account', font='ar 15 bold',
              foreground='blue').grid(row=0, column=0)

        username = Label(new_win, text='Username', foreground='green')
        password = Label(new_win, text='Password', foreground='green')

        username.grid(row=1, column=0, pady=15)
        password.grid(row=2, column=0, pady=15)

        user_entry = Entry(new_win, width=25)
        pass_entry = Entry(new_win, width=25, show="*")

        user_entry.grid(row=1, column=1, padx=5, pady=15)
        pass_entry.grid(row=2, column=1, padx=5, pady=15)

        Button(new_win, text='Login', command=self.admin_win).grid(row=3, column=0)
        Button(new_win, text='Forgot Password').grid(row=3, column=1)
        

    def facult_login_win(self):
        
        new_win = Toplevel(master=self)
        new_win.title('Faculty login')
        new_win.geometry(self.geometry())

        Label(new_win, text='Login to faculty account', font='ar 15 bold',
              foreground='blue').grid(row=0, column=0)

        username = Label(new_win, text='Username', foreground='green')
        password = Label(new_win, text='Password', foreground='green')

        username.grid(row=1, column=0, pady=15)
        password.grid(row=2, column=0, pady=15)

        user_entry = Entry(new_win, width=25)
        pass_entry = Entry(new_win, width=25, show="*")

        user_entry.grid(row=1, column=1, padx=5, pady=15)
        pass_entry.grid(row=2, column=1, padx=5, pady=15)

        Button(new_win, text='Login', command=self.faculty_win).grid(
            row=3, column=0, pady=15)
        Button(new_win, text='Forgot Password').grid(
            row=3, column=1, pady=15)

    def admin_login_infra():
        pass

    def faculty_login_infra():
        pass