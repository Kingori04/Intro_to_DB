try:
    # Attempt to connect to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    # ✅ Handles connection or execution errors
    print(f"Error: {e}")

finally:
    # ✅ Ensures database connection is always closed
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

