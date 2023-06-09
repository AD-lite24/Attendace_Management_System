CREATE TABLE IF NOT EXISTS students(
        Student_id VARCHAR(255) NOT NULL,
        First_name VARCHAR(255) NOT NULL,
        Last_name VARCHAR(255) NOT NULL,
        DOB DATE NOT NULL,
        Dept_name VARCHAR(255),
        PRIMARY KEY(Student_id)
    );


CREATE TABLE IF NOT EXISTS admins(
        admin_id VARCHAR(255) NOT NULL,
        Password VARCHAR(255),
        Fav_colour VARCHAR(255),
        PRIMARY KEY(admin_id)
    );


CREATE TABLE IF NOT EXISTS departments(
        Dept_name VARCHAR(255) NOT NULL,
        Dept_location VARCHAR(255),
        PRIMARY KEY(Dept_name)
    );


CREATE TABLE IF NOT EXISTS employees(
        Emp_id VARCHAR(255) NOT NULL,
        First_name VARCHAR(255) NOT NULL,
        Last_name VARCHAR(255) NOT NULL,
        DOB DATE,
        PRIMARY KEY (Emp_id)
    );

CREATE TABLE IF NOT EXISTS instructors(
        Emp_id VARCHAR(255),
        Dept_name VARCHAR(255),
        Password VARCHAR(255),
        Fav_colour VARCHAR(255),
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
        date Date NOT NULL,
        Present boolean default NULL,
        PRIMARY KEY(Student_id, Course_id, date),
        FOREIGN KEY(Student_id) REFERENCES Students(Student_id) on delete cascade on update cascade,
        FOREIGN KEY(Course_id) REFERENCES Courses(Course_id) on delete cascade on update cascade
    );

CREATE TABLE IF NOT EXISTS Student_permission(
        Student_id VARCHAR(255) NOT NULL,
        date Date NOT NULL,
        Permission boolean default False,
        PRIMARY KEY(Student_id, date),
        FOREIGN KEY(Student_id) REFERENCES Students(Student_id) on delete cascade on update cascade
    );

CREATE TABLE IF NOT EXISTS Employee_records(
        Emp_id VARCHAR(255) NOT NULL,
        date DATE NOT NULL,
        Present boolean default NULL,
        Permission boolean default False,
        PRIMARY KEY(Emp_id, date),
        FOREIGN KEY(Emp_id) REFERENCES employees(Emp_id)
    );

drop trigger if exists tr_up_id_student;
drop trigger if exists tr_up_id_faculty;
drop trigger if exists tr_up_id_emp;

CREATE TRIGGER tr_up_id_student
BEFORE INSERT ON students
FOR EACH ROW
    SET NEW.student_id = LOWER(NEW.student_id);

CREATE TRIGGER tr_up_id_faculty
BEFORE INSERT ON instructors
FOR EACH ROW
    SET NEW.Emp_id = LOWER(NEW.Emp_id);

CREATE TRIGGER tr_up_id_emp
BEFORE INSERT ON employees
FOR EACH ROW
    SET NEW.Emp_id = LOWER(NEW.Emp_id);

