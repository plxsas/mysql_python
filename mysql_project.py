import os
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


#try:
    #with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        #sql = "SELECT * FROM Genre;"
        #cursor.execute(sql)
        #for row in cursor:
            #print(row)

    
#try:
    #with connection.cursor() as cursor:
        #cursor.execute("""CREATE TABLE IF NOT EXISTS
                          #Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists


#try:
    #with connection.cursor() as cursor:
        #rows = [("bob", 21, "1990-02-06 23:04:56"),
                #("jim", 56, "1955-05-09 13:12:45"),
                #("fred", 100, "1911-09-12 01:01:01")]
        #cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        #connection.commit()



finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()

