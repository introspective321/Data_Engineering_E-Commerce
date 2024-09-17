import mysql.connector

def get_artists_with_sculpture_2023():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataEngineering",
        database="art_platform"
    )
    cursor = conn.cursor()

    query = """
    SELECT DISTINCT a.artist_name
    FROM Artist a
    JOIN Artwork aw ON a.artist_id = aw.artist_id
    WHERE YEAR(aw.listing_date) = 2023
    AND a.artist_id IN (
        SELECT artist_id
        FROM Artwork
        WHERE YEAR(listing_date) = 2023
        GROUP BY artist_id
        HAVING COUNT(DISTINCT MONTH(listing_date)) = 12
    )
    AND a.artist_id IN (
        SELECT artist_id
        FROM Artwork
        WHERE category = 'Sculpture'
    );
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return [result[0] for result in results]

# Usage
artists = get_artists_with_sculpture_2023()
for artist in artists:
    print(f"Artist with sculpture: {artist}")