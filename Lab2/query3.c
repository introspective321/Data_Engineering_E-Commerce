#include <stdio.h>
#include <stdlib.h>
#include <mysql/mysql.h>

void get_artists_without_artwork() {
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    conn = mysql_init(NULL);
    if (!mysql_real_connect(conn, "localhost", "your_username", "your_password", "art_platform", 0, NULL, 0)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    char *query = "SELECT a.* "
                  "FROM Artist a "
                  "LEFT JOIN Artwork aw ON a.artist_id = aw.artist_id "
                  "WHERE aw.artwork_id IS NULL;";

    if (mysql_query(conn, query)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);
    printf("Artists without artwork listings:\n");
    while ((row = mysql_fetch_row(res)) != NULL) {
        printf("Artist ID: %s\n", row[0]);
        printf("Artist Name: %s\n", row[1]);
        printf("Biography: %s\n", row[2]);
        printf("Portfolio URL: %s\n", row[3]);
        printf("---\n");
    }

    mysql_free_result(res);
    mysql_close(conn);
}

int main() {
    get_artists_without_artwork();
    return 0;
}
