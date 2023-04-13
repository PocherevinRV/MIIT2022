import psycopg2


def main():
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port="5432"
    )
    print("Database opened successfully")

    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS STUDENT")
    cur.execute('''CREATE TABLE IF NOT EXISTS STUDENT  
         (ID SERIAL PRIMARY KEY,
         NAME TEXT NOT NULL,
         AGE INT NOT NULL,
         COURSE CHAR(50),
         DEPARTMENT CHAR(50));''')

    print("Table created successfully")
    cur.execute('''INSERT INTO STUDENT (NAME,AGE,COURSE,DEPARTMENT) VALUES 
            (%s, %s, 'Computer Science', 'ICT'),
            (%s, %s, 'Computer Science', 'ICT')''', ('Kirill', 18, 'Pavel', 19))

    connection.commit()
    print("Record inserted successfully")
    cur.execute("SELECT id, name, age, course, department from STUDENT")
    rows = cur.fetchall()
    for row in rows:
        print("ID =", row[0])
        print("NAME =", row[1])
        print("AGE =", row[2])
        print("COURSE =", row[3])
        print("DEPARTMENT =", row[4], "\n")

    print("Operation done successfully")
    connection.close()


if __name__ == "__main__":
    main()