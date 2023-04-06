--insert into students table
Insert into students values
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

Insert into employees VALUES
    ('e1', 'Kumar Matthews', '1980-05-06'),
    ('e2', 'Larry Summer', '1981-11-17'),
    ('e3', 'Mitchell Max', '1979-12-29'),
    ('e4', 'Nathan Swepson', '1982-09-21'),
    ('e5', 'Omar Khan', '1978-04-16');

Insert into instructors VALUES
    ('e1', 'EEE', 'KMat', 'Yellow'),
    ('e2', 'Econ', 'LSum', 'Red'),
    ('e4', 'CSIS', 'NSwe', 'Blue');

insert into courses VALUES
    ('c1', 3, 'e1', 'EEE'),
    ('c2', 4, 'e2', 'Econ'),
    ('c3', 2, 'e1', 'EEE'),
    ('c4', 3, 'e4', 'CSIS'),
    ('c5', 2, 'e2', 'Econ');

insert into Takes VALUES
    ('s1', 'e2', '2023-04-07', 'True'),
    ('s2', 'e3', '2023-04-08', 'True'),
    ('s3', 'e1', '2023-04-05', 'False'),
    ('s4', 'e4', '2023-04-06', 'True');


