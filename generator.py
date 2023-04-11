import random
import datetime
import mysql.connector

def student_takes_generator(connection):

    students = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']

    mycursor = connection.cursor()

    for s in students:
        if s == 's1':
            courses_taken = ['c1', 'c2']
        elif s == 's2':
            courses_taken = ['c1']
        elif s == 's3':
            courses_taken = ['c4', 'c5']
        elif s == 's4':
            courses_taken = ['c3', 'c5']
        elif s == 's5':
            courses_taken = ['c1', 'c8']
        elif s == 's6':
            courses_taken = ['c7', 'c8']
        elif s == 's7':
            courses_taken = ['c7', 'c5']
        elif s == 's8':
            courses_taken = ['c1', 'c7']
        elif s == 's9':
            courses_taken = ['c5']
        else:
            courses_taken = ['c2']
            
        for c in courses_taken:
            for i in range(1, 32):
                year = 2023
                month = 1
                day = i
                date = datetime.date(year, month, day)
                prob = 0.1
                status = True if random.random() > prob else False
                query = f"""
                INSERT IGNORE INTO takes
                    VALUES
                        ('{s}', '{c}', '{date.strftime("%Y-%m-%d")}', {status});
                """
                mycursor.execute(query)
                connection.commit()
                
    mycursor.close()
    
                
def employee_record_generator(connection):

    employees = ['e1', 'e2', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 's10']

    mycursor = connection.cursor()
            
    for e in employees:
        for i in range(1, 32):
            year = 2023
            month = 1
            day = i
            date = datetime.date(year, month, day)
            present_prob = 0.1
            permission_prob = 0.8
            present = True if random.random() > present_prob else False
            if present == False:
                permission = True if random.random() < permission_prob else False
            else:
                permission = False

            query = f"""
            INSERT IGNORE INTO employee_records
                VALUES
                    ('{e}', '{date.strftime("%Y-%m-%d")}', {present}, {permission});
            """
            mycursor.execute(query)
            connection.commit()
                
    mycursor.close()
    