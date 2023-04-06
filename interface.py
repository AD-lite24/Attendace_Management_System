from tkinter import *
from admin_utils import UniversityAdmin
from faculty_utils import UniversityFaculty
import mysql.connector

class InterfaceWindow(Toplevel):
    
    def __init__(self, master, connection):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry(master.geometry())
        self.master = master
        self.connection = connection
        self.validate = False


        Label(self, text='Welcome', font='ar 15 bold', foreground='red').pack(side=TOP, pady=10)

        Button(self, text='Admin', command=self.admin_login_win).pack(pady=15)
        Button(self, text='Faculty', command=self.faculty_login_win).pack(pady=15)
    

    def admin_win(self):

        new_win = Toplevel(master=self)
        new_win.title('Admin functions')
        new_win.geometry(self.geometry())

        admin = UniversityAdmin(self.connection, self.master)
        Button(new_win, text='Add Student', command=admin.add_student).pack(pady=15)
        Button(new_win, text = 'Remove Student', command = admin.remove_student).pack(pady=15)
        Button(new_win, text='Show Info', command=admin.show_student_info).pack(pady=15)
        Button(new_win, text = 'Register Student in Course', command = admin.register_student_course).pack(pady=15)
        Button(new_win, text = 'Mark Employee Attendance', command = admin.employee_attendance).pack(pady=15)

    def faculty_win(self):
        
        new_win = Toplevel(master=self)
        new_win.title('Faculty functions')
        new_win.geometry(self.geometry())

        faculty = UniversityFaculty(self.connection, self.master)

        #Add faculty buttons here

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

        Button(new_win, text='Login', command=lambda:self.admin_login_infra(
            new_win, user_entry.get(), pass_entry.get())).grid(row=3, column=0)

        Button(new_win, text='Forgot Password').grid(row=3, column=1)

    def faculty_login_win(self):
        
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

    def admin_login_infra(self, new_win, username, password):
        
        self.admin_win()
        new_win.destroy()
        return
    
        # mycursor = self.connection.cursor()
        # mycursor.execute(
        #     f"""SELECT * FROM admins
        #         WHERE admin_id = '{username}';
        #     """
        # )
        # out = mycursor.fetchone()

        # if (out == None):
        #     print('Admin User not found')
        #     return
        
        # else:
        #     stored_pwd = out[1]

        #     if stored_pwd == password:
        #         print(f'Welcome admin {username}')
        #         new_win.destroy()
        #         self.admin_win()
        #         return
        #     else:
        #         print('Wrong Password!')
        #         return

    def faculty_login_infra(self, new_win, username, password):
        self.faculty_win()
        new_win.destroy()
        return
