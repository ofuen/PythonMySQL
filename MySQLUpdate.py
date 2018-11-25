import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","****","test")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    #Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
