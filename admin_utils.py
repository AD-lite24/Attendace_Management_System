import mysql.connector
from tkinter import *
import window_utils
import utils

class UniversityAdmin():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master

    def add_student(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Add Student')
        new_win.geometry(self.master.geometry())

        ID, first_name, last_name, dept, DOB = window_utils.populate_add_student_gui(new_win=new_win)

        if ID == '':
            return
        else:
            utils.add_student_query(self.connection, ID, first_name, last_name, dept, DOB)


    def remove_student(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Remove Student')
        new_win.geometry(self.master.geometry())

        ID = window_utils.populate_remove_student_gui(new_win=new_win)
        if ID == '':
            return
        else:
            utils.remove_student_query(self.connection, ID)

    def show_student_info(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Show Details')
        new_win.geometry(self.master.geometry())

        ID = window_utils.populate_student_info_gui(new_win=new_win)
        if ID == '':
            return
        else:
            utils.info_student_query(self.connection, ID)

    def employee_attendance(self):

        new_win = Toplevel(master=self.master)
        new_win.title('Employee Attendance')
        new_win.geometry(self.master.geometry())
        emp_ID, date, status = window_utils.populate_employee_attendance_gui(new_win=new_win, connection=self.connection)
        
        if emp_ID == '':
            return
            
        else:
            if status == 'Present':
                status = 1
            elif status == 'Absent':
                status = 0
            utils.employee_attendance(self.connection, emp_ID, date, status)
            
    def add_faculty(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Add Faculty')
        new_win.geometry(self.master.geometry())
        emp_id, first_name, last_name, dob, dept_name, password, fav_colour = window_utils.populate_add_faculty_gui(new_win=new_win)
        if emp_id == '':
            return
        else:
            utils.add_faculty(self.connection, emp_id, first_name, last_name, dob, dept_name, password, fav_colour)

    #Add other operations here
    #************************************************#

    #Other trends that need to be shown
    
    
    