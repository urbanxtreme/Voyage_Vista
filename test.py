import pymysql
from pymysql.err import OperationalError


def get_user_input():
    # Get user input for pickup location, drop location, and time
    pickup_location = input("Enter pickup location: ")
    drop_location = input("Enter drop location: ")
    time = input("Enter time (HH:MM:SS): ")

    return pickup_location, drop_location, time


def fetch_data(pickup_location, drop_location, time):
    conn = None
    try:
        # Step 1: Connect to the MySQL server
        conn = pymysql.connect(
            host="localhost",  # Replace with your MySQL server host
            user="root",  # Replace with your MySQL username
            password="19112005",  # Replace with your MySQL password
            database="school"  # Connect directly to the 'school' database
        )

        if conn.open:
            print("Successfully connected to MySQL server")

        cursor = conn.cursor()

        # Step 2: Define the SQL query
        query = """
        SELECT * FROM students
        WHERE pickuploc = %s
        AND droploc = %s
        AND TIME(time) = %s
        """

        # Execute the query with user-provided data
        cursor.execute(query, (pickup_location, drop_location, time))

        # Fetch all results
        rows = cursor.fetchall()

        # Display results
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found matching the criteria.")

    except OperationalError as e:
        print(f"Error: {e}")

    finally:
        # Step 3: Close the connection
        if conn is not None and conn.open:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    pickup_location, drop_location, time = get_user_input()
    fetch_data(pickup_location, drop_location, time)
