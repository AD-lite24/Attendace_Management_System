import mysql.connector
from datetime import datetime 
def init_schema(connection):

    mycursor = connection.cursor()

    #create student table
    mycursor.execute(
    """CREATE TABLE IF NOT EXISTS students (
        Student_id VARCHAR(255) NOT NULL,
        First_name VARCHAR(255) NOT NULL,
        Last_name VARCHAR(255) NOT NULL,
        DOB DATE NOT NULL,
        Dept_name VARCHAR(255),
        PRIMARY KEY(Student_id)
    );
    """
    )
    connection.commit()
    #create dept table
    mycursor.execute(
    """CREATE TABLE IF NOT EXISTS departments(
        Dept_name VARCHAR(255) NOT NULL,
        Dept_location VARCHAR(255),
        PRIMARY KEY(Dept_name)
    );
    """
    )
    connection.commit()
    #Initialize dept table
    mycursor.execute(
    """INSERT IGNORE INTO departments
        VALUES
            ('CSIS','NAB'),
            ('Mech','FD1'),
            ('EEE','FD2'),
            ('Chemical','FD1'),
            ('Eco', 'NAB'),
            ('Bio', 'FD3');
    """
    )
    #create courses table
    mycursor.execute(
    """CREATE TABLE IF NOT EXISTS courses(
        Course_id VARCHAR(255) NOT NULL,
        Credits int,
        Emp_id VARCHAR(255), 
        Dept_name VARCHAR(255) NOT NULL,
        PRIMARY KEY(Course_id),
        FOREIGN KEY(Dept_name) REFERENCES departments(Dept_name),
        FOREIGN KEY(Emp_id) REFERENCES employees(Emp_id)
    );
    """
    )
    connection.commit()
    #create takes table
    mycursor.execute(
    """CREATE table if not exists Takes(
        Student_id Varchar(255) NOT NULL,
        Course_id Varchar(255) NOT NULL, 
        Att_date Date NOT NULL,
        Att_present boolean NOT NULL,
        PRIMARY KEY(Student_id, Course_id),
        FOREIGN KEY(Student_id) REFERENCES Students(Student_id) on delete cascade on update cascade,
        FOREIGN KEY(Student_id) REFERENCES Coursess(Course_id) on delete cascade on update cascade
    );
    """
    )
    connection.commit()
    #create employee table
    mycursor.execute(
        """CREATE TABLE IF NOT EXISTS employees(
            Emp_id VARCHAR(255) NOT NULL,
            Name VARCHAR(255) NOT NULL,
            DOB DATE,
            PRIMARY KEY (Emp_id)
        );
        """
    )
    connection.commit()
    

        #create takes table

        # mycursor.execute(
        #     """CREATE TABLE IF NOT EXISTS takes(
        #         Student_id VARCHAR(255) NOT NULL,
        #         Course_id VARCHAR(255) NOT NULL,
        #         Att_date DATE NOT NULL,
        #     )
        #     """
        # )
        #done above
    
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

def register_course_student(connection, stu_ID, course_ID):

    mycursor = connection.cursor()
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mycursor.execute("INSERT INTO Takes values ('{stu_ID}', '{course_ID}', '{current_date}', 'True')")

    

    #Add other utility queries here
    #***************************************#
