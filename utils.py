import mysql.connector
from datetime import datetime 

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
    mycursor.execute(f"Select Student_id, count(*) as count from takes where Course_id = '{course_id}' and present = True group by Student_id order by count;")
    out = mycursor.fetchall()
    for i in out:
        print("Student id: ", i[0], ";", "Attendance count: ", i[1])
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
    mycursor.execute(f"Select Course_id, sum(present) as count from takes where date = '{date}' group by Course_id order by count desc;")
    out = mycursor.fetchall()
    for i in out:
        print("Course_id: ", i[0], "; No of Students: ", i[1])

    connection.commit()
    mycursor.close()

def add_faculty(connection, emp_id, first_name, last_name, dob, dept_name, password, fav_colour):
    mycursor = connection.cursor()
    # mycursor.execute(
    #     f"""INSERT IGNORE INTO employees
    #         VALUES
    #             ('{emp_id}', '{first_name}', '{last_name}', '{dob}');
    #     """
    # )
    # mycursor.execute(
    #     f"""INSERT IGNORE INTO instructors
    #         VALUES
    #             ('{emp_id}', '{dept_name}', '{password}', '{fav_colour}');
    #     """
    # )
    # mycursor.execute(f'CALL addInstructor('{}', )')
    mycursor.execute(f"""
    CALL addInstructor('{emp_id}', '{first_name}', '{last_name}', '{dob}', '{dept_name}', '{password}', '{fav_colour}');""")
    connection.commit()
    mycursor.close()


def attendance_between_dates(connection, start_date, end_date, stu_id):
    mycursor = connection.cursor()
    mycursor.execute(f"select course_id, count(*) as count from takes where student_id = '{stu_id}' AND date BETWEEN '{start_date}' AND '{end_date}' AND present = True group by course_id order by count desc;")
    out = mycursor.fetchall()
    for i in out:
        print("Course_id: ", i[0], "; No of Days Present: ", i[1])
    connection.commit()
    mycursor.close()
    
    
def attendance_for_course(connection, course_id):
    mycursor = connection.cursor()
    mycursor.execute(f"select date, count(*) as 'No of students present' from takes where course_id = '{course_id}' and present = True group by date order by date;")
    out = mycursor.fetchall()
    for i in out:
        print("Date: ", i[0], "; No of Students Present: ", i[1])
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
