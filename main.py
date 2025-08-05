import pymysql
from pymysql.err import OperationalError

conn = None  # Initialize conn to ensure it is defined

try:
    # Step 1: Connect to the MySQL server
    conn = pymysql.connect(
        host="localhost",  # Replace with your MySQL server host
        user="root",  # Replace with your MySQL username
        password="19112005"  # Replace with your MySQL password
    )

    if conn.open:
        print("Successfully connected to MySQL server")

    cursor = conn.cursor()

    # Step 2: Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    print("Database 'school' created or already exists.")

    # Step 3: Connect to the new database
    conn.select_db("school")

    # Drop the table if it exists (for debugging purposes)
    cursor.execute("DROP TABLE IF EXISTS students")

    # Step 4: Create a new table
    cursor.execute("""
    CREATE TABLE students (
        Sno INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        vehnmbr VARCHAR(255) NOT NULL,
        pickuploc VARCHAR(255) NOT NULL,
        droploc VARCHAR(255) NOT NULL,
        price FLOAT NOT NULL,
        distance FLOAT NOT NULL,
        company VARCHAR(255) NOT NULL,
        time TIME,
        arrtime TIME,
        conductor VARCHAR(100)
    )
    """)
    print("Table 'students' created or already exists.")

    # Step 5: Insert data into the table
    students = [
        ("sharath", "DL 13 B 4567", "Tilak Nagar", "Agra", 1245.0, 378.0, "UBER", "08:20:00", None, None),
        ("Sudheesh", "KL 32 F 4621", "A", "B", 1.0, 2.0, "UBER", "13:15:00", None, None),
        ("Pranav", "KL 16 H 0115", "C", "D", 1.0, 2.0, "UBER", "13:15:00", None, None),
        ("Aadhikesh", "KL 12 S 2005", "A", "B", 1.0, 2.0, "UBER", "16:00:00", None, None),
        ("Kiran", "KL 24 Y 8956", "A", "B", 1.0, 2.0, "UBER", None, None, None),
        ("Shankar", "KL 16 H 4626", "A", "B", 1.0, 2.0, "UBER", None, None, None),
        ("Gopika", "KL 24 K 2369", "A", "B", 1.0, 2.0, "UBER", None, None, None),
        ("Devu", "KL 45 M 7890", "A", "B", 1.0, 2.0, "UBER", None, None, None),
        ("Nandana", "KL 65 X 6969", "A", "B", 1.0, 2.0, "UBER", None, None, None),
        ("Saranya", "KL 73 J 1714", "A", "B", 1.0, 2.0, "UBER", None, None, None)
    ]

    for student in students:
        cursor.execute(
            "INSERT INTO students (name, vehnmbr, pickuploc, droploc, price, distance, company, time, arrtime, conductor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            student
        )

    # Commit the transaction
    conn.commit()
    print("Data inserted into 'students' table.")

    # Step 6: Retrieve and display the data
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except OperationalError as e:
    print(f"Error: {e}")

finally:
    # Step 7: Close the connection
    if conn is not None and conn.open:
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
