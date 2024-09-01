import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",       # Replace with your host
    user="root",            # Replace with your MySQL username
    password="b22bb044@007bond",    # Replace with your MySQL password
    database="art_platform" # Replace with your database name
)

# Create a cursor object
cursor = conn.cursor()

# Insert additional users
cursor.execute("""
    INSERT INTO User (username, password, email, role) VALUES
    ('artist3', 'password5', 'artist3@example.com', 'Artist'),
    ('buyer3', 'password6', 'buyer3@example.com', 'Buyer');
""")

# Insert additional artists
cursor.execute("""
    INSERT INTO Artist (artist_id, biography, portfolio_url) VALUES
    (3, 'Bio of artist 3', 'http://portfolio3.com');
""")

# Insert additional artworks
cursor.execute("""
    INSERT INTO Artwork (title, description, image_url, price, availability, medium, style, artist_id) VALUES
    ('Artwork 4', 'Description 4', 'http://image4.com', 150.00, 'Available', 'Digital', 'Modern', 3);
""")

# Insert additional orders
cursor.execute("""
    INSERT INTO `Order` (order_date, total_amount, buyer_id, status) VALUES
    ('2024-09-01', 150.00, 4, 'Delivered');
""")

# Insert additional order items
cursor.execute("""
    INSERT INTO OrderItem (order_id, artwork_id, quantity) VALUES
    (3, 4, 1);
""")

# Insert additional reviews
cursor.execute("""
    INSERT INTO Review (rating, comment, buyer_id, artwork_id) VALUES
    (5, 'Excellent piece of art!', 4, 4);
""")

# Commit all changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Additional records inserted successfully!")
