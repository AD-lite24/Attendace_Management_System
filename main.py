from tkinter import *
import utils
import mysql.connector
from mysql.connector import Error
from interface import InterfaceWindow

class MainWindow():
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('500x300')

        Label(self.root, text='Login to server', font='ar 15 bold', foreground='blue').grid(row = 0, column=0)
        
        username = Label(self.root, text='Username', foreground='green')
        password = Label(self.root, text='Password', foreground='green')

        username.grid(row = 1, column= 0, pady=15)
        password.grid(row = 2, column= 0, pady=15)

        self.user_entry = Entry(self.root, width=25)
        self.pass_entry = Entry(self.root, width=25, show="*")

        self.user_entry.grid(row=1, column=1, padx=5, pady=15)
        self.pass_entry.grid(row=2, column=1, padx=5, pady=15)

        Button(text = 'Login', command = self.__login).grid(row = 3, column = 0, pady=15)
        Label(self.root, text='NOTE: Enter your root password here', foreground='red').grid(row=4, column=0)
       
        self.root.mainloop()

    def __login(self):
        
        connection = self.__connect(self.user_entry.get(), self.pass_entry.get())
        if connection == None:
            return
        InterfaceWindow(self.root, connection)

    def __connect(self, user, pwd):

        def delete_text():
            self.user_entry.delete(0, 100)
            self.pass_entry.delete(0, 100)

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 user=user,
                                                 password=pwd)

            if connection.is_connected():

                mycursor = connection.cursor()
                mycursor.execute('CREATE DATABASE IF NOT EXISTS university_b;')
                mycursor.execute('USE university_b;')
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                connection.commit()
                mycursor.close()
                utils.init_schema(connection)
                return connection

        except Error as e:
            print('Error while connecting to mysql', e)
            delete_text()
            return

    

if __name__ == '__main__':

    print('Starting')
    window = MainWindow()

