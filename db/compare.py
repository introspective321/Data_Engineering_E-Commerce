import mysql.connector
import time

# Function to execute a query and measure execution time
def execute_query(cursor, query):
    start_time = time.time()
    cursor.execute(query)
    result = cursor.fetchall()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="b22bb044@007bond",
    database="art_platform"
)

# Create a cursor object
cursor = conn.cursor()

# Queries for clustering and secondary indexes
queries = {
    "Clustering Index (artwork_id)": "SELECT * FROM Artwork WHERE artwork_id = 1;",
    "Secondary Index (style)": "SELECT * FROM Artwork WHERE style = 'Impressionism';",
    "Secondary Index (medium)": "SELECT * FROM Artwork WHERE medium = 'Oil';"
}

# Execute and measure execution times
for description, query in queries.items():
    result, execution_time = execute_query(cursor, query)
    print(f"{description}:")
    print(f"Results: {result}")
    print(f"Execution Time: {execution_time:.6f} seconds\n")

# Close the cursor and connection
cursor.close()
conn.close()
