import mysql.connector

def get_artists_without_artwork():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataEngineering",
        database="art_platform"
    )
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT a.*
    FROM Artist a
    LEFT JOIN Artwork aw ON a.artist_id = aw.artist_id
    WHERE aw.artwork_id IS NULL;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

# Usage
artists = get_artists_without_artwork()
for artist in artists:
    print(f"Artist without artwork: {artist['artist_name']}")
    print(f"Biography: {artist['biography']}")
    print(f"Portfolio URL: {artist['portfolio_url']}")
    print("---")