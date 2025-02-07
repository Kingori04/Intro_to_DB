import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL Server (change 'your_password' accordingly)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("✅ Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"❌ Error: {e}")

    finally:
        # Ensure the connection is closed properly
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()

