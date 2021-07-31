import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

cursor = conn.execute("SELECT Name,Actor,Actress,Director,Date of Release from Movies")
for row in cursor:
   print "Name = ", row[0]
   print "Actor = ", row[1]
   print "Actress = ", row[2]
   print "Director = ", row[3]
   print "Date of Release = ", row[4], "\n"

print "Operation done successfully";
conn.close()