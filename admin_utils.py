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

    def register_student_course(self):

        new_win = Toplevel(master=self.master)
        new_win.title('Show Details')
        new_win.geometry(self.master.geometry())

        stu_ID, course_id = window_utils.populate_register_student_gui(new_win=new_win)
        if stu_ID == '':
            return
        else:
            utils.register_course_student(self.connection, stu_ID, course_id)


    #Add other operations here
    #************************************************#

    #Other trends that need to be shown
    
    
    