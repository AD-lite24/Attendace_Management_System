import random
import datetime
import mysql.connector

def student_takes_generator(connection):

    students = ['s1', 's2', 's3', 's4', 's5']
    courses = ['c1', 'c2', 'c3', 'c4', 'c5']

    mycursor = connection.cursor()
    data = []

    for s in students:
        if s == 's1':
            courses_taken = ['c1', 'c2']
        elif s == 's2':
            courses_taken = ['c1']
        elif s == 's3':
            courses_taken = ['c4', 'c5']
        elif s == 's4':
            courses_taken = ['c3', 'c5']
        else:
            courses_taken = ['c2']
            
        for c in courses_taken:
            for i in range(1, 32):
                year = 2023
                month = 1
                day = i
                date = datetime.date(year, month, day)
                status = True
                data.append((s, c, date.strftime("%Y-%m-%d"), status))
                query = f"""
                INSERT IGNORE INTO takes
                    VALUES
                        ('{s}', '{c}', '{date.strftime("%Y-%m-%d")}', {status});
                """
                mycursor.execute(query)
                connection.commit()
                
    
    mycursor.close()
                
    