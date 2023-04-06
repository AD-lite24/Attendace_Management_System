import mysql.connector
from tkinter import *
import window_utils
import utils

class UniversityFaculty():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master

    def register_student_course(self):

        new_win = Toplevel(master=self.master)
        new_win.title('Show Details')
        new_win.geometry(self.master.geometry())

        stu_ID, course_id = window_utils.populate_register_student_gui(new_win=new_win)

        if stu_ID == '':
            return
        else:
            utils.register_course_student(self.connection, stu_ID, course_id)
    
    def check_student_attendance(self):
        new_win = Toplevel(master=self.master)
        new_win.title('Show Details')
        new_win.geometry(self.master.geometry())

        course_id = window_utils.populate_student_attendance_gui(new_win=new_win)

        if course_id == '':
            return 
        else:     
            utils.check_student_attendance(self.connection, course_id)

    def get_student_reports(self):
        pass
       
            
    