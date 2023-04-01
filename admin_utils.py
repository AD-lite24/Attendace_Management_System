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

        ID, name, dept, DOB = window_utils.populate_add_student(new_win=new_win)
        utils.add_student(ID, name, dept, DOB)

    def remove_student():
        pass

    def show_student_info():
        pass

    #Add other operations here
    #************************************************#

    
    
    
    