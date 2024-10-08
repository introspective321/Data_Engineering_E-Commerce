import mysql.connector
from mysql.connector import Error


conn = mysql.connector.connect(
    host='localhost',        
    user='root',    
    password='DataEngineering', 
    database='art_platform' 
    )
    
cursor = conn.cursor()      

cursor.execute("""
        SELECT u.username
        FROM User u
        LEFT JOIN `Order` o ON u.user_id = o.buyer_id
        WHERE o.order_id IS NULL;
        """)

rows = cursor.fetchall()
if rows:
        for row in rows:
                print(row)
        else:
            print("No users found with zero purchases.")

    
if conn is not None and conn.is_connected():
    conn.close()
