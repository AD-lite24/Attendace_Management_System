import mysql.connector
from tkinter import *
import window_utils
import utils

class UniversityStudent():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master

    def apply_for_leave(self):
        new_win = Toplevel(self.master)
        new_win.title('Leave application')
        new_win.geometry(self.master.geometry())

        ID, date = window_utils.populate_student_leave_gui(new_win=new_win)

        if ID == '':
            return
        else:
            utils.student_apply_for_leave(self.connection, ID, date)
    def check_attendance(self):
        new_win = Toplevel(self.master)
        new_win.title('Check Attendance')
        new_win.geometry(self.master.geometry())
        
        start_date, end_date, stu_ID = window_utils.populate_attendance_between_dates_gui(new_win = new_win)
        
        if stu_ID == '':
            return
        else:
            utils.attendance_between_dates(self.connection, start_date, end_date, stu_ID)