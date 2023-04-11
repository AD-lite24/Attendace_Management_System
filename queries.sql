--Inserts entries into the takes table
delimiter #
CREATE PROCEDURE insert_into_takes(
    IN student_id VARCHAR(255),
    IN Course_id Varchar(255),
    IN date DATE,
    IN Present boolean
)
BEGIN
INSERT IGNORE INTO takes
    VALUES
        (student_id, Course_id, date, Present);
END #
delimiter ;

--Insert entries into employee records table
delimiter #
CREATE PROCEDURE insert_into_employee_records(
    IN e_id VARCHAR(255),
    IN date DATE,
    IN Present boolean,
    IN permission boolean
)
BEGIN
INSERT IGNORE INTO employee_records
        VALUES
            (e_id, date, Present, permission);
END #
delimiter ;

--Update passwords of instructors and admin 
--here type can be either instructors or admins
delimiter #
CREATE PROCEDURE update_password(
    in type Varchar(255),
    in new_pass Varchar(255),
    in employee_id Varchar(255)
)
BEGIN
UPDATE type
    SET
        Password = new_pass
    WHERE
        Emp_id = employee_id;
END #
delimiter ;

--Creates the database university_b
CREATE DATABASE IF NOT EXISTS university_b;

--Sets up database for use
USE university_b;

--Procedure to add instructors by the admin
--The procedure adds the instructor to both instructors and 
--Employee table
CREATE PROCEDURE addInstructor(
    IN Emp_id VARCHAR(255), 
    IN First_name VARCHAR(255), 
    IN Last_name VARCHAR(255), 
    IN DOB DATE,
    IN Dept_name VARCHAR(255),
    IN Password VARCHAR(255), 
    IN Fav_colour VARCHAR(255)
)
BEGIN
    INSERT IGNORE INTO employees
    VALUES
        (Emp_id, First_name, Last_name, DOB);

    INSERT IGNORE INTO instructors
    VALUES
        (Emp_id, Dept_name, Password, Fav_colour);
END #

--Procedure to check if the student had applied permission for leave
create procedure check_leave(in id Varchar(255), in d date)
begin
    select permission from student_permission where student_id = id and date = d;
end#

--Procedure to check if the employee had applied for permission for leave
create procedure employee_check_leave(in id Varchar(255), in d date)
begin
    select permission from employee_records where Emp_id = id and date = d;
end#

--Add new student
delimiter #
CREATE PROCEDURE insert_into_students(
    IN student_id VARCHAR(255),
    IN First_name Varchar(255),
    IN Last_name Varchar(255),
    IN DOB date,
    IN dept Varchar(255)
)
BEGIN
INSERT INTO students
        VALUES (student_id, First_name, Last_name, DOB, dept);
END #
delimiter ;

--Remove a student from the table
delimiter #
CREATE PROCEDURE delete_from_student(
    IN ID Varchar(255)
)
BEGIN
DELETE FROM students
    WHERE Student_id = ID;
END #
delimiter ;

--Get student info from the students table
delimiter #
CREATE PROCEDURE get_student_info(
    IN ID Varchar(255)
)
BEGIN
SELECT * FROM students
    WHERE Student_id = ID;
END #
delimiter ;

--Get employee attendance for the day
delimiter #
CREATE PROCEDURE get_employee_attendance(
    IN employee_id Varchar(255),
    IN today_date Date
)
BEGIN
SELECT * FROM Employee_records
    WHERE emp_id = employee_id AND date = today_date;
END #
delimiter ;

--Mark attendance of the employee when permission was not applied
delimiter #
CREATE PROCEDURE mark_employee_attendance_no_permit(
    IN employee_id Varchar(255),
    IN today_date Varchar(255),
    IN Present boolean
)
BEGIN
INSERT IGNORE INTO Employee_Records values (employee_id, today_date, Present, False);
END #
delimiter ;

--Mark attendance of the employee when permission has already been applied
delimiter #
CREATE PROCEDURE mark_employee_attendance_yes_permit(
    IN employee_id Varchar(255),
    IN today_date Varchar(255),
    IN Present_status boolean
)
BEGIN
UPDATE Employee_records
    SET
        Present = Present_status
    WHERE
        emp_id = employee_id AND date = today_date;
END #
delimiter ;

--Check all the entries of each student registered in the course
delimiter #
CREATE PROCEDURE check_course_attendance(
    in course_id Varchar(255)
)
BEGIN
Select Student_id, count(*) as count from takes where Course_id = course_id group by Student_id order by student_id;
END #
delimiter ;

--finds amount of times the student was present in class
delimiter #
CREATE PROCEDURE student_attendance_count(
        in course_id Varchar(255),
        in student_id Varchar(255),
        in course_id Varchar(255)
)
BEGIN
select count(*) as count from takes where student_id = student_id and course_id = course_id and present = True;
END #
delimiter ;

--Employee applies for leave
delimiter #
CREATE PROCEDURE employee_apply_for_leave(
    in faculty_id Varchar(255),
    in date Date
)
BEGIN
INSERT IGNORE INTO Employee_records
        VALUES 
            (faculty_id, date, NULL, True);
END #
delimiter ;

--Student appliues for leave
INSERT INTO student_permission
        VALUES
            (student_id, date, True)

--Selects the number of students present for a 
--particular course on a given date. Sum function is used to
--add up all the entries where present = 1 ie. true
Select Course_id, sum(present) as count from takes where date = entered_date group by Course_id order by course_id;

--Selects the number of students who were supposed 
--to attend the course on the given date. 
--The above two queries are used to find the percentage of students who attend the course
select count(*) as count from takes where course_id = given_course_id and date = entered_date;

--
select course_id, count(*) as count from takes where student_id = entered_id AND date BETWEEN start_date AND end_date group by course_id order by course_id;
--
select count(*) from takes where course_id = entered_course and student_id = entered_id and date BETWEEN start_date AND end_date AND present = True;

--Checks whether student has applied for leave permission on a particular date
select permission from Student_permission where date = entered_date AND Student_id = entered_id;

--Inserts into the permissions table a false value if the student is absent without permission.
insert into student_permission values (student_id, date, False);

--Selects the permission value from the employee records table for a given date to check 
--if they had applied for leave before their absency
select permission from employee_records where date = entered_date AND Emp_id = employee_id;

--Updates employee information
UPDATE employees
    SET
        first_name = entered_new_first_name,
        last_name = entered_new_last_name,
        DOB = new_DOB
    WHERE
        emp_id = employee_id;

--Update student information
UPDATE students
    SET
        first_name = entered_new_first_name,
        last_name = entered_new_last_name,
        DOB = new_DOB
    WHERE
        Student_id = entered_id;

--Selects all students who have been absent 
--without permission as well as their dates. 
--This data is used to find the percentage of 
--time a student is absent without permission.
select * from student_permission where permission = 0;

--create student table
CREATE TABLE IF NOT EXISTS students(
        Student_id VARCHAR(255) NOT NULL,
        First_name VARCHAR(255) NOT NULL,
        Last_name VARCHAR(255) NOT NULL,
        DOB DATE NOT NULL,
        Dept_name VARCHAR(255),
        PRIMARY KEY(Student_id)
    );

--create admin table
CREATE TABLE IF NOT EXISTS admins(
        admin_id VARCHAR(255) NOT NULL,
        Password VARCHAR(255),
        Fav_colour VARCHAR(255),
        PRIMARY KEY(admin_id)
    );

--create department table
CREATE TABLE IF NOT EXISTS departments(
        Dept_name VARCHAR(255) NOT NULL,
        Dept_location VARCHAR(255),
        PRIMARY KEY(Dept_name)
    );

--create employee table
CREATE TABLE IF NOT EXISTS employees(
        Emp_id VARCHAR(255) NOT NULL,
        First_name VARCHAR(255) NOT NULL,
        Last_name VARCHAR(255) NOT NULL,
        DOB DATE,
        PRIMARY KEY (Emp_id)
    );

--create instructor table
CREATE TABLE IF NOT EXISTS instructors(
        Emp_id VARCHAR(255),
        Dept_name VARCHAR(255),
        Password VARCHAR(255),
        Fav_colour VARCHAR(255),
        PRIMARY KEY (Emp_id),
         FOREIGN KEY (Dept_name) REFERENCES departments(Dept_name)
    );

--create courses table
CREATE TABLE IF NOT EXISTS courses(
        Course_id VARCHAR(255) NOT NULL,
        Credits int,
        Emp_id VARCHAR(255), 
        Dept_name VARCHAR(255) NOT NULL,
        PRIMARY KEY(Course_id),
        FOREIGN KEY(Dept_name) REFERENCES departments(Dept_name),
        FOREIGN KEY(Emp_id) REFERENCES instructors(Emp_id)
    );

--create takes table
CREATE table if not exists Takes(
        Student_id Varchar(255) NOT NULL,
        Course_id Varchar(255) NOT NULL, 
        date Date NOT NULL,
        Present boolean default NULL,
        PRIMARY KEY(Student_id, Course_id, date),
        FOREIGN KEY(Student_id) REFERENCES Students(Student_id) on delete cascade on update cascade,
        FOREIGN KEY(Course_id) REFERENCES Courses(Course_id) on delete cascade on update cascade
    );

--create student permission table
CREATE TABLE IF NOT EXISTS Student_permission(
        Student_id VARCHAR(255) NOT NULL,
        date Date NOT NULL,
        Permission boolean default False,
        PRIMARY KEY(Student_id, date),
        FOREIGN KEY(Student_id) REFERENCES Students(Student_id) on delete cascade on update cascade
    );

--create employee records table
CREATE TABLE IF NOT EXISTS Employee_records(
        Emp_id VARCHAR(255) NOT NULL,
        date DATE NOT NULL,
        Present boolean default NULL,
        Permission boolean default False,
        PRIMARY KEY(Emp_id, date),
        FOREIGN KEY(Emp_id) REFERENCES employees(Emp_id)
    );

--Drop the triggers if they already exist to prevent errors
drop trigger if exists tr_up_id_student;
drop trigger if exists tr_up_id_faculty;
drop trigger if exists tr_up_id_emp;

--Set all the ids to lower case for consistency
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

--populate dept table
INSERT IGNORE INTO departments
    VALUES
        ('CSIS','NAB');

--populate student table
INSERT IGNORE INTO students 
    VALUES
        ('s1', 'Aryan', 'Gupta', '2003-01-25', 'CSIS');

--populate employees table
INSERT IGNORE INTO employees 
    VALUES
        ('e1', 'Kumar', 'Matthews', '1980-05-06');

--populate courses table
INSERT IGNORE INTO courses 
    VALUES
        ('c1', 3, 'e1', 'EEE');

--populate student_permission table
INSERT IGNORE INTO Student_permission
    VALUES
        ('s1', '2023-05-09', True);

--populate admins table
INSERT IGNORE INTO admins
    VALUES
        ('a1','12345', 'green');