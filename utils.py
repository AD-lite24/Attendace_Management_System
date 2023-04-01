import mysql.connector

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

    #create dept table
    mycursor.execute(
    """CREATE TABLE IF NOT EXISTS departments(
        Dept_name VARCHAR(255) NOT NULL,
        Dept_location VARCHAR(255),
        PRIMARY KEY(Dept_name)
    );
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
        FOREIGN KEY(Dept_name) REFERENCES departments(Dept_name)
        FOREIGN KEY(Emp_id) REFERENCES employees(emp_id)
    )
    """
    )

    #create employee table
    mycursor.execute(
        """CREATE TABLE IF NOT EXISTS employees(
            Emp_id VARCHAR(255) NOT NULL,
            Name VARCHAR(255) NOT NULL,
            DOB DATE,
            PRIMARY KEY (Emp_id);
        )
        """
    )

    #create takes table
    
    # mycursor.execute(
    #     """CREATE TABLE IF NOT EXISTS takes(
    #         Student_id VARCHAR(255) NOT NULL,
    #         Course_id VARCHAR(255) NOT NULL,
    #         Att_date DATE NOT NULL,
    #     )
    #     """
    # )


