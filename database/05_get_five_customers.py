import sqlite3

# create database connection
db = sqlite3.connect('employee_basic_crud.db')
cursor = db.cursor()

# write your query here
query = ''' SELECT FirstName,lastname, email
                FROM customers LIMIT 5 '''


try:
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
except:
    print('Something wrong in your query')

# close database connection
db.close()
