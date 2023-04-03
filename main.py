from tkinter import *
import utils
import mysql.connector
from mysql.connector import Error
from interface import InterfaceWindow

class MainWindow():
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('500x300')

        Label(self.root, text='Login', font='ar 15 bold', foreground='blue').grid(row = 0, column=0)
        
        username = Label(self.root, text='Username', foreground='green')
        password = Label(self.root, text='Password', foreground='green')

        username.grid(row = 1, column= 0, pady=15)
        password.grid(row = 2, column= 0, pady=15)


        self.user_entry = Entry(self.root, width=25)
        self.pass_entry = Entry(self.root, width=25, show="*")

        self.user_entry.grid(row=1, column=1, padx=5, pady=15)
        self.pass_entry.grid(row=2, column=1, padx=5, pady=15)

        Button(text = 'Login', command = self.__login).grid(row = 3, column = 0, pady=15)
        Button(text = 'Forgot Password', command = self.__forgot_pass).grid(row = 3, column = 1, pady=15)

        #For quick connection remove later!!
        self.__connect('root', '21012003')
        
        self.root.mainloop()

    def __login(self):

        #AUTO LOGIN FOR TESTING REMOVE LATER
        connection = self.__connect(self.user_entry.get(), self.pass_entry.get())
        new = InterfaceWindow(self.root, connection)
        
        def delete_text():
            self.user_entry.delete(0, 100)
            self.pass_entry.delete(0, 100)
        
        correct_user = 'root'
        correct_pass = '24112003'
        if self.user_entry.get() != correct_user:
            print("Wrong Username!")
            delete_text()
            
        else:
            if self.pass_entry.get() != correct_pass:
                print('Wrong Password!')
                delete_text()
                
            else:
                print('Login Succesful!')
                connection = self.__connect(self.user_entry.get(), self.pass_entry.get())
                utils.init_schema(connection=connection)
                new = InterfaceWindow(self.root, connection)


    def __forgot_pass(self):
        pass
    

    def __connect(self, user, pwd):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 user=user,
                                                 password=pwd)

            if connection.is_connected():

                mycursor = connection.cursor()
                mycursor.execute('CREATE DATABASE IF NOT EXISTS university_a;')
                mycursor.execute('USE university_a;')
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                return connection

        except Error as e:
            print('Error while connecting to mysql', e)

    

if __name__ == '__main__':

    print('Starting')
    window = MainWindow()

