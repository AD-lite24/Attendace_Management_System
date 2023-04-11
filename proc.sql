drop procedure if exists addInstructor;#

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


drop procedure if exists check_leave;#
create procedure check_leave(in id Varchar(255), in d date)
begin
    select permission from student_permission where student_id = id and date = d;
end#
