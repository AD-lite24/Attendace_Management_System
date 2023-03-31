from tkinter import *
import mysql.connector

class InterfaceWindow(Toplevel):
    
    def __init__(self, master):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry(master.geometry())
        
