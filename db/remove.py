import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="b22bb044@007bond",
    database="art_platform"
)

cursor = conn.cursor()

# SQL query to delete artwork purchases made after 7 PM on August 15, 2024
delete_order_items_query = """
DELETE FROM OrderItem
WHERE order_id IN (
    SELECT order_id
    FROM `Order`
    WHERE order_date = '2024-08-15' AND TIME(order_date) > '19:00:00'
);
"""

# Execute the query
cursor.execute(delete_order_items_query)
conn.commit()

# Optionally delete related orders
delete_orders_query = """
DELETE FROM `Order`
WHERE order_date = '2024-08-15' AND TIME(order_date) > '19:00:00';
"""

# Execute the query
cursor.execute(delete_orders_query)
conn.commit()

print("Artwork purchases made after 7 PM on August 15, 2024, have been removed.")

# Close the cursor and connection
cursor.close()
conn.close()
