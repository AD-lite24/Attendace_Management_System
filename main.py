from tkinter import *
import mysql.connector
from mysql.connector import Error
from interface import InterfaceWindow

class MainWindow():
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('500x300')

        Label(self.root, text='Login', font='ar 15 bold').grid(row = 0, column=3)
        
        username = Label(self.root, text='Username')
        password = Label(self.root, text='Password')

        username.grid(row = 1, column= 2)
        password.grid(row = 2, column= 2)

        username_value = StringVar()
        password_value = StringVar()

        self.user_entry = Entry(self.root, width=25, textvariable=username_value)
        self.pass_entry = Entry(self.root, width=25, textvariable=password_value, show="*")

        self.user_entry.grid(row=1, column=3)
        self.pass_entry.grid(row=2, column=3)

        Button(text = 'Login', command = self.login).grid(row = 4, column = 2)
        Button(text = 'Forgot Password', command = self.forgot_pass).grid(row = 4, column = 3)

        #For quick connection remove later!!
        self.connect('root', '24112003')
        
        self.root.mainloop()

    def login(self):
        
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
                self.connect(self.user_entry.get(), self.pass_entry.get())
                new = InterfaceWindow(self.root)


    def forgot_pass(self):
        pass
    

    def connect(self, user, pwd):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 user=user,
                                                 password=pwd)

            if connection.is_connected():

                mycursor = connection.cursor()
                mycursor.execute('CREATE DATABASE IF NOT EXISTS university;')
                mycursor.execute('USE university;')
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print('Error while connecting to mysql', e)

    

if __name__ == '__main__':


    print('Starting')
    window = MainWindow()

