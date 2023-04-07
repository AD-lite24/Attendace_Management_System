from tkinter import *
import utils
from faculty_utils import UniversityFaculty
def populate_add_student_gui(new_win):

    ID = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    dept = StringVar()
    DOB = StringVar()
    

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
    Button(master=new_win, text='Cancel', command=new_win.destroy).grid(row=5, column=0, pady=5)

    new_win.grab_set()
    new_win.wait_window()

    
    return ID.get(), first_name.get(), last_name.get(), dept.get(), DOB.get()
    
    

#Add other gui functions here
#*******************************************#

def populate_remove_student_gui(new_win):

    ID = StringVar()
    
    stu_id = Label(new_win, text='ID:', foreground='green')
    stu_id.pack()

    e_id = Entry(new_win, width=25, textvariable=ID)
    e_id.pack()

    Button(master=new_win, text='Submit', command=new_win.destroy).pack()
    Button(master=new_win, text='Cancel', command=new_win.destroy).pack()


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
    Button(master=new_win, text='Cancel', command=new_win.destroy).pack()

    new_win.grab_set()
    new_win.wait_window()

    return ID.get()
    
def populate_register_student_gui(new_win, connection):

    Student_id = StringVar()
    Course_id = StringVar()
    Date = StringVar()

    stu_id = Label(new_win, text='ID:', foreground='green')
    stu_id.grid(row = 0, column=0, pady = 5)

    e_id = Entry(new_win, width=25, textvariable=Student_id)
    e_id.grid(row = 0, column = 1, pady = 5)
    
    cou_id = Label(new_win, text='COURSE ID:', foreground='green')
    cou_id.grid(row = 1, column=0, pady = 5)

    e_cid = Entry(new_win, width=25, textvariable=Course_id)
    e_cid.grid(row = 1, column = 1, pady = 5)
    dateL = Label(new_win, text = 'DATE:', foreground = 'green')
    dateL.grid(row = 2, column = 0, pady = 5)
    dateE = Entry(new_win, width = 25, textvariable=Date)
    dateE.grid(row = 2, column = 1, pady = 5)
    options = StringVar()
    options.set("Null")
    markAtt = Label(new_win, text = "Select", width = 10, foreground='green')
    markAtt.grid(row = 3, column = 0)
    AttSelect = OptionMenu(new_win, options, "Null", "Present", "Absent")
    AttSelect.grid(row = 3, column = 1)

    Button(master=new_win, text='Check Permission', command = lambda:utils.check_student_leave_permission(connection, Student_id.get(), Date.get())).grid(row = 4, column = 2, pady=5)
    Button(master=new_win, text='Register', command=new_win.destroy).grid(row = 4, column=1, pady=5)
    Button(master=new_win, text='Cancel', command=new_win.destroy).grid(row=4, column=0, pady=5)
    Note = Label(new_win, text = 'YYYY-MM-DD', foreground='red')
    Note.grid(row = 2, column = 2, pady = 5)
    new_win.grab_set()
    new_win.wait_window()
    
    return Student_id.get(), Course_id.get(), Date.get(), options.get()

def populate_employee_attendance_gui(new_win, connection):

    Employee_id = StringVar()
    Date = StringVar()
    emp_id = Label(new_win, text='ID:', foreground='green')
    emp_id.grid(row = 0, column=0, pady = 5)

    e_id = Entry(new_win, width=25, textvariable=Employee_id)
    e_id.grid(row = 0, column = 1, pady = 5)
    
    dateL = Label(new_win, text = 'DATE:', foreground = 'green')
    dateL.grid(row = 1, column = 0, pady = 5)
    dateE = Entry(new_win, width = 25, textvariable=Date)
    dateE.grid(row = 1, column = 1, pady = 5)
    Note = Label(new_win, text='YYYY-MM-DD', foreground='red')
    Note.grid(row=1, column=2, pady=5)
    
    Button(master=new_win, text='Mark Attendance', command=new_win.destroy).grid(row = 2, column=0, pady=5)
    Button(master=new_win, text='Check permission', command=lambda:utils.check_employee_leave_permission(connection, Employee_id.get(), Date.get())).grid(row=2, column=1)

    new_win.grab_set()
    new_win.wait_window()
    
    return Employee_id.get(), Date.get()
    
def populate_student_attendance_gui(new_win):
    Course_id = StringVar()
    c_id = Label(new_win, text = 'Course ID:', foreground='green')
    c_id.grid(row = 0, column = 0, pady = 5)
    
    c_id = Entry(new_win, width = 25, textvariable=Course_id)
    c_id.grid(row = 0, column = 1, pady = 5)
    Button(master=new_win, text='Show Attendance', command=new_win.destroy).grid(row = 1, column=1, pady=5)
    new_win.grab_set()
    new_win.wait_window()
    
    return Course_id.get()

# def populate_student_report_gui(new_win):
#     Button(new_win, text= 'Check Coursewise Attendance', command=faculty.coursewise_attendance).pack(pady=15)
#     Button(new_win, text = 'Check Attendance Between Two Dates', command=faculty.attendance_between_dates).pack(pady=15)
#     Button(master=new_win, text='Trend 3').pack()
#     Button(master=new_win, text='Trend 4').pack()


def populate_coursewise_attendance_gui(new_win):
    Date = StringVar()
    dateL = Label(new_win, text = 'DATE:', foreground = 'green')
    dateL.grid(row = 0, column = 0, pady = 5)
    dateE = Entry(new_win, width = 25, textvariable=Date)
    dateE.grid(row = 0, column = 1, pady = 5)
    Button(master=new_win, text='Check Coursewise Attendance', command=new_win.destroy).grid(row = 1, column=1, pady=5)
    Note = Label(new_win, text = 'Please enter date in YYYY-MM-DD format', foreground='red')
    Note.grid(row = 2, column = 0, pady = 5)
    new_win.grab_set()
    new_win.wait_window() 
    return Date.get()

def populate_faculty_leave_gui(new_win):

    Label(new_win, text='ID:', foreground='green').grid(row=0, column=0, padx=15, pady=15)
    Label(new_win, text='Date:', foreground='green').grid(row=1, column=0, padx=15, pady=15)

    Date = StringVar()
    ID = StringVar()

    e_date = Entry(new_win, width=25, textvariable=Date)
    e_date.grid(row=1, column=1, padx=15, pady=15)
    e_ID = Entry(new_win, width=25, textvariable=ID)
    e_ID.grid(row=0, column=1, padx=15, pady=15)

    Button(new_win, text='Submit', command=new_win.destroy).grid(row=2, column=0, padx=50)
    new_win.grab_set()
    new_win.wait_window()

    return Date.get(), ID.get()

def populate_add_faculty_gui(new_win):

    ID = StringVar()
    Name = StringVar()
    DOB = StringVar()
    Dept = StringVar()
    Pwd = StringVar()
    Colour = StringVar()

    Label(new_win, text='ID:', foreground='green').grid(row=0, column=0, padx=15, pady=5)
    Label(new_win, text='Name:', foreground='green').grid(row=1, column=0, padx=15, pady=5)
    Label(new_win, text='DOB:', foreground='green').grid(row=2, column=0, padx=15, pady=5)
    Label(new_win, text='Dept:', foreground='green').grid(row=3, column=0, padx=15, pady=5)
    Label(new_win, text='Password:', foreground='green').grid(row=4, column=0, padx=15, pady=5)
    Label(new_win, text='Fav colour:', foreground='green').grid(row=5, column=0, padx=15, pady=5)

    e_ID = Entry(new_win, width=25, textvariable=ID)
    e_ID.grid(row=0, column=1, padx=15)
    e_name = Entry(new_win, width=25, textvariable=Name)
    e_name.grid(row=1, column=1, padx=15)
    e_DOB = Entry(new_win, width=25, textvariable=DOB)
    e_DOB.grid(row=2, column=1, padx=15)
    e_dept = Entry(new_win, width=25, textvariable=Dept)
    e_dept.grid(row=3, column=1, padx=15)
    e_Pwd = Entry(new_win, width=25, textvariable=Pwd)
    e_Pwd.grid(row=4, column=1, padx=1)
    e_colour = Entry(new_win, width=25, textvariable=Colour)
    e_colour.grid(row=5, column=1, padx=15)

    Button(new_win, text='Submit', command=new_win.destroy).grid(row=6, column=0)
    new_win.grab_set()
    new_win.wait_window()

    return ID.get(), Name.get(), DOB.get(), Dept.get(), Pwd.get(), Colour.get()
    

def populate_attendance_between_dates_gui(new_win):

    StartDate = StringVar()
    EndDate = StringVar()
    StudentID = StringVar()

    date1L = Label(new_win, text = 'START DATE:', foreground = 'green')
    date1L.grid(row = 0, column = 0, pady = 5)
    date1E = Entry(new_win, width = 25, textvariable=StartDate)
    date1E.grid(row = 0, column = 1, pady = 5)
    date2L = Label(new_win, text = 'END DATE:', foreground = 'green')
    date2L.grid(row = 1, column = 0, pady = 5)
    date2E = Entry(new_win, width = 25, textvariable=EndDate)
    date2E.grid(row = 1, column = 1, pady = 5)
    Stu_ID = Label(new_win, text = 'STUDENT ID:', foreground = 'green')
    Stu_ID.grid(row = 2, column = 0, pady = 5)
    Stu_IDe = Entry(new_win, width = 25, textvariable=StudentID)
    Stu_IDe.grid(row = 2, column = 1, pady = 5)

    Button(master=new_win, text='Check Attendance', command=new_win.destroy).grid(row = 3, column=1, pady=5)

    Note = Label(new_win, text = 'Please enter date in YYYY-MM-DD format', foreground='red')
    Note.grid(row = 4, column = 0, pady = 5)

    new_win.grab_set()
    new_win.wait_window() 

    return StartDate.get(), EndDate.get(), StudentID.get()

def populate_attendance_for_course_gui(new_win):
    Course_id = StringVar()
    course_id = Label(new_win, text = 'Course ID:', foreground = 'green')
    course_id.grid(row = 0, column = 0, pady = 5)
    course_id_Entry = Entry(new_win, width = 25,textvariable=Course_id)
    course_id_Entry.grid(row = 0, column = 1, pady = 5)
    Button(master=new_win, text='Check Attendance on Different Dates', command=new_win.destroy).grid(row = 2, column=1, pady=5)    
    new_win.grab_set()
    new_win.wait_window() 
    return Course_id.get()

def populate_student_leave_gui(new_win):
    
    ID = StringVar()
    Date = StringVar()

    Label(new_win, text='ID:', foreground = 'green').grid(row = 0, column = 0, pady=15)
    Label(new_win, text='Date:', foreground='green').grid(row=1, column=0, pady=15)

    e_ID = Entry(new_win, width=25, textvariable=ID)
    e_ID.grid(row=0, column=1, padx=10, pady=15)
    e_date = Entry(new_win, width=25, textvariable=Date)
    e_date.grid(row=1, column=1, padx=10, pady=15)

    Button(master=new_win, text='Submit', command=new_win.destroy).grid(row = 3, column=1, pady=5)
   
    new_win.grab_set()
    new_win.wait_window()

    return ID.get(), Date.get()

