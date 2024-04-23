import psycopg2
from config import host, user, password, db_name
import csv

data = [('Johnny', 'Bell', 87770000000), ('Jane', 'Liam', 87770000001), ('Bob', 'Ross', 87770000002)]
name = 'Lily'
lname = 'Loo'
phone = 87770000004

try:
    #connect existing database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    #cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Select version: {cursor.fetchone()}")

    #create new table
    '''with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users2(
            id serial PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            phone_number NUMERIC(11) NOT NULL);"""
        )
        print("[INFO] Table was succesfully created")
    ''' 
    
    #insert data into table
    '''with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users2 (first_name, last_name, phone_number) VALUES ('Lily', 'Lee', '87770000004');"""
        )
        print("[INFO] Data succesfully inserted")
    '''

    #insert data into table 2
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM users2 WHERE first_name = %s;", (name,))
        result = cursor.fetchone()
        
        if ("SELECT COUNT(*) FROM users2 WHERE first_name = name;"):
            cursor.execute(
                """UPDATE users2 SET phone_number = %s WHERE first_name = %s""",
                (phone, name)
            )
            print("[INFO] Data succesfully updated")
        else:
            cursor.execute(
                "INSERT INTO users2 (first_name, last_name, phone_number) VALUES (%s, %s, %s);",
                (name, lname, phone)
            )
            print("[INFO] Data succesfully inserted")
    
    
    #import data from csv 
    '''with open('sample.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row

        # Iterate over the rows in the CSV file and insert them into the database
        with connection.cursor() as cursor:
            for row in reader:
                cursor.execute(
                    "INSERT INTO users2 (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (row[0], row[1], row[2])
                )
            print("[INFO] Data from csv file succesfully inserted")
    '''
    
    #import data from list
    with connection.cursor() as cursor:
        if not all(c.isdigit() for c in phone):
            print("Invalid phone number")
            
        cursor.execute(

        )

    #updating information
    '''with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE users2 SET first_name = 'Jonathan' WHERE id = 1;"""
        )
        print("[INFO] Data succesfully updated")
    '''

    #get data from table 
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT first_name, last_name, phone_number FROM users2 WHERE id = 2;"
        )
        print(cursor.fetchone())
    
    
    #delete data from table
    '''with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM users2 WHERE id = 1;"""
        )
        print("[INFO] Data succesfully deleted")
    '''

    #delete whole table
    '''with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users2"""
        )
        print("[INFO] Table was succesfully deleted")
    '''

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
