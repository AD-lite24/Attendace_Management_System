from tkinter import *
from admin_utils import UniversityAdmin
from faculty_utils import UniversityFaculty
from student_utils import UniversityStudent
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
        Button(self, text='Student', command=self.student_win).pack(pady=15)

    def admin_win(self):

        new_win = Toplevel(master=self)
        new_win.title('Admin functions')
        new_win.geometry(self.geometry())

        admin = UniversityAdmin(self.connection, self.master)

        Button(new_win, text='Add Student', command=admin.add_student).pack(pady=15)
        Button(new_win, text = 'Add faculty', command = admin.add_faculty).pack(pady=15)
        Button(new_win, text = 'Remove Student', command = admin.remove_student).pack(pady=15)
        Button(new_win, text='Show Info', command=admin.show_student_info).pack(pady=15)  
        Button(new_win, text = 'Mark Employee Attendance', command = admin.employee_attendance).pack(pady=15)

    def faculty_win(self):

        new_win = Toplevel(master=self)
        new_win.title('Faculty functions')
        new_win.geometry(self.geometry())
        faculty = UniversityFaculty(self.connection, self.master)

        Button(new_win, text = 'Mark attendance', command = faculty.student_attendance).pack(pady=15)
        Button(new_win, text= 'Reports', command=faculty.get_student_reports).pack(pady=15)
        Button(new_win, text='Update Info', command=faculty.update_info).pack(pady=15)
        Button(new_win, text= 'Leave permission', command=faculty.apply_for_leave).pack(pady=15)


        
    def student_win(self):

        new_win = Toplevel(self)
        new_win.title('Student options')
        new_win.geometry(self.geometry())
        student = UniversityStudent(self.connection, self.master)

        Button(new_win, text='Apply for leave', command=student.apply_for_leave).pack(pady=15)
        Button(new_win, text='Check Attendance', command=student.check_attendance).pack(pady=15)
        Button(new_win, text='Update Info', command=student.update_info).pack(pady=15)


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

        Button(new_win, text='Forgot Password', command=lambda:self.forgot_pass_win('admins')).grid(row=3, column=1)

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
        Button(new_win, text='Forgot Password', command=lambda:self.forgot_pass_win('instructors')).grid(
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
        # self.connection.commit()
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

    def forgot_pass_win(self, type):

        new_win = Toplevel(master=self)
        new_win.title('Forgot Password')
        new_win.geometry(self.geometry())

        Label(new_win, text='Enter Username', foreground='green').grid(row=0, column=0, padx=15, pady=15)
        e_username = Entry(new_win, width=25)
        e_username.grid(row=0, column=1, padx=15, pady=15)
        Label(new_win, text='Favorite color', foreground='green').grid(row=1, column=0, padx=15, pady=15)
        e_colour = Entry(new_win, width=25)
        e_colour.grid(row=1, column=1, padx=15, pady=15)

        Button(new_win, text='Verify', command=lambda:self.forgot_pass_infra(
            new_win, e_username.get(), e_colour.get(), type 
        )).grid(row=3, column=0)
        
    
    def forgot_pass_infra(self, new_win, username, colour, type):

        mycursor = self.connection.cursor(buffered = True)
        
        if type == 'instructors':
            mycursor.execute(
                f"""SELECT * FROM {type}
                    WHERE emp_id = '{username}';
                """
            )
        else:
            mycursor.execute(
                f"""SELECT * FROM {type}
                    WHERE admin_id = '{username}';
                """
            )

        self.connection.commit()
        out = mycursor.fetchall()
        

        if (out == None):
            print(f'{type} not found')
            return
        
        else:
            out = out[0]
            stored_fav_colour = out[3] if type == 'instructors' else out[2]

            if stored_fav_colour == colour:
                self.update_password_win(new_win, username, type)
                mycursor.close()
                self.faculty_win()
                new_win.destroy()
                return
            else:
                print('Wrong safe key')
                mycursor.close()
                return

    def update_password_win(self, master, username, type):
        
        new_win = Toplevel(master)
        new_win.title('Enter new password')
        new_win.geometry(master.geometry())
        new_pass = StringVar()

        Label(new_win, text='Enter New Password', foreground='green').pack(pady=20)
        e_pass = Entry(new_win, width=25, textvariable=new_pass)
        e_pass.pack()
        Button(new_win, text='Submit', command=new_win.destroy).pack()
        new_win.grab_set()
        new_win.wait_window()
        mycursor = self.connection.cursor()

        if type == 'instructors':
            mycursor.execute(
                f"""UPDATE {type}
                    SET
                        Password = '{new_pass.get()}'
                    WHERE
                        Emp_id = '{username}';
                """
            )
        else:
            mycursor.execute(
                f"""UPDATE {type}
                    SET
                        Password = '{new_pass.get()}'
                    WHERE
                        admin_id = '{username}';
                """
            )
        self.connection.commit()
        print('Password updated successfully')
        mycursor.close()
        return

