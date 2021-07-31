import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE Movies
        (NAME           CHAR(30)    NOT NULL,
         Actor            CHAR(30,
         Actress        CHAR(30),
         Director        CHAR(30), 
         Date of Release DATE);''')

print "Table created successfully";

conn.close()