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

# Step 1: Create Tables

# Create User table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        role ENUM('Artist', 'Buyer') NOT NULL
    );
""")

# Create Artist table (subtype of User)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Artist (
        artist_id INT PRIMARY KEY,
        biography TEXT,
        portfolio_url VARCHAR(255),
        FOREIGN KEY (artist_id) REFERENCES User(user_id)
    );
""")

# Create Artwork table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Artwork (
        artwork_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        image_url VARCHAR(255),
        price DECIMAL(10, 2) NOT NULL,
        availability ENUM('Available', 'Sold') NOT NULL,
        medium VARCHAR(255),
        style VARCHAR(255),
        artist_id INT,
        FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
    );
""")

# Create Order table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS `Order` (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        order_date DATE NOT NULL,
        total_amount DECIMAL(10, 2) NOT NULL,
        buyer_id INT,
        status ENUM('Pending', 'Shipped', 'Delivered') NOT NULL,
        FOREIGN KEY (buyer_id) REFERENCES User(user_id)
    );
""")

# Create OrderItem table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS OrderItem (
        order_item_id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        artwork_id INT,
        quantity INT NOT NULL,
        FOREIGN KEY (order_id) REFERENCES `Order`(order_id),
        FOREIGN KEY (artwork_id) REFERENCES Artwork(artwork_id)
    );
""")

# Create Review table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Review (
        review_id INT AUTO_INCREMENT PRIMARY KEY,
        rating INT CHECK (rating >= 1 AND rating <= 5),
        comment TEXT,
        buyer_id INT,
        artwork_id INT,
        FOREIGN KEY (buyer_id) REFERENCES User(user_id),
        FOREIGN KEY (artwork_id) REFERENCES Artwork(artwork_id)
    );
""")

# Step 2: Insert Dummy Records

# Insert dummy users
cursor.execute("""
    INSERT INTO User (username, password, email, role) VALUES
    ('artist1', 'password1', 'artist1@example.com', 'Artist'),
    ('artist2', 'password2', 'artist2@example.com', 'Artist'),
    ('buyer1', 'password3', 'buyer1@example.com', 'Buyer'),
    ('buyer2', 'password4', 'buyer2@example.com', 'Buyer');
""")

# Get the last inserted user IDs to use for artists
conn.commit()

# Insert dummy artists
cursor.execute("""
    INSERT INTO Artist (artist_id, biography, portfolio_url) VALUES
    (1, 'Bio of artist 1', 'http://portfolio1.com'),
    (2, 'Bio of artist 2', 'http://portfolio2.com');
""")

# Insert dummy artworks
cursor.execute("""
    INSERT INTO Artwork (title, description, image_url, price, availability, medium, style, artist_id) VALUES
    ('Artwork 1', 'Description 1', 'http://image1.com', 100.00, 'Available', 'Oil', 'Abstract', 1),
    ('Artwork 2', 'Description 2', 'http://image2.com', 200.00, 'Available', 'Acrylic', 'Realism', 1),
    ('Artwork 3', 'Description 3', 'http://image3.com', 300.00, 'Sold', 'Watercolor', 'Impressionism', 2);
""")

# Insert dummy orders
cursor.execute("""
    INSERT INTO `Order` (order_date, total_amount, buyer_id, status) VALUES
    ('2024-08-30', 300.00, 3, 'Pending'),
    ('2024-08-31', 200.00, 4, 'Shipped');
""")

# Insert dummy order items
cursor.execute("""
    INSERT INTO OrderItem (order_id, artwork_id, quantity) VALUES
    (1, 3, 1),
    (2, 2, 1);
""")

# Insert dummy reviews
cursor.execute("""
    INSERT INTO Review (rating, comment, buyer_id, artwork_id) VALUES
    (5, 'Amazing artwork!', 3, 3),
    (4, 'Very nice.', 4, 2);
""")

# Commit all changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Tables created and dummy records inserted successfully!")
