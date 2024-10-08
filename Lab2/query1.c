#include <mysql.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    char *server = "localhost";
    char *user = "root";
    char *password = "DataEngineering"; /* set me first */
    char *database = "art_platform";

    conn = mysql_init(NULL);

    // Connect to database
    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    // Send SQL query
    if (mysql_query(conn, "SELECT DISTINCT a.artist_name, aw.title FROM Artist a JOIN Artwork aw ON a.artist_id = aw.artist_id WHERE YEAR(aw.listing_date) = 2023 AND a.artist_id IN (SELECT artist_id FROM Artwork WHERE YEAR(listing_date) = 2023 GROUP BY artist_id HAVING COUNT(DISTINCT MONTH(listing_date)) = 12);")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);

    // Output artist names and titles
    printf("Artists with artwork listed in all months of 2023:\n");
    while ((row = mysql_fetch_row(res)) != NULL)
        printf("Artist: %s, Artwork: %s\n", row[0], row[1]);

    // Close connection
    mysql_free_result(res);
    mysql_close(conn);

    return 0;
}
