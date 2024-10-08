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
    if (mysql_query(conn, "SELECT a.* FROM Artist a LEFT JOIN Artwork aw ON a.artist_id = aw.artist_id WHERE aw.artwork_id IS NULL;")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);

    // Output artist names
    printf("Artists without artwork:\n");
    while ((row = mysql_fetch_row(res)) != NULL)
        printf("Artist Name: %s\n", row[1]); // assuming name is second column

    // Close connection
    mysql_free_result(res);
    mysql_close(conn);

    return 0;
}
