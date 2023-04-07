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
        stu_ID, course_id, date, status = window_utils.populate_register_student_gui(new_win=new_win)

        if stu_ID == '':
            return
        else:
            utils.register_course_student(self.connection, stu_ID, course_id, date, status)
    
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
        
        new_win = Toplevel(master=self.master)
        new_win.title('Student reports')
        new_win.geometry(self.master.geometry())

        window_utils.populate_student_report_gui(new_win=new_win)
       

    def coursewise_attendance(self):
        new_win = Toplevel(master=self.master)
        new_win.title('Coursewise Attendance')
        new_win.geometry(self.master.geometry())
        date = window_utils.populate_coursewise_attendance_gui(new_win = new_win)
        utils.coursewise_attendance(self.connection, date)
        
    def apply_for_leave(self):

        new_win = Toplevel(master=self.master)
        new_win.title('Apply for faculty leave')
        new_win.geometry(self.master.geometry())

        date, faculty_id = window_utils.populate_faculty_leave_gui(new_win=new_win)   

        if date == '':
            return
        else:
            utils.faculty_apply_for_leave(self.connection, date, faculty_id) 

    def attendance_between_dates(self):
        new_win = Toplevel(master=self.master)
        new_win.title('Attendance Between Two Dates')
        new_win.geometry(self.master.geometry())
        
        start_date, end_date, student_id = window_utils.populate_attendance_between_dates_gui(new_win = new_win)
        utils.attendance_between_dates(self.connection, start_date, end_date, student_id)
    