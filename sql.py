import pymysql
from pymysql.err import OperationalError

def connect_to_mysql():
    """Connect to the MySQL server and return the connection object."""
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="19112005"
        )
        if conn.open:
            print("Successfully connected to MySQL server")
        return conn
    except OperationalError as e:
        print(f"Error connecting to MySQL server: {e}")
        return None

def create_database(cursor):
    """Create the 'school' database if it does not already exist."""
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    print("Database 'school' created or already exists.")

def create_table(cursor):
    """Create the 'students' table in the 'school' database."""
    cursor.execute("DROP TABLE IF EXISTS students")  # Drop the table if it exists
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
        trtime TIME,
        arrtime TIME,
        ttime TIME,
        conductor VARCHAR(100)
    )
    """)
    print("Table 'students' created or already exists.")

def insert_data(cursor, students):
    """Insert a list of student tuples into the 'students' table."""
    insert_query = """
    INSERT INTO students (name, vehnmbr, pickuploc, droploc, price, distance, company, time, trtime, arrtime, ttime,conductor) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """
    for student in students:
        cursor.execute(insert_query, student)
    print("Data inserted into 'students' table.")

def retrieve_and_display_data(cursor):
    """Retrieve and display all data from the 'students' table."""
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = None
    try:
        conn = connect_to_mysql()
        if conn is None:
            return

        cursor = conn.cursor()
        create_database(cursor)
        conn.select_db("school")
        create_table(cursor)

        students = [
            # List of student tuples
            ("Sharath", "AB 13 B 4567", "SOUTH Jn", "NORTH Jn", 3000.0, 169.0, "KUBER", None, "03:56:00", None, None,None),
            ("Sudheesh", "AB 32 F 4621", "SOUTH Jn", "NORTH Jn", 3250.0, 169.0, "KOLAA", None, "03:47:00", None, None,None),
            ("Pranav", "AB 16 H 0115", "SOUTH Jn", "NORTH Jn", 2750.0, 169.0, "ZWIFT", "07:00:00", "03:40:00", None,None,
             "Haripriya"),
            ("Aadhikesh", "AB 12 S 2005", "SOUTH Jn", "NORTH Jn", 3450.0, 169.0, "DAPPIDO", None, "03:55:40", None,None,
             None),
            ("Kiran", "AB 24 Y 8956", "NORTH Jn", "SOUTH Jn", 3250.0, 169.0, "KOLAA", None, "03:47:00", None, None,None),
            ("Shankar", "AB 16 H 4626", "NORTH Jn", "SOUTH Jn", 3450.0, 169.0, "DAPPIDO", None,
             "03:55:00", None,None, None),
            ("Gopika", "AB 24 K 2369", "NORTH Jn", "SOUTH Jn", 3000.0, 169.0, "KUBER", None, "03:56:00", None, None,None),
            ("Devu", "AB 45 M 7890", "NORTH Jn", "SOUTH Jn", 2750.0, 169.0, "ZWIFT", "10:00:00", "03:40:20", None,None,
             "Anand"),
            ("Niranjan", "AB 65 X 6969", "EAST Jn", "WEST Jn", 5050.0, 206.0, "KUBER", None, "04:10:00", None, None,None),
            ("Aashray", "AB 73 J 1714", "EAST Jn", "WEST Jn", 5100.0, 206.0, "KOLAA", None, "04:05:52", None,None,
             None),
            ("Kakakshi", "AB 15 J 1814", "EAST Jn", "WEST Jn", 4500.0, 206.0, "ZWIFT", "09:00:00", "04:30:00", None,None,
             "Don Lee"),
            ("John Doe", "AB 10 C 1234", "EAST Jn", "WEST Jn", 5000.0, 206.0, "DAPPIDO", None, "04:00:00", None, None,None),
            ("Jane Smith", "AB 20 B 5678", "WEST Jn", "EAST Jn", 5050.0, 206.0, "KUBER", None, "04:10:00", None,None,
             None),
            ("Alice Brown", "AB 05 D 4321", "WEST Jn", "EAST Jn", 5100.0, 206.0, "KOLAA", None, "04:05:52", None,None,
             None),
            (
                "Bob Johnson", "AB 22 A 8765", "WEST Jn", "EAST Jn", 4500.0, 206.0, "ZWIFT", "11:00:00", "04:30:00", None,None,
                "James Max"),
            ("Emily Davis", "AB 12 X 9876", "WEST Jn", "EAST Jn", 5000.0, 206.0, "DAPPIDO", None, "04:00:00", None,None,
             None),
            ("Michael Wilson", "AB 32 F 5432", "NORTH Jn", "EAST Jn", 3575.0, 178.0, "DAPPIDO", None, "04:00:00", None,None,

             None),
            (
                "Jessica Miller", "AB 08 P 2468", "NORTH Jn", "EAST Jn", 3450.0, 178.0, "KUBER", None, "04:05:00", None,None,
                None),
            ("David Lee", "AB 17 N 1357", "NORTH Jn", "EAST Jn", 3300.0, 178.0, "KOLAA", None, "03:50:00", None,None,
             None),
            ("Sarah Wilson", "AB 14 L 9753", "NORTH Jn", "EAST Jn", 3250.0, 178.0, "ZWIFT", "08:00:00", "04:00:00", None,None,
                "Sam David"),
            ("Matthew Thomas", "AB 09 Q 8026", "EAST Jn", "NORTH Jn", 3250.0, 178.0, "ZWIFT", "12:00:00", "04:00:00", None,None,
             "Fabian Ruiz"),
            ("Jennifer Garcia", "AB 03 E 7890", "EAST Jn", "NORTH Jn", 3300.0, 178.0, "KOLAA", None, "03:53:00", None,None,
             None),
            ("Daniel Martinez", "AB 18 H 6543", "EAST Jn", "NORTH Jn", 3450.0, 178.0, "KUBER", None,
             "04:10:00", None, None,None),
            ("Lisa Robinson", "AB 27 R 3210", "EAST Jn", "NORTH Jn", 3575.0, 178.0, "DAPPIDO", None, "04:00:00", None,None,
             None),
            ("Anthony Clark", "AB 04 T 5678", "NORTH Jn", "WEST Jn", 4250.0, 250.0, "DAPPIDO", None, "05:30:00",None,
             None, None),
            ("Megan Lewis", "AB 06 S 4321", "NORTH Jn", "WEST Jn", 4520.0, 250.0, "KUBER", None, "05:15:00", None,None,
             None),
            ("Kevin Walker", "AB 05 L 9876", "NORTH Jn", "WEST Jn", 4500.0, 250.0, "KOLAA", None, "05:10:00",None,None,
             None),
            ("Laura Hall", "AB 11 B 2468", "NORTH Jn", "WEST Jn", 4010.0, 250.0, "ZWIFT", "10:00:00", "04:50:00", None,None,
             "Peter Durry"),
            ("Eric Young", "AB 21 D 1357", "SOUTH Jn", "EAST Jn", 5000.0, 320.0, "ZWIFT", "12:00:00", "06:55:00", None,None,
             "Lingard"),
            ("Rachel White", "AB 08 P 9753", "SOUTH Jn", "EAST Jn", 5100.0, 320.0, "KUBER", None, "06:45:00", None,None,
             None),
            (
            "Steven King", "AB 12 Q 8026", "SOUTH Jn", "EAST Jn", 5101.0, 320.0, "KOLAA", None, "06:30:00", None, None,None),
            ("Liam Johnson", "AB 18 B 1234", "SOUTH Jn", "EAST Jn", 5000.0, 320.0, "DAPPIDO", None, "06:35:00", None,None,
             None),
            ("Olivia Williams", "AB 28 F 5678", "EAST Jn", "SOUTH Jn", 5100.0, 320.0, "KUBER", None,
             "06:45:00", None, None,None),
            ("Noah Brown", "AB 14 H 9012", "EAST Jn", "SOUTH Jn", 5101.0, 320.0, "KOLAA", None, "06:30:00", None, None,None),
            ("Emma Davis", "AB 17 J 3456", "EAST Jn", "SOUTH Jn", 5000.0, 320.0, "ZWIFT", "16:00:00", "06:55:00", None,None,
             "Roshan"),
            ("William Miller", "AB 25 K 7890", "EAST Jn", "SOUTH Jn", 5000.0, 320.0, "DAPPIDO", None, "06:35:00", None,None,
             None),
            ("Sophia Garcia", "AB 31 M 2345", "SOUTH Jn", "WEST Jn", 2750.0, 130.0, "DAPPIDO", None,
             "02:30:00", None, None,None),
            ("James Martinez", "AB 19 X 6789", "SOUTH Jn", "WEST Jn", 2800.0, 130.0, "KUBER", None, "02:45:00", None,None,
             None),
            ("Isabella Robinson", "AB 22 Y 0123", "SOUTH Jn", "WEST Jn", 2890.0, 130.0, "KOLAA", None, "02:25:00",None,
             None, None),
            ("Benjamin Clark", "AB 20 Z 4567", "SOUTH Jn", "WEST Jn", 2840.0, 130.0, "ZWIFT", "11:00:00",
             "02:15:00", None,None, "Lucas Wong"),
            ("Amelia Lewis", "AB 08 A 7890", "WEST Jn", "NORTH Jn", 4010.0, 250.0, "ZWIFT", "13:00:00",
             "04:50:00", None,None, "Ella Lee"),
            ("Lucas Walker", "AB 21 B 2468", "WEST Jn", "NORTH Jn", 4500.0, 250.0, "KOLAA", None, "05:10:00", None,
             None, None),
            ("Mia Hall", "AB 11 C 1357", "WEST Jn", "NORTH Jn", 4520.0, 250.0, "KUBER", None, "05:15:00", None, None,None),
            ("Ethan Young", "AB 15 D 8026", "WEST Jn", "NORTH Jn", 4010.0, 250.0, "DAPPIDO", None, "05:30:00",
             None, None,None),
            ("Harper White", "AB 09 E 9753", "WEST Jn", "SOUTH Jn", 2750.0, 250.0, "DAPPIDO", None,
             "02:30:00", None, None,None),
            ("Mason King", "AB 25 F 4321", "WEST Jn", "SOUTH Jn", 2800.0, 130.0, "KUBER", None, "02:45:00", None,
             None,None),
            ("Evelyn Hall", "AB 16 G 5678", "WEST Jn", "SOUTH Jn", 2890.0, 130.0, "KOLAA", None, "02:25:00",
             None, None,None),
            ("Logan Young", "AB 19 H 9012", "WEST Jn", "SOUTH Jn", 2840.0, 130.0, "ZWIFT", "15:00:00",
             "02:15:00", None,None, "Lucas Wong"),
            ("Charlie Tom", "AB 19 H 9012", "WEST Jn", "SOUTH Jn", 2840.0, 130.0, "ZWIFT", "00:00:00",
             "02:15:00", None,None, "William Wong"),
            ("Fluffy Kim", "AB 19 H 9012", "WEST Jn", "SOUTH Jn", 2840.0, 130.0, "ZWIFT", "09:00:00",
             "02:15:00", None,None, "Jacob Jaiswal"),
            ("Amanda Lewis", "AB 08 A 7890", "WEST Jn", "NORTH Jn", 4010.0, 250.0, "ZWIFT", "19:00:00",
             "04:50:00", None,None, "Lee Mathew"),
            ("Benjamin Joshy ", "AB 08 A 7890", "WEST Jn", "NORTH Jn", 4010.0, 250.0, "ZWIFT", "01:00:00",
             "04:50:00", None,None, "Misty Ash"),
            ("Sebastian Clark", "AB 20 Z 4567", "SOUTH Jn", "WEST Jn", 2840.0, 130.0, "ZWIFT", "19:00:00",
             "02:15:00", None,None, "James Ron"),
            ("Adam Willy", "AB 20 Z 4567", "SOUTH Jn", "WEST Jn", 2840.0, 130.0, "ZWIFT", "04:00:00",
             "02:15:00", None,None, "Jhon Silva"),
            ("Cris Chriz", "AB 17 J 3456", "EAST Jn", "SOUTH Jn", 5000.0, 320.0, "ZWIFT", "00:00:00", "06:55:00", None,None,
             "Joash"),
            ("Tulasi Max", "AB 17 J 3456", "EAST Jn", "SOUTH Jn", 5000.0, 320.0, "ZWIFT", "08:00:00", "06:55:00", None,None,
             "Jojo"),
            ("Dominic Dolf", "AB 21 D 1357", "SOUTH Jn", "EAST Jn", 5000.0, 320.0, "ZWIFT", "20:00:00", "06:55:00", None,None,
             "Antony"),
            ("James Jain", "AB 21 D 1357", "SOUTH Jn", "EAST Jn", 5000.0, 320.0, "ZWIFT", "04:00:00", "06:55:00", None,None,
             "Hitler Gandhi"),
            ("Calvin Jeep", "AB 11 B 2468", "NORTH Jn", "WEST Jn", 4010.0, 250.0, "ZWIFT", "16:00:00", "04:50:00", None,None,
             "Pepe Bob"),
            ("Simon", "AB 11 B 2468", "NORTH Jn", "WEST Jn", 4010.0, 250.0, "ZWIFT", "22:00:00", "04:50:00", None, None,
             "Jack"),
            ("Jessy K", "AB 16 H 0115", "SOUTH Jn", "NORTH Jn", 2750.0, 169.0, "ZWIFT", "13:00:00", "03:40:00", None, None,
             "Jackson "),
            ("Anirudh", "AB 16 H 0115", "SOUTH Jn", "NORTH Jn", 2750.0, 169.0, "ZWIFT", "19:00:00", "03:40:00", None,None,
             "Ramos"),
            ("PavitHra", "AB 45 M 7890", "NORTH Jn", "SOUTH Jn", 2750.0, 169.0, "ZWIFT", "16:00:00", "03:40:20", None, None,
             "Sreehari"),
            ("King ", "AB 45 M 7890", "NORTH Jn", "SOUTH Jn", 2750.0, 169.0, "ZWIFT", "22:00:00", "03:40:20", None,None,
             "Fanta Bob"),
            ("Hiroshi", "AB 15 J 1814", "EAST Jn", "WEST Jn", 4500.0, 206.0, "ZWIFT", "13:00:00", "04:30:00", None,None,
             "Jung Soo"),
            ("Nakamura", "AB 15 J 1814", "EAST Jn", "WEST Jn", 4500.0, 206.0, "ZWIFT", "18:00:00", "04:30:00", None,None,
             "Hinata"),
            (" Johnson", "AB 22 A 8765", "WEST Jn", "EAST Jn", 4500.0, 206.0, "ZWIFT", "15:00:00", "04:30:00", None,None,
            "Levi Ackerman"),
            ("Eren Jaeger", "AB 22 A 8765", "WEST Jn", "EAST Jn", 4500.0, 206.0, "ZWIFT", "21:00:00", "04:30:00", None,None,
            "Mikasa Ackerman"),
            ( "Willam Nato", "AB 14 L 9753", "NORTH Jn", "EAST Jn", 3250.0, 178.0, "ZWIFT", "16:00:00", "04:00:00", None,None,
            "Luke Antony"),
            ("J J Thompson", "AB 14 L 9753", "NORTH Jn", "EAST Jn", 3250.0, 178.0, "ZWIFT", "00:00:00", "04:00:00", None,None,
             "David James"),
            ("Naslen Jhon", "AB 09 Q 8026", "EAST Jn", "NORTH Jn", 3250.0, 178.0, "ZWIFT", "20:00:00", "04:00:00",
             None,None,"Darren"),
            ("Silver Gold", "AB 09 Q 8026", "EAST Jn", "NORTH Jn", 3250.0, 178.0, "ZWIFT", "04:00:00", "04:00:00",
             None,None, "Martin Cooper"),

            #PARTIAL TRIPS

            ("Liam Turner", "AB 30 I 6789", "NORTH Jn", "NORTH EAST Jn", 1400.0, 90.0, "KOLAA", None, "02:00:00", None,
             None, None),
            ("Olivia Roberts", "AB 31 J 1234", "NORTH EAST Jn", "EAST Jn", 1400.0, 90.0, "KOLAA", None, "02:00:00", None,
             None, None),
            ("William Evans", "AB 40 S 6789", "EAST Jn", "NORTH EAST Jn", 1400.0, 90.0, "KOLAA", None, "05:30:00", None,
             None, None),
            ("Charlotte Baker", "AB 39 R 2345", "NORTH EAST Jn", "NORTH Jn", 1400.0, 90.0, "KOLAA", None, "05:15:00",
             None, None, None),
            ("Noah Carter", "AB 32 K 5678", "NORTH Jn", "NORTH WEST Jn", 2100.0, 130.00, "KOLAA", None, "02:30:00", None, None,
             None),
            ("Aiden Scott", "AB 34 M 2345", "NORTH WEST  Jn", "WEST Jn", 2100.0, 130.0, "KOLAA", None, "02:30:00", None,
             None, None),
            ("Isabella Adams", "AB 35 N 6789", "WEST Jn", "NORTH WEST Jn", 2100.0, 130.0, "KOLAA", None, "02:30:00", None,
             None, None),
            ("Ethan Nelson", "AB 36 O 1234", "NORTH WEST Jn", "NORTH Jn", 2100.0, 130.0, "KOLAA", None, "02:30:00", None, None,
            None),
            ("Jacob Lee", "AB 38 Q 9012", "SOUTH Jn", "SOUTH EAST Jn", 2550.0, 150.0, "KOLAA", None, "03:00:00", None, None,
             None),
            ("James Lewis", "AB 42 U 1234", "SOUTH EAST Jn", "EAST Jn", 2550.0, 150.0, "KOLAA", None, "03:00:00", None,
             None, None),
            ("Sophia Martin", "AB 43 V 5678", "EAST Jn", "SOUTH EAST Jn", 2550.0, 150.0, "KOLAA", None, "03:00:00", None,
             None, None),
            ("Benjamin Harris", "AB 44 W 9012", "SOUTH EAST Jn", "SOUTH Jn", 2550.0, 150.0, "KOLAA", None, "03:00:00", None,
             None, None),

            ("Elijah Clark", "AB 46 Y 6789", "SOUTH Jn", "SOUTH WEST Jn", 1500.0, 70.0, "KOLAA", None, "01:30:00", None,
             None, None),
            ("Ella Walker", "AB 47 Z 9012", "SOUTH WEST Jn", "WEST Jn", 1500.0, 70.0, "KOLAA", None, "01:30:00", None, None,
             None),
            ("Lucas Young", "AB 48 A 2345", "WEST Jn", "SOUTH WEST Jn", 1500.0, 70.0, "KOLAA", None, "01:30:00", None, None,
             None),
            ("Matthew Turner", "AB 50 C 9012", "SOUTH WEST Jn", "WEST Jn", 1500.0, 70.0, "KOLAA", None, "01:30:00", None,
             None, None),



            ("Ava Johnson", "AB 51 D 2345", "NORTH Jn", "NORTH EAST Jn", 1200.0, 90.0, "KUBER", None, "01:15:00", None, None,
             None),
            ("Daniel Thompson", "AB 52 E 6789", "NORTH EAST Jn", "EAST Jn", 1200.0, 90.0, "KUBER", None, "01:15:00", None,
             None, None),
            ("Oliver Green", "AB 54 G 2345", "EAST Jn", "NORTH EAST Jn", 1200.0, 90.0, "KUBER", None, "01:15:00", None,
             None, None),
            ("Lily Martinez", "AB 55 H 5678", "NORTH EAST Jn", "NORTH Jn", 1200.0, 90.0, "KUBER", None, "01:15:00", None,
             None, None),


            ( "Samuel Lee", "AB 58 K 5678", "NORTH WEST Jn", "WEST Jn", 2000.0, 130.0, "KUBER", None, "02:40:00", None, None,
            None),
            ("Henry White", "AB 56 I 9012", "WEST Jn", "NORTH WEST Jn", 2000.0, 130.0, "KUBER", None, "02:40:00", None, None,
             None),
            ("Chloe Adams", "AB 59 L 9012", "NORTH WEST Jn", "NORTH Jn", 2000.0, 130.0, "KUBER", None,"02:40:00", None, None,
             None),
            ("Jackson Allen", "AB 60 M 2345", "NORTH Jn", "NORTH WEST Jn", 2000.0, 130.0, "KUBER", None, "02:40:00", None,
             None, None),

            ("Benjamin Martin", "AB 62 O 9012", "SOUTH Jn", "SOUTH EAST Jn", 2500.0, 150.0, "KUBER", None, "03:15:00", None,
             None, None),
            ("Mia Harris", "AB 63 P 2345", "SOUTH EAST Jn", "EAST Jn", 2500.0, 150.0, "KUBER", None, "03:15:00", None, None,
             None),
            ("Sophia Carter", "AB 20 I 1234", "EAST Jn", "SOUTH EAST Jn", 2500.0, 150.0, "KUBER", None, "03:15:00", None,
             None, None),
            ("Liam Harris", "AB 21 J 5678", "SOUTH EAST Jn", "EAST Jn", 2500.0, 150.0, "KUBER", None, "03:15:00", None, None,
             None),



            ("Ava Thompson", "AB 22 K 9012", "SOUTH Jn", "SOUTH WEST Jn", 1450.0, 70.0, "KUBER", None, "01:45:00", None, None,
            None),
            ("Emily Wilson", "AB 24 M 6789", "SOUTH WEST Jn", "WEST Jn", 1450.0, 70.0, "KUBER", None, "01:45:00", None,
             None, None),
            ("Noah Brown", "AB 25 N 1234", "WEST Jn", "SOUTH WEST Jn", 1450.0, 70.0, "KUBER", None, "01:45:00", None, None,
             None),
            ("Isabella White", "AB 26 O 5678", "SOUTH WEST Jn", "SOUTH Jn", 1450.0, 70.0, "KUBER", None, "01:45:00", None,
             None, None),





            ("Michael Robinson", "AB 28 Q 2345", "NORTH Jn", "NORTH WEST Jn", 2100.0, 130.0, "DAPPIDO", None, "02:30:00", None,
            None, None),
            ("Chloe Adams", "AB 29 R 6789", "NORTH WEST Jn", "WEST Jn", 2100.0, 130.0, "DAPPIDO", None, "02:30:00", None, None,
             None),
            ("Alexander Lewis", "AB 30 S 9012", "WEST Jn", "NORTH WEST Jn", 2100.0, 130.0, "DAPPIDO", None, "02:30:00", None,
             None, None),
             ("Benjamin Taylor", "AB 32 U 5678", "NORTH WEST Jn", " NORTH Jn", 2100.0, 130.0, "DAPPIDO", None, "02:30:00", None,
             None, None),


            ("Lily Scott", "AB 33 V 9012", "NORTH Jn", "NORTH EAST Jn", 1100.0, 90.0, "DAPPIDO", None, "01:20:00", None, None,
             None),
            ("William Young", "AB 34 W 2345", "NORTH EAST Jn", "EAST Jn", 1100.0, 90.0, "DAPPIDO", None, "01:20:00", None,
             None, None),
            ("James Anderson", "AB 36 Y 9012", "EAST Jn", "NORTH EAST Jn", 1100.0, 90.0, "DAPPIDO", None, "01:20:00", None,
             None, None),
            ("Mia Walker", "AB 37 Z 2345", "NORTH EAST Jn", "NORTH Jn", 1100.0, 90.0, "DAPPIDO", None, "01:20:00", None, None,
             None),


            ("Noah Hall", "AB 38 A 5678", "SOUTH Jn", "SOUTH EAST Jn", 2400.0, 150.0, "DAPPIDO", None, "03:20:00", None, None,
             None),
            ("Elijah Lewis", "AB 40 C 2345", "SOUTH EAST Jn", "EAST Jn", 2400.0, 150.0, "DAPPIDO", None, "03:20:00", None,
             None, None),
            ("Sofia Miller", "AB 41 D 6789", "EAST Jn", "SOUTH EAST Jn", 2400.0, 150.0, "DAPPIDO", None, "03:20:00", None, None,
            None),
            ("Oliver King", "AB 42 E 9012", "SOUTH EAST Jn", "SOUTH Jn", 2400.0, 150.0, "DAPPIDO", None, "03:20:00", None, None,
             None),



            ("Daniel Thompson", "AB 44 G 5678", "SOUTH Jn", "SOUTH WEST Jn", 1400.0, 70.0, "DAPPIDO", None, "01:30:00", None,
             None, None),
            ("Grace Brown", "AB 45 H 9012", "SOUTH WEST Jn", "WEST Jn", 1400.0, 70.0, "DAPPIDO", None, "01:30:00", None, None,
             None),
            ( "Samuel Green", "AB 46 I 2345", "WEST Jn", "SOUTH WEST Jn", 1400.0, 70.0, "DAPPIDO", None, "01:30:00", None, None,
            None),
             ("Aiden Miller", "AB 48 K 9012", "SOUTH WEST Jn", "SOUTH Jn", 1400.0, 70.0, "DAPPIDO", None, "01:30:00", None,
             None, None),


            ("Lila Moore", "AB 49 L 2345", "WEST Jn", "SOUTH Jn", 2800.0, 130.0, "KUBER", None, "10:15:00", None, None,
             None),
            (
            "Henry Harris", "AB 50 M 5678", "WEST Jn", "SOUTH Jn", 2900.0, 140.0, "KOLAA", None, "10:30:00", None, None,
            None),
            ("Harper Lee", "AB 51 N 9012", "WEST Jn", "SOUTH Jn", 2850.0, 150.0, "ZWIFT", "23:00:00", "10:00:00", None,
             None, "Chloe Adams"),

            ("Michael Clark", "AB 52 O 2345", "EAST Jn", "NORTH Jn", 2750.0, 150.0, "DAPPIDO", None, "11:00:00", None,
             None, None),
            ("Ava Taylor", "AB 53 P 6789", "EAST Jn", "NORTH Jn", 2800.0, 160.0, "KUBER", None, "11:15:00", None, None,
             None),

            ( "Amelia Green", "AB 41 T 9012", "EAST Jn", "NORTH Jn", 2850.0, 140.0, "ZWIFT", "18:00:00", "05:00:00", None,
            None, "Liam Davis"),
            ("Harper Anderson", "AB 45 X 2345", "WEST Jn", "NORTH Jn", 2850.0, 160.0, "ZWIFT", "19:00:00", "06:00:00",
             None, None, "Olivia Smith"),
            ("Mia Scott", "AB 49 B 5678", "SOUTH Jn", "EAST Jn", 2850.0, 150.0, "ZWIFT", "20:00:00", "07:00:00", None,
             None, "Ethan Brown"),
            ("Grace Robinson", "AB 53 F 9012", "NORTH Jn", "EAST Jn", 2850.0, 170.0, "ZWIFT", "21:00:00", "08:00:00",
             None, None, "Harper Wilson"),
            ("Zoe Taylor", "AB 57 J 2345", "EAST Jn", "SOUTH Jn", 2850.0, 160.0, "ZWIFT", "22:00:00", "09:00:00", None,
             None, "Jackson Hall"),
            ("Ella Walker", "AB 61 N 5678", "SOUTH Jn", "WEST Jn", 2850.0, 170.0, "ZWIFT", "23:00:00", "10:00:00", None,
             None, "Ethan Young"),
            ("Jacob Lee", "AB 23 L 2345", "SOUTH WEST Jn", "SOUTH Jn", 1450.0, 170.0, "ZWIFT", "16:00:00", "03:00:00",
             None,None, "Mia Allen"),
            ("Ethan Clark", "AB 27 P 9012", "WEST Jn", "NORTH Jn", 2850.0, 160.0, "ZWIFT", "17:00:00", "04:00:00", None,
             None, "Olivia Harris"),
            ("Mia Martinez", "AB 31 T 2345", "SOUTH Jn", "EAST Jn", 2850.0, 150.0, "ZWIFT", "18:00:00", "05:00:00", None,
            None, "James Wilson"),
            ("Harper Davis", "AB 35 X 5678", "NORTH Jn", "WEST Jn", 2850.0, 160.0, "ZWIFT", "19:00:00", "06:00:00", None,
            None, "Ava Brown"),
            ("Charlotte Allen", "AB 39 B 9012", "EAST Jn", "SOUTH Jn", 2850.0, 170.0, "ZWIFT", "20:00:00", "07:00:00",
             None, None, "Benjamin Harris"),
            ( "Ella Johnson", "AB 43 F 2345", "SOUTH Jn", "WEST Jn", 2850.0, 160.0, "ZWIFT", "21:00:00", "08:00:00", None,
            None, "Jacob Lee"),
            ("Zoe Walker", "AB 47 J 5678", "NORTH Jn", "EAST Jn", 2850.0, 170.0, "ZWIFT", "22:00:00", "09:00:00", None,
             None, "Ethan Scott"),

             # Add other tuples here
        ]

        insert_data(cursor, students)
        conn.commit()
        retrieve_and_display_data(cursor)

    except OperationalError as e:
        print(f"Error: {e}")

    finally:
        if conn is not None and conn.open:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    main()