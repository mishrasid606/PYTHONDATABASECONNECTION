import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host='localhost',          # Replace with your host
    user='root',      # Replace with your username
    password='987654321',  # Replace with your password
    database='conectest'   # Replace with your database name
)

# Create a cursor object
cursor = connection.cursor()

# SQL statement to create the employee table
create_table_query = '''
CREATE TABLE shreya(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(50) NOT NULL
);
'''

# Execute the SQL statement
cursor.execute(create_table_query)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("shreya table created successfully.")
