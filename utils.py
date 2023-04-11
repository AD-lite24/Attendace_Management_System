import mysql.connector
from datetime import datetime 
import matplotlib.pyplot as plt 

#Script to run queries from the .sql files
def run_queries(connection, filename, delimiter):

    mycursor = connection.cursor()

    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(delimiter)

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

def student_attendance(connection, stu_ID, course_ID, date, status):

    mycursor = connection.cursor()
    mycursor.execute(f"INSERT INTO Takes values ('{stu_ID}', '{course_ID}', '{date}', {status});")
    connection.commit()
    mycursor.close()  
    if(status==False):
        mycursor = connection.cursor()
        mycursor.execute(f"call check_leave('{stu_ID}', '{date}');")
        out = mycursor.fetchone()    
        if(out!=None):
            out = out[0]
            print(f"Leave has been applied by {stu_ID} for {date}")
        else:
            print(f"No leave has been applied by {stu_ID} for {date}")
        connection.commit()
        mycursor.close()
def employee_attendance(connection, emp_ID, date, status):
    mycursor = connection.cursor()
    mycursor.execute(
        f"""SELECT * FROM Employee_records
            WHERE emp_id = '{emp_ID}' AND date = '{date}';
        """
    )
    out = mycursor.fetchall()
    connection.commit()
    print(out)
    if len(out) == 0:
        print("No leave applied")
        mycursor.execute(
            f"INSERT IGNORE INTO Employee_Records values ('{emp_ID}', '{date}', {status}, False);")
        connection.commit()

    else:
        mycursor.execute(
            f"""UPDATE Employee_records
                SET
                    Present = {status}
                WHERE
                    emp_id = '{emp_ID}' AND date = '{date}';
            """
        )
    print(f'Marked attendance as {status}')

def check_student_attendance(connection, course_id):
    mycursor = connection.cursor()
    mycursor.execute(f"Select Student_id, count(*) as count from takes where Course_id = '{course_id}' group by Student_id order by student_id;")
    out = mycursor.fetchall()
    for i in out:
        mycursor.execute(f"select count(*) as count from takes where student_id = '{i[0]}' and course_id = '{course_id}' and present = True;")
        out2 = mycursor.fetchall()
        if(out2!=None):
            out2 = out2[0]
            print("Student id: ", i[0], ";", "Attendance count: ", out2[0], "; Percentage of Attendance: ", (100*out2[0])/i[1])
        
    if not out:
        print("No Student is registered in this course or no student has attended any class of this course")
        
    connection.commit()
    mycursor.close()

def faculty_apply_for_leave(connection, date, faculty_id):
    mycursor = connection.cursor()
    mycursor.execute(
        f"""INSERT IGNORE INTO Employee_records
            VALUES 
                ('{faculty_id}', '{date}', NULL, True);
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
    mycursor.execute(f"Select Course_id, sum(present) as count from takes where date = '{date}' group by Course_id order by course_id;")
    out = mycursor.fetchall()

    for i in out:
        mycursor.execute(f"select count(*) as count from takes where course_id = '{i[0]}' and date = '{date}';")
        out2 = mycursor.fetchall()
        if(out2!=None):
            out2 = out2[0]
            print("Course id: ", i[0], ";", "Attendance count: ", i[1], "; Percentage of Attendance: ", (100*i[1])/out2[0])
        
    if not out:
        print("Class has not been held for any course on this date or attendance has not been taken")

    courses, number = [i[0] for i in out], [i[1] for i in out]

    fig = plt.figure(figsize=(5, 5))
    plt.bar(courses, number, color='green', width=0.5)
    plt.xlabel("Courses")
    plt.ylabel("Student Attendance")
    plt.title(f"Coursewise attendance of students on a {date}")
    plt.show()

    connection.commit()
    mycursor.close()

def add_faculty(connection, emp_id, first_name, last_name, dob, dept_name, password, fav_colour):
    mycursor = connection.cursor()
    mycursor.execute(f"""
    CALL addInstructor('{emp_id}', '{first_name}', '{last_name}', '{dob}', '{dept_name}', '{password}', '{fav_colour}');""")
    connection.commit()
    mycursor.close()


def attendance_between_dates(connection, start_date, end_date, stu_id):
    mycursor = connection.cursor()
    mycursor.execute(f"select course_id, count(*) as count from takes where student_id = '{stu_id}' AND date BETWEEN '{start_date}' AND '{end_date}' group by course_id order by course_id;")
    out = mycursor.fetchall()
    for i in out:
        mycursor.execute(f"select count(*) from takes where course_id = '{i[0]}' and student_id = '{stu_id}' and date BETWEEN '{start_date}' AND '{end_date}' AND present = True;")
        out2 = mycursor.fetchone()
        out2 = out2[0]
        print("Course_id: ", i[0], "; No of Days Present: ", out2, f"; Percentage of Attendance between these two dates: ", (out2*100)/i[1])
    connection.commit()
    mycursor.close()
    
    
def attendance_for_course(connection, course_id):
    mycursor = connection.cursor()
    mycursor.execute(f"select date, count(*) as 'No of students present' from takes where course_id = '{course_id}' group by date order by date;")
    out = mycursor.fetchall()
    for i in out:
        mycursor.execute(f"select count(*) from takes where date = '{i[0]}' and course_id = '{course_id}' and present = True;")
        out2 = mycursor.fetchone()
        if(out2!=None):
            out2 = out2[0]
            print("Date: ", i[0], "; No of Students Present: ", out2, "; Percentage of Attendance: ", (100*out2)/i[1])
    connection.commit()
    mycursor.close()
    
def check_student_leave_permission(connection, student_id, date):
    mycursor = connection.cursor()
    mycursor.execute(f"select permission from Student_permission where date = '{date}' AND Student_id = '{student_id}';")
    out = mycursor.fetchall()
    try:
        out = out[0]
        if out[0]==1 :
            print("Leave has been applied") 
        else:
            print("Leave not applied")
            mycursor.execute(f"insert into student_permission values ('{student_id}', '{date}', '0');")

    except:
        print('Leave not applied')
        mycursor.execute(f"insert into student_permission values ('{student_id}', '{date}', '0');")
    connection.commit()
    mycursor.close()

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

def update_faculty_info(connection, emp_id, new_first_name, new_last_name, new_DOB):
    mycursor = connection.cursor()
    mycursor.execute(
        f"""UPDATE employees
            SET
                first_name = '{new_first_name}',
                last_name = '{new_last_name}',
                DOB = '{new_DOB}'
            WHERE
                emp_id = '{emp_id}';
        """
    )

    print('Successfully updated information')
    connection.commit()
    mycursor.close()

def update_student_info(connection, student_id, new_first_name, new_last_name, new_DOB):
    mycursor = connection.cursor()
    mycursor.execute(
        f"""UPDATE students
            SET
                first_name = '{new_first_name}',
                last_name = '{new_last_name}',
                DOB = '{new_DOB}'
            WHERE
                Student_id = '{student_id}';
        """
    )

    print('Successfully updated information')
    connection.commit()
    mycursor.close()
    
def absent_without_permission(connection):
    mycursor = connection.cursor()
    mycursor.execute("select * from student_permission where permission = 0;")
    out = mycursor.fetchall()
    for i in out:
        print("Student ID: ", i[0], "; Absent on Date: ", i[1])
    connection.commit()
    mycursor.close()

    #Add other utility queries here
    #***************************************#
