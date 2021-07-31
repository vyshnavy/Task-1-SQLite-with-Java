conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute("INSERT INTO Movies (Name,Actor,Actress,Director,Date of Release) \
      VALUES ("Yeh Jawaani Hai Deewani","Ranbir Kapoor","Deepika Padukone","Ayan Mukerji","30/05/2013")");
conn.execute("INSERT INTO Movies (Name,Actor,Actress,Director,Date of Release) \
      VALUES ("Little Wome","James Norton","Emma Watson	Greta Gerwig","07/12/2017")");
conn.execute("INSERT INTO Movies (Name,Actor,Actress,Director,Date of Release) \
      VALUES ("Bangalore Days","Nivin Pauly","Nazriya Nazim","Anjali Menon","09/05/2014")");

conn.execute("INSERT INTO Movies (Name,Actor,Actress,Director,Date of Release) \
      VALUES ("Twilight","Robert Pattison","Kristen Stewart","Catherine Hardwicke","21/11/2008")");

conn.execute("INSERT INTO Movies (Name,Actor,Actress,Director,Date of Release) \
      VALUES ("Kumbalangi Nights","Shane Nigam","Anna Ben","Madhu C. Narayanan","07/02/2019")");



conn.commit()
print "Records created successfully";
conn.close()