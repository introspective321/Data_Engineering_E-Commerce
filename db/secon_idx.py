import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",       
    user="root",           
    password="b22bb044@007bond",   
    database="art_platform" 
)

# Create a cursor object
cursor = conn.cursor()

# Add a secondary index on the 'style' column
cursor.execute("""
    CREATE INDEX idx_style ON Artwork (style);
""")

# Add a secondary index on the 'medium' column
cursor.execute("""
    CREATE INDEX idx_medium ON Artwork (medium);
""")

# Commit the changes
conn.commit()

# Verify that the indexes have been added
cursor.execute("SHOW INDEX FROM Artwork;")
indexes = cursor.fetchall()
for index in indexes:
    print(index)

# Close the cursor and connection
cursor.close()
conn.close()

print("Secondary indexes added and verified successfully!")
