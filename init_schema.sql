CREATE TABLE IF NOT EXISTS admins(
            admin_id VARCHAR(255),
            admin_password VARCHAR(255),
            PRIMARY KEY(admin_id)
        );

INSERT IGNORE INTO admins
            VALUES
                ('a1','12345'),
                ('a2','12345'),
                ('a3','12345'),
                ('a4','98765');

CREATE TABLE IF NOT EXISTS students(
        Student_id VARCHAR(255) NOT NULL,
        First_name VARCHAR(255) NOT NULL,
        Last_name VARCHAR(255) NOT NULL,
        DOB DATE NOT NULL,
        Dept_name VARCHAR(255),
        PRIMARY KEY(Student_id)
    );

CREATE TABLE IF NOT EXISTS departments(
        Dept_name VARCHAR(255) NOT NULL,
        Dept_location VARCHAR(255),
        PRIMARY KEY(Dept_name)
    );

INSERT IGNORE INTO departments
        VALUES
            ('CSIS','NAB'),
            ('Mech','FD1'),
            ('EEE','FD2'),
            ('Chemical','FD1'),
            ('Eco', 'NAB'),
            ('Bio', 'FD3');

CREATE TABLE IF NOT EXISTS employees(
            Emp_id VARCHAR(255) NOT NULL,
            Name VARCHAR(255) NOT NULL,
            DOB DATE,
            PRIMARY KEY (Emp_id)
        );

CREATE TABLE IF NOT EXISTS instructors(
            Emp_id VARCHAR(255),
            Dept_name VARCHAR(255),
            Password VARCHAR(255),
            PRIMARY KEY (Emp_id),
            FOREIGN KEY (Dept_name) REFERENCES departments(Dept_name)
        );

CREATE TABLE IF NOT EXISTS courses(
        Course_id VARCHAR(255) NOT NULL,
        Credits int,
        Emp_id VARCHAR(255), 
        Dept_name VARCHAR(255) NOT NULL,
        PRIMARY KEY(Course_id),
        FOREIGN KEY(Dept_name) REFERENCES departments(Dept_name),
        FOREIGN KEY(Emp_id) REFERENCES instructors(Emp_id)
    );

CREATE table if not exists Takes(
        Student_id Varchar(255) NOT NULL,
        Course_id Varchar(255) NOT NULL, 
        Att_date Date NOT NULL,
        Att_present boolean NOT NULL,
        PRIMARY KEY(Student_id, Course_id),
        FOREIGN KEY(Student_id) REFERENCES Students(Student_id) on delete cascade on update cascade,
        FOREIGN KEY(Student_id) REFERENCES Courses(Course_id) on delete cascade on update cascade
    );

CREATE TABLE IF NOT EXISTS employees(
            Emp_id VARCHAR(255) NOT NULL,
            Name VARCHAR(255) NOT NULL,
            DOB DATE,
            PRIMARY KEY (Emp_id)
        );