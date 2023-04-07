import mysql.connector
from datetime import datetime 
def run_queries(connection, filename):

    mycursor = connection.cursor()

    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                mycursor.execute(command)
                connection.commit()
        except IOError as msg:
            print ("Command skipped: ", msg)
    
    mycursor.close()

def add_student_query(connection, ID, first_name, last_name, dept, DOB):

    print('query ', connection)
    mycursor = connection.cursor()
    query = f"""INSERT INTO students
            VALUES ('{ID}','{first_name}','{last_name}','{DOB}','{dept}');
            """
    
    mycursor.execute(query)
    connection.commit()
    mycursor.close()

def remove_student_query(connection, ID):
    
    mycursor = connection.cursor()
    
    query = f"""DELETE FROM students
            WHERE Student_id = '{ID}';
            """

    mycursor.execute(query)
    connection.commit()
    mycursor.close()

def info_student_query(connection, ID):

    mycursor = connection.cursor()

    query = f"""SELECT * FROM students
            WHERE Student_id = '{ID}';
            """

    mycursor.execute(query)
    out = mycursor.fetchall()
    out = out[0]

    print('ID: ', out[0])
    print('Name: ', out[1], ' ', out[2])
    print('DOB: ', out[3])
    print('Department: ', out[4])

    connection.commit()
    mycursor.close()

def register_course_student(connection, stu_ID, course_ID, date, status):

    mycursor = connection.cursor()
    mycursor.execute(f"INSERT INTO Takes values ('{stu_ID}', '{course_ID}', '{date}', '{status}');")
    connection.commit()
    mycursor.close()


def employee_attendance(connection, emp_ID, date):
    mycursor = connection.cursor()
    mycursor.execute(f"INSERT INTO Employee_Records values ('{emp_ID}', '{date}', True);")
    connection.commit()
    mycursor.close()
    
def check_student_attendance(connection, course_id):
    mycursor = connection.cursor()
    mycursor.execute(f"Select Student_id, count(*) as count from takes where Course_id = '{course_id}' and present = True group by Student_id order by count;")
    out = mycursor.fetchall()
    for i in out:
        print("Student id: ", i[0])
        print("Attendance count: ", i[1])
    if not out:
        print("No Student is registered in this course or no student has attended any class of this course")
        
    connection.commit()
    mycursor.close()

def faculty_apply_for_leave(connection, date, faculty_id):
    mycursor = connection.cursor()
    mycursor.execute(
        f"""INSERT IGNORE INTO Employee_records
            VALUES 
                ('{faculty_id}', '{date}', NULL, True)
        """
    )
    print(f"Successfuly applied for leave on {date}")
    connection.commit()
    mycursor.close()

def student_apply_for_leave(connection, student_id, date):
    print(student_id, date)
    mycursor = connection.cursor()
    mycursor.execute(
        f"""INSERT INTO student_permission
            VALUES
                ('{student_id}', '{date}', True);
        """
    )
    print(f"Successfuly applied for leave on {date}")
    connection.commit()
    mycursor.close()
    
def coursewise_attendance(connection, date):
    mycursor = connection.cursor()
    mycursor.execute(f"Select Course_id, count(*) as count from takes where present = True AND date = '{date}' group by Course_id order by count desc;")
    out = mycursor.fetchall()
    for i in out:
        print("Course_id: ", i[0], "; No of Students: ", i[1])

    connection.commit()
    mycursor.close()

def add_faculty(connection, emp_id, name, dob, dept_name, password, fav_colour):
    mycursor = connection.cursor()
    mycursor.execute(
        f"""INSERT IGNORE INTO employees
            VALUES
                ('{emp_id}', '{name}', '{dob}');
        """
    )
    mycursor.execute(
        f"""INSERT IGNORE INTO instructors
            VALUES
                ('{emp_id}', '{dept_name}', '{password}', '{fav_colour}');
        """
    )
    connection.commit()
    mycursor.close()


def attendance_between_dates(connection, start_date, end_date, stu_id):
    mycursor = connection.cursor()
    mycursor.execute(f"select course_id, count(*) as count from takes where student_id = '{stu_id}' AND date BETWEEN '{start_date}' AND '{end_date}' AND present = True group by course_id order by count desc;")
    out = mycursor.fetchall()
    for i in out:
        print("Course_id: ", i[0])
        print("No of Days Present: ", i[1])
    connection.commit()
    mycursor.close()
    
    
def attendance_for_course(connection, course_id):
    mycursor = connection.cursor()
    mycursor.execute(f"select date, count(*) as 'No of students present' from takes where course_id = '{course_id}' and present = True group by date order by date;")
    out = mycursor.fetchall()
    for i in out:
        print("Date: ", i[0])
        print("No of Students Present: ", i[1])
    connection.commit()
    mycursor.close()
    
def check_student_leave_permission(connection, student_id, date):
    mycursor = connection.cursor()
    mycursor.execute(f"select permission from Student_permission where date = '{date}' AND Student_id = '{student_id}';")
    out = mycursor.fetchall()
    try:
        out = out[0]
        print("Leave has been applied") if out[0] == 1 else print(
            "Leave not applied")

    except:
        print('Leave not applied')

def check_employee_leave_permission(connection, emp_id, date):
    mycursor = connection.cursor()
    mycursor.execute(
        f"select permission from employee_records where date = '{date}' AND Emp_id = '{emp_id}';")
    out = mycursor.fetchall()
    try:
        out = out[0]
        print("Leave has been applied") if out[0] == 1 else print(
            "Leave not applied")

    except:
        print('Leave not applied')


    #Add other utility queries here
    #***************************************#
