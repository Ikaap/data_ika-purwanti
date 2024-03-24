import os
import requests
import mysql.connector


# Function to send a request to the API and return the user data
def get_user_data():
    api_url = "https://jsonplaceholder.typicode.com/posts?userId=1"
    response = requests.get(api_url)
    data = response.json()
    return data


# Function to insert user data into the MySQL table
def insert_into_mysql(users):
    try:
        # Replace the connection parameters with your MySQL database details
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME"),
        )

        cursor = connection.cursor()

        # Create the users table if not exists
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                body VARCHAR(255)
            )
        """
        )

        # Insert user data into the table
        for user in users:
            cursor.execute(
                """
                INSERT INTO users (title, body)
                VALUES (%s, %s)
            """,
                (user["title"], user["body"]),
            )

        connection.commit()
        print("Data inserted successfully into MySQL")

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Step 1: Get user data from the API
    users_data = get_user_data()

    # Step 2: Extract relevant information and insert into MySQL
    if users_data:
        user_info_to_insert = [
            {
                "title": user["title"],
                "body": user["body"]
            }
            for user in users_data
        ]
        insert_into_mysql(user_info_to_insert)
    else:
        print("No user data retrieved from the API.")
