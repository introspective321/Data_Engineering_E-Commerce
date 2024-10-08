import mysql.connector

def get_artists_oil_paintings_2022():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataEngineering",
        database="art_platform"
    )
    cursor = conn.cursor(dictionary=True)

    query = """
     SELECT DISTINCT a.*
    FROM Artist a
    JOIN Artwork aw ON a.artist_id = aw.artist_id
    JOIN OrderItem oi ON aw.artwork_id = oi.artwork_id
    JOIN `Order` o ON oi.order_id = o.order_id
    WHERE aw.category = 'Oil Painting'
    AND YEAR(o.order_date) = 2022;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

# Usage
artists = get_artists_oil_paintings_2022()
for artist in artists:
    print(f"Artist: {artist['artist_name']}")
  #  print(f"Biography: {artist['biography']}")
 #   print(f"Portfolio URL: {artist['portfolio_url']}")
    print("---")