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

def register_course_student(connection, stu_ID, course_ID, value):

    mycursor = connection.cursor()
    current_date = datetime.date.today()
    mycursor.execute(f"INSERT INTO Takes values ('{stu_ID}', '{course_ID}', '{current_date}', '{value}')")
    mycursor.close()


def employee_attendance(connection, emp_ID):
    mycursor = connection.cursor()
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mycursor.execute(f"INSERT INTO Employee_Records values ('{emp_ID}', '{current_date}', 'True')")
    mycursor.close()
    
def check_student_attendance(connection, course_id):
    mycursor = connection.cursor()
    mycursor.execute(f"Select Student_id, count(*) as count from takes where Course_id = '{course_id}' and Att_present = 'True' group by Student_id order by count")
    out = mycursor.fetchall()
    for i in out:
        print("Student id: ", i[0])
        print("\t Attendance count: ", i[1])
        print("\n")
    connection.commit()
    mycursor.close()

def apply_for_leave(connection, date, faculty_id):
    pass
    
    #Add other utility queries here
    #***************************************#
