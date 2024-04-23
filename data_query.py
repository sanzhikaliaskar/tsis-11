import psycopg2
from config import host, user, password, db_name
import pandas as pd
table_name, limit, offset = 'users2', 2, 0

# try:
#     #connect existing database
    

#     connection.autocommit = True

#     #cursor for performing database operations
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT version();"
#         )
#         print(f"Select version: {cursor.fetchone()}")

#     query = f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}"
#     cursor.execute(query)
#     rows = cursor.fetchall()
    
#     # Create a DataFrame from the query result
#     columns = [desc[0] for desc in cursor.description]
#     df = pd.DataFrame(rows, columns=columns)
    
#     # Export the DataFrame to an Excel file
#     file_name = f"{table_name}_{offset}_{limit}.xlsx"
#     df.to_excel(file_name, index=False)

# except Exception as _ex:
#     print("[INFO] Error while working with PostgreSQL", _ex)
# finally:
#     if connection:
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")

def query_data_with_pagination(table_name, limit, offset):
    # Connect to the database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    
    # Execute the query with pagination parameters
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Create a DataFrame from the query result
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    
    # Export the DataFrame to an Excel file
    file_name = f"{table_name}_{offset}_{limit}.xlsx"
    df.to_excel(file_name, index=False)
    
    # Close the cursor and database connection
    cursor.close()
    connection.close()
    
    # Return the DataFrame
    return df
