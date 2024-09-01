import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="b22bb044@007bond",
    database="art_platform"
)

cursor = conn.cursor()

# SQL query to add 5 new contemporary artists

add_artists_query = """
INSERT INTO User (username, password, email, role) VALUES
('contemporary_artist1', 'password5', 'contemporary1@example.com', 'Artist'),
('contemporary_artist2', 'password6', 'contemporary2@example.com', 'Artist'),
('contemporary_artist3', 'password7', 'contemporary3@example.com', 'Artist'),
('contemporary_artist4', 'password8', 'contemporary4@example.com', 'Artist'),
('contemporary_artist5', 'password9', 'contemporary5@example.com', 'Artist');
"""

# Execute the query
cursor.execute(add_artists_query)
conn.commit()

# Assuming artist_ids start from 5, this must be checked and adjusted accordingly
add_artist_details_query = """
INSERT INTO Artist (artist_id, biography, portfolio_url) VALUES
(5, 'Biography of contemporary artist 1', 'http://portfolio5.com'),
(6, 'Biography of contemporary artist 2', 'http://portfolio6.com'),
(7, 'Biography of contemporary artist 3', 'http://portfolio7.com'),
(8, 'Biography of contemporary artist 4', 'http://portfolio8.com'),
(9, 'Biography of contemporary artist 5', 'http://portfolio9.com');
"""

# Execute the query
cursor.execute(add_artist_details_query)
conn.commit()

print("5 new contemporary artists added successfully.")

# Close the cursor and connection
cursor.close()
conn.close()
