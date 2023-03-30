from tkinter import *

class MainWindow():
    
    def __init__(self) -> None:
        root = Tk()
        root.geometry('500x300')

        Label(root, text='Login', font='ar 15 bold').grid(row = 0, column=3)
        
        username = Label(root, text='Username')
        password = Label(root, text='Password')

        username.grid(row = 1, column= 2)
        password.grid(row = 2, column= 2)

        username_value = StringVar()
        password_value = StringVar()

        self.user_entry = Entry(root, width=25, textvariable=username_value)
        self.pass_entry = Entry(root, width=25, textvariable=password_value, show="*")

        self.user_entry.grid(row=1, column=3)
        self.pass_entry.grid(row=2, column=3)

        Button(text = 'Login', command = self.login).grid(row = 4, column = 2)
        Button(text = 'Forgot Password', command = self.forgot_pass()).grid(row = 4, column = 3)
        
        root.mainloop()

    def login(self):
        
        def delete_text():
            self.user_entry.delete(0, 100)
            self.pass_entry.delete(0, 100)
        
        correct_user = 'admin'
        correct_pass = '1234'
        if self.user_entry.get() != correct_user:
            print("Wrong Username!")
            delete_text()
            
        else:
            if self.pass_entry.get() != correct_pass:
                print('Wrong Password!')
                delete_text()
                
            else:
                print('Login Succesful!')


    def forgot_pass(self):
        pass

    

if __name__ == '__main__':


    print('Starting')
    window = MainWindow()

