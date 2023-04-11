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

