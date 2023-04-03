import mysql.connector
from tkinter import *
import window_utils
import utils

class UniversityAdmin():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master
        self.mycursor = self.connection.cursor()

    def add_student(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Add Student')
        new_win.geometry(self.master.geometry())

        ID, first_name, last_name, dept, DOB = window_utils.populate_add_student_gui(new_win=new_win)
        utils.add_student_query(self.connection, ID, first_name, last_name, dept, DOB)


    def remove_student(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Remove Student')
        new_win.geometry(self.master.geometry())

        ID = window_utils.populate_remove_student_gui(new_win=new_win)
        utils.remove_student_query(self.connection, ID)

    def show_student_info(self):
        
        new_win = Toplevel(master=self.master)
        new_win.title('Show Details')
        new_win.geometry(self.master.geometry())

        ID = window_utils.populate_student_info_gui(new_win=new_win)
        utils.info_student_query(self.connection, ID)


    #Add other operations here
    #************************************************#

    #Other trends that need to be shown
    
    
    