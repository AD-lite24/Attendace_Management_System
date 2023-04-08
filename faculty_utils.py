import mysql.connector
from tkinter import *
import window_utils
import utils

class UniversityFaculty():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master


    def student_attendance(self):

        new_win = Toplevel(master=self.master)
        new_win.title('Show Details')
        new_win.geometry(self.master.geometry())
        stu_ID, course_id, date, status = window_utils.populate_mark_student_attendance_gui(new_win=new_win, connection=self.connection)

        if stu_ID == '':
            return
            
        else:
            if status == 'Present':
                status = 1
            elif status == 'Absent':
                status = 0
            utils.student_attendance(self.connection, stu_ID, course_id, date, status)
    
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
        #window_utils.populate_student_report_gui(new_win=new_win)
        Button(new_win, text= 'Check Coursewise Attendance', command=self.coursewise_attendance).pack(pady=15)
        Button(new_win, text = 'Check Attendance Between Two Dates', command=self.attendance_between_dates).pack(pady=15)
        Button(new_win, text = 'Check Student Attendance', command=self.check_student_attendance).pack(pady=15)
        Button(new_win, text='Check Attendance For A Course', command=self.attendance_for_course).pack(pady = 15)
        Button(new_win, text='Check Students Absent without Permission', command=self.absent_without_permission).pack(pady = 15)

    def coursewise_attendance(self):
        new_win = Toplevel(master=self.master)
        new_win.title('Coursewise Attendance')
        new_win.geometry(self.master.geometry())
        date = window_utils.populate_coursewise_attendance_gui(new_win = new_win)
        if date == '':
            return
        else:
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
        if student_id == '':
            return 
        else:
            utils.attendance_between_dates(self.connection, start_date, end_date, student_id)
        
    def attendance_for_course(self):
        new_win = Toplevel(master = self.master)
        new_win.title('Attendance For A Course On Different Dates')
        new_win.geometry(self.master.geometry())
        
        course_id = window_utils.populate_attendance_for_course_gui(new_win = new_win)
        if course_id == '':
            return 
        else:
            utils.attendance_for_course(self.connection, course_id)
            
    def check_leave_permission(self, student_id, date):
        # new_win = Toplevel(master = self.master)
        # new_win.title('Check Leave Permission')
        # new_win.geometry(self.master.geometry())

        if student_id == '':
            return 
        else:
            utils.check_leave_permission(self.connection, student_id, date)

    def update_info(self):
        new_win = Toplevel(master=self.master)
        new_win.title('Update Info')
        new_win.geometry(self.master.geometry())

        ID, new_first_name, new_last_name, new_DOB = window_utils.populate_update_info(new_win=new_win)

        if ID == '':
            return
        else:
            utils.update_faculty_info(self.connection, ID, new_first_name, new_last_name, new_DOB)
    def absent_without_permission(self):
        utils.absent_without_permission(self.connection)