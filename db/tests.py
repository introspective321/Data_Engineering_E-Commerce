import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="b22bb044@007bond",
    database="art_platform"
)

cursor = conn.cursor()

# SQL query to retrieve all artworks along with their dates
# #query = """
# SELECT artwork_id, title, description, image_url, price, availability, medium, style, artist_id, created_at
# FROM Artwork;
# """

# If the dates are stored in a different table, use a join:
query = """
SELECT Artwork.artwork_id, title, description, image_url, price, availability, medium, style, artist_id, Order.order_date
FROM Artwork
JOIN OrderItem ON Artwork.artwork_id = OrderItem.artwork_id
JOIN `Order` ON OrderItem.order_id = `Order`.order_id;
"""


cursor.execute(query)
results = cursor.fetchall()

# Column names in the Artwork table along with dates
columns = ["Artwork ID", "Title", "Description", "Image URL", "Price", "Availability", "Medium", "Style", "Artist ID", "Date"]

for row in results:
    for col_name, value in zip(columns, row):
        print(f"{col_name}: {value}")
    print()  

cursor.close()
conn.close()
