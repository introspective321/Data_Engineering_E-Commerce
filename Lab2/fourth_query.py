import mysql.connector

def get_buyers_oil_paintings_2022():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataEngineering",
        database="art_platform"
    )
    cursor = conn.cursor()

    query = """
    SELECT DISTINCT u.username
    FROM User u
    JOIN `Order` o ON u.user_id = o.buyer_id
    JOIN OrderItem oi ON o.order_id = oi.order_id
    JOIN Artwork aw ON oi.artwork_id = aw.artwork_id
    WHERE aw.category = 'Oil Painting'
    AND YEAR(o.order_date) = 2022;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return [result[0] for result in results]

# Usage
buyers = get_buyers_oil_paintings_2022()
for buyer in buyers:
    print(f"Buyer who purchased oil painting in 2022: {buyer}")