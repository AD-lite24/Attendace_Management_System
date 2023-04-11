--Inserts entries into the takes table
delimiter #
CALL PROCEDURE insert_into_takes(
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
CALL PROCEDURE insert_into_employee_records(
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
CALL PROCEDURE insert_into_takes(
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
CALL PROCEDURE insert_into_students(
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
CALL PROCEDURE delete_from_student(
    IN ID Varchar(255)
)
BEGIN
DELETE FROM students
    WHERE Student_id = ID;
END #
delimiter ;

--Get student info from the students table
delimiter #
CALL PROCEDURE insert_into_takes(
    IN ID Varchar(255)
)
BEGIN
SELECT * FROM students
    WHERE Student_id = ID;
END #
delimiter ;

--Get employee attendance for the day
delimiter #
CALL PROCEDURE insert_into_takes(
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
CALL PROCEDURE insert_into_takes(
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
CALL PROCEDURE insert_into_takes(
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

delimiter #
CALL PROCEDURE insert_into_takes(
    IN student_id VARCHAR(255),
    IN Course_id Varchar(255),
    IN date DATE,
    IN Present boolean
)
BEGIN
INSERT IGNORE INTO takes
    VALUES
        ('{s}', '{c}', '{date.strftime("%Y-%m-%d")}', {status});
END #
delimiter ;

delimiter #
CALL PROCEDURE insert_into_takes(
    IN student_id VARCHAR(255),
    IN Course_id Varchar(255),
    IN date DATE,
    IN Present boolean
)
BEGIN
INSERT IGNORE INTO takes
    VALUES
        ('{s}', '{c}', '{date.strftime("%Y-%m-%d")}', {status});
END #
delimiter ;

delimiter #
CALL PROCEDURE insert_into_takes(
    IN student_id VARCHAR(255),
    IN Course_id Varchar(255),
    IN date DATE,
    IN Present boolean
)
BEGIN
INSERT IGNORE INTO takes
    VALUES
        ('{s}', '{c}', '{date.strftime("%Y-%m-%d")}', {status});
END #
delimiter ;

delimiter #
CALL PROCEDURE insert_into_takes(
    IN student_id VARCHAR(255),
    IN Course_id Varchar(255),
    IN date DATE,
    IN Present boolean
)
BEGIN
INSERT IGNORE INTO takes
    VALUES
        ('{s}', '{c}', '{date.strftime("%Y-%m-%d")}', {status});
END #
delimiter ;

