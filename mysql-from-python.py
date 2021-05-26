import os
import datetime
import pymysql

#get username from cloud9 workspace
username = os.getenv('C9_USER')

#connect to database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        row = ("Bob",21,"1990-02-06 23:04:56")
        cursor.execute("INSERT INTO FRIENDS VALUES(%s, %s, %s);", row)
        connection.commit()
        

finally:
    # close connection to sql
    connection.close()
