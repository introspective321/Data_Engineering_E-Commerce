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
    if (mysql_query(conn, "SELECT DISTINCT a.* FROM Artist a JOIN Artwork aw ON a.artist_id = aw.artist_id JOIN OrderItem oi ON aw.artwork_id = oi.artwork_id JOIN `Order` o ON oi.order_id = o.order_id WHERE aw.category = 'Oil Painting' AND YEAR(o.order_date) = 2022;")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);

    // Output artist details
    printf("Artists who sold oil paintings in 2022:\n");
    while ((row = mysql_fetch_row(res)) != NULL)
        printf("Artist ID: %s, Name: %s\n", row[0], row[1]);

    // Close connection
    mysql_free_result(res);
    mysql_close(conn);

    return 0;
}
