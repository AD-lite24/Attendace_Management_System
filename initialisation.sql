
INSERT IGNORE INTO departments
    VALUES
        ('CSIS','NAB'),
        ('Mech','FD1'),
        ('EEE','FD2'),
        ('Chemical','FD1'),
        ('Eco', 'NAB'),
        ('Bio', 'FD3');


INSERT IGNORE INTO students 
    VALUES
        ('s1', 'Aryan', 'Gupta', '2003-01-25', 'CSIS'),
        ('s2', 'Ben', 'Williams', '2004-03-20', 'Mech'),
        ('s3', 'Cathy', 'Jill', '2003-02-05', 'EEE'),
        ('s4', 'Doug', 'Starc', '2003-09-07', 'Chemical'),
        ('s5', 'Erling', 'Cooper', '2004-10-15', 'Eco'),
        ('s6', 'Farooq', 'Abdullah', '2003-12-02', 'Bio'),
        ('s7', 'Garry', 'Marsh', '2004-08-06', 'CSIS'),
        ('s8', 'Harry', 'Smith', '2004-04-13', 'Mech'),
        ('s9', 'Indy', 'Stiller', '2003-06-30', 'EEE'),
        ('s10', 'Jake', 'McNally', '2003-07-18', 'Chemical');


INSERT IGNORE INTO employees 
    VALUES
        ('e1', 'Kumar', 'Matthews', '1980-05-06'),
        ('e2', 'Larry', 'Summer', '1981-11-17'),
        ('e3', 'Mitchell', 'Max', '1979-12-29'),
        ('e4', 'Nathan', 'Swepson', '1982-09-21'),
        ('e5', 'Omar', 'Khan', '1978-04-16'),
        ('e6', 'Johnson', 'Smith', '1985-09-12'),
        ('e7', 'Garcia', 'Jones', '1982-02-18'),
        ('e8', 'Brown', 'Miller', '1984-11-30'),
        ('e9', 'Lee', 'Davis', '1987-06-07'),
        ('e10', 'Robinson', 'Wilson', '1983-08-14'),
        ('e11', 'Wright', 'Clark', '1988-04-22'),
        ('e12', 'Nguyen', 'Rodriguez', '1981-12-01'),
        ('e13', 'Scott', 'Lopez', '1986-03-09'),
        ('e14', 'Hall', 'Hernandez', '1989-10-23'),
        ('e15', 'Green', 'Gonzalez', '1980-07-12');


INSERT IGNORE INTO instructors 
    VALUES
        ('e1', 'EEE', 'KMat', 'Yellow'),
        ('e2', 'Chemical', 'LSum', 'Red'),
        ('e4', 'CSIS', 'NSwe', 'Blue'),
        ('e4', 'Bio', '9hNzF#', 'Purple'),
        ('e5', 'Chemical', 'aL8cD$', 'Yellow'),
        ('e6', 'Eco', '4sTbM@', 'Orange'),
        ('e7', 'Mech', 'cR1pK%', 'Pink'),
        ('e8', 'CSIS', '6fZnG#', 'Black'),
        ('e9', 'Bio', '2jQyU@', 'Grey'),
        ('e10', 'Chemical', '5xVhL*', 'Brown');


INSERT IGNORE INTO courses 
    VALUES
        ('c1', 3, 'e1', 'EEE'),
        ('c2', 4, 'e2', 'Eco'),
        ('c3', 2, 'e1', 'EEE'),
        ('c4', 3, 'e4', 'CSIS'),
        ('c5', 2, 'e2', 'Eco');


INSERT IGNORE INTO Takes (Student_id, Course_id, date, Present)
    VALUES
        ('s1', 'c1', '2023-04-07', True),
        ('s2', 'c2', '2023-04-08', True),
        ('s3', 'c3', '2023-04-05', False),
        ('s4', 'c5', '2023-04-06', True),
        ('s1', 'c1', '2023-06-15', False),
        ('s2', 'c5', '2023-04-28', True),
        ('s3', 'c3', '2023-07-02', False),
        ('s4', 'c2', '2023-05-10', True),
        ('s5', 'c1', '2023-08-18', False),
        ('s6', 'c4', '2023-06-21', True),
        ('s7', 'c2', '2023-09-07', False),
        ('s8', 'c3', '2023-05-01', True),
        ('s9', 'c1', '2023-07-22', False),
        ('s10', 'c5', '2023-08-09', True),
        ('s6', 'c2', '2023-09-20', True),
        ('s7', 'c1', '2023-05-13', False),
        ('s8', 'c4', '2023-08-06', True),
        ('s9', 'c5', '2023-06-01', False),
        ('s10', 'c3', '2023-07-28', True),
        ('s1', 'c5', '2023-05-30', True),
        ('s2', 'c3', '2023-08-12', False),
        ('s3', 'c4', '2023-06-24', True),
        ('s4', 'c1', '2023-07-09', False),
        ('s5', 'c2', '2023-09-04', True),
        ('s6', 'c1', '2023-06-07', False),
        ('s7', 'c5', '2023-08-19', True),
        ('s8', 'c2', '2023-07-01', False),
        ('s9', 'c3', '2023-05-25', True),
        ('s10', 'c4', '2023-09-10', False),
        ('s1', 'c1', '2023-01-01', True),
        ('s2', 'c2', '2023-01-02', False),
        ('s3', 'c3', '2023-01-03', True),
        ('s4', 'c4', '2023-01-04', False),
        ('s5', 'c5', '2023-01-05', True),
        ('s6', 'c1', '2023-01-06', False),
        ('s7', 'c2', '2023-01-07', True),
        ('s8', 'c3', '2023-01-08', False),
        ('s9', 'c4', '2023-01-09', True),
        ('s10', 'c5', '2023-01-10', False),
        ('s1', 'c1', '2023-01-11', True),
        ('s2', 'c2', '2023-01-12', False),
        ('s3', 'c3', '2023-01-13', True),
        ('s4', 'c4', '2023-01-14', False),
        ('s5', 'c5', '2023-01-15', True),
        ('s6', 'c1', '2023-01-16', False),
        ('s7', 'c2', '2023-01-17', True),
        ('s8', 'c3', '2023-01-18', False),
        ('s9', 'c4', '2023-01-19', True),
        ('s10', 'c5', '2023-01-20', False),
        ('s1', 'c1', '2023-01-21', True),
        ('s2', 'c2', '2023-01-22', False),
        ('s3', 'c3', '2023-01-23', True),
        ('s4', 'c4', '2023-01-24', False),
        ('s5', 'c5', '2023-01-25', True),
        ('s6', 'c1', '2023-01-26', False),
        ('s7', 'c2', '2023-01-27', True),
        ('s8', 'c3', '2023-01-28', False),
        ('s9', 'c4', '2023-01-29', True),
        ('s10', 'c5', '2023-01-30', False),
        ('s1', 'c1', '2023-01-31', True);

INSERT IGNORE INTO Student_permission
    VALUES
        ('s1', '2023-05-09', True),
        ('s1', '2023-05-10', True),
        ('s1', '2023-05-11', True),
        ('s1', '2023-05-12', True),
        ('s2', '2023-05-09', True),
        ('s1', '2023-01-01', True),
        ('s2', '2023-01-02', True),
        ('s3', '2023-01-03', True),
        ('s4', '2023-01-04', True),
        ('s5', '2023-01-05', True),
        ('s6', '2023-01-06', True),
        ('s7', '2023-01-07', True),
        ('s8', '2023-01-08', True),
        ('s9', '2023-01-09', True),
        ('s10', '2023-01-10', True),
        ('s1', '2023-01-11', True),
        ('s2', '2023-01-12', True),
        ('s3', '2023-01-13', True),
        ('s4', '2023-01-14', True),
        ('s5', '2023-01-15', True),
        ('s6', '2023-01-16', True),
        ('s7', '2023-01-17', True),
        ('s8', '2023-01-18', True),
        ('s9', '2023-01-19', True),
        ('s10', '2023-01-20', True),
        ('s1', '2023-01-21', True),
        ('s2', '2023-01-22', True),
        ('s3', '2023-01-23', True),
        ('s4', '2023-01-24', True),
        ('s5', '2023-01-25', True),
        ('s6', '2023-01-26', True),
        ('s7', '2023-01-27', True),
        ('s8', '2023-01-28', True),
        ('s9', '2023-01-29', True),
        ('s10', '2023-01-30', True),
        ('s1', '2023-01-31', True);

INSERT IGNORE INTO admins
    VALUES
        ('a1','12345', 'green'),
        ('a2','12345', 'yellow'),
        ('a3','12345', 'red'),
        ('a4','98765', 'blue');

INSERT IGNORE INTO Employee_records
    VALUES
        ('e1', '2023-04-07', False, True),
        ('e1', '2023-04-08', False, False),
        ('e2', '2023-04-07', True, False),
        ('e2', '2023-04-09', False, False),
        ('e3', '2023-05-07', True, False),
        ('e1', '2023-01-01', True, False),
        ('e2', '2023-01-02', True, False),
        ('e3', '2023-01-03', True, False),
        ('e4', '2023-01-04', True, False),
        ('e5', '2023-01-05', True, False),
        ('e6', '2023-01-06', True, False),
        ('e7', '2023-01-07', True, True),
        ('e8', '2023-01-08', True, False),
        ('e9', '2023-01-09', False, False),
        ('e10', '2023-01-10', True, False),
        ('e11', '2023-01-11', True, False),
        ('e12', '2023-01-12', True, False),
        ('e13', '2023-01-13', True, False),
        ('e14', '2023-01-14', True, False),
        ('e15', '2023-01-15', True, False),
        ('e1', '2023-01-16', True, False),
        ('e2', '2023-01-17', True, False),
        ('e3', '2023-01-18', False, True),
        ('e4', '2023-01-19', False, True),
        ('e5', '2023-01-20', True, False),
        ('e6', '2023-01-21', False, False),
        ('e7', '2023-01-22', True, False),
        ('e8', '2023-01-23', True, False),
        ('e9', '2023-01-24', True, False),
        ('e10', '2023-01-25', True, False),
        ('e11', '2023-01-26', False, False),
        ('e12', '2023-01-27', True, False),
        ('e13', '2023-01-28', True, False),
        ('e14', '2023-01-29', True, False),
        ('e15', '2023-01-30', True, False),
        ('e1', '2023-01-31', True, False);
        

