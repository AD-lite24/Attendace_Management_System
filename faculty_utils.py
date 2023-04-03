import mysql.connector
from tkinter import *
import window_utils
import utils

class UniversityFaculty():

    def __init__(self, connection, master) -> None:
        self.connection = connection
        self.master = master

    