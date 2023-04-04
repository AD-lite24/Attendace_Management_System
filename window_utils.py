from tkinter import *
import utils

def populate_add_student_gui(new_win):

    ID = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    dept = StringVar()
    DOB = StringVar()
    kill = False

    def setKill():
        kill = True
        new_win.destroy()

    stu_first_name = Label(new_win, text='First name:', foreground='green')
    stu_first_name.grid(row=0, column=0, pady=5)

    e_first_name = Entry(new_win, width=25, textvariable=first_name)
    e_first_name.grid(row=0, column=1, pady=5)

    stu_last_name = Label(new_win, text='Last name:', foreground='green')
    stu_last_name.grid(row=1, column=0, pady=5)

    e_last_name = Entry(new_win, width=25, textvariable=last_name)
    e_last_name.grid(row=1, column=1, pady=5)

    stu_ID = Label(new_win, text='ID:', foreground='green')
    stu_ID.grid(row=2, column=0, pady=5)

    e_ID = Entry(new_win, width=25, textvariable=ID)
    e_ID.grid(row=2, column=1, pady=5)

    stu_dept = Label(new_win, text='Department:', foreground='green')
    stu_dept.grid(row=3, column=0, pady=5)

    e_dept = Entry(new_win, width=25, textvariable=dept)
    e_dept.grid(row=3, column=1, pady=5)

    stu_DOB = Label(new_win, text='DOB:', foreground='green')
    stu_DOB.grid(row=4, column=0, pady=5)

    e_DOB = Entry(new_win, width=25, textvariable=DOB)
    e_DOB.grid(row=4, column=1, pady=5)

    Button(master=new_win, text='Submit', command=new_win.destroy).grid(row = 5, column=1, pady=5)
    Button(master=new_win, text='Cancel', command=setKill).grid(row=5, column=0, pady=5)

    new_win.grab_set()
    new_win.wait_window()

    if not kill:
        return ID.get(), first_name.get(), last_name.get(), dept.get(), DOB.get()
    else:
        return None
    

#Add other gui functions here
#*******************************************#

def populate_remove_student_gui(new_win):

    ID = StringVar()
    
    stu_id = Label(new_win, text='ID:', foreground='green')
    stu_id.pack()

    e_id = Entry(new_win, width=25, textvariable=ID)
    e_id.pack()

    Button(master=new_win, text='Submit', command=new_win.destroy).pack()

    new_win.grab_set()
    new_win.wait_window()

    return ID.get()

def populate_student_info_gui(new_win):
    
    ID = StringVar()

    stu_id = Label(new_win, text='ID:', foreground='green')
    stu_id.pack()

    e_id = Entry(new_win, width=25, textvariable=ID)
    e_id.pack()

    Button(master=new_win, text='Submit', command=new_win.destroy).pack()

    new_win.grab_set()
    new_win.wait_window()

    return ID.get()
    
def populate_register_student_gui(new_win):
    
    Student_id = StringVar()
    Course_id = StringVar()
    
    stu_id = Label(new_win, text='ID:', foreground='green')
    stu_id.grid(row = 0, column=0, pady = 5)

    e_id = Entry(new_win, width=25)
    e_id.grid(row = 0, column = 1, pady = 5)
    
    cou_id = Label(new_win, text='COURSE ID:', foreground='green')
    cou_id.grid(row = 1, column=0, pady = 5)

    e_cid = Entry(new_win, width=25)
    e_cid.grid(row = 1, column = 1, pady = 5)
    
    Button(master=new_win, text='Register', command=new_win.destroy).grid(row = 2, column=1, pady=5)
    new_win.grab_set()
    new_win.wait_window()
    
    return Student_id.get(), Course_id.get()
    


