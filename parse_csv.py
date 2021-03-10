import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('AGENTS.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS deployments')
print("table dropped successfully");
    # create table again
conn.execute('CREATE TABLE AGENTS (AgentID INTEGER, Busines_Name TEXT, Phone_Number INTEGER,City TEXT, Country TEXT)')
print("table created successfully");
    

with open('Active_Agents.csv', newline='') as f:
    reader = csv.reader(f, delimiter = ",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        AgentID = str(row[0])
        Busines_Name = str(row[2])
        Phone_Number = str(row[3])
        City  = str(row[4])
        Country = str(row[5])
       
        
        cur.execute('INSERT INTO AGENTS VALUES(?,?,?,?,?)', (AgentID, Busines_Name, Phone_Number, City, Country))
    print("data parsed successfully");
    conn.commit()
    conn.close()