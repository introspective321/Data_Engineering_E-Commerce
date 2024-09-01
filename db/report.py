import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="b22bb044@007bond",
    database="art_platform"
)

cursor = conn.cursor()

# SQL query to retrieve artwork listings
report_query = """
SELECT artwork_id, title, description, image_url, price, availability, medium, style, artist_id
FROM Artwork
WHERE artwork_id IN (
    SELECT artwork_id
    FROM OrderItem
    JOIN `Order` ON OrderItem.order_id = `Order`.order_id
    WHERE `Order`.order_date BETWEEN '2024-08-01' AND '2024-08-31'
);
"""

# Execute the query
cursor.execute(report_query)
results = cursor.fetchall()

# Column names in the Artwork table
columns = ["Artwork ID", "Title", "Description", "Image URL", "Price", "Availability", "Medium", "Style", "Artist ID"]

# Display the results with column names
for row in results:
    for col_name, value in zip(columns, row):
        print(f"{col_name}: {value}")
    print()  # Adds a blank line between each record for readability

# Close the cursor and connection
cursor.close()
conn.close()

