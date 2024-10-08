import mysql.connector
from mysql.connector import Error
import time

def main():
    start_time = time.time()

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
    for row in rows:
        print(row)
    
    if conn is not None and conn.is_connected():
        conn.close()

    end_time = time.time()
    print("Execution time in Python: {:.6f} seconds".format(end_time - start_time))

if __name__ == '__main__':
    main()
