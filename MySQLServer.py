# MySQLServer.py

import mysql.connector
from mysql.connector import Error as MySQLError

def create_database():
    try:
        # Connect to MySQL server (adjust host/user/password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except MySQLError as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    create_database()

