#include <stdio.h>
#include <stdlib.h>
#include <mysql/mysql.h>

void get_artists_with_sculpture_2023() {
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    conn = mysql_init(NULL);
    if (!mysql_real_connect(conn, "localhost", "your_username", "your_password", "art_platform", 0, NULL, 0)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    char *query = "SELECT DISTINCT a.artist_name "
                  "FROM Artist a "
                  "JOIN Artwork aw ON a.artist_id = aw.artist_id "
                  "WHERE YEAR(aw.listing_date) = 2023 "
                  "AND a.artist_id IN ("
                  "    SELECT artist_id "
                  "    FROM Artwork "
                  "    WHERE YEAR(listing_date) = 2023 "
                  "    GROUP BY artist_id "
                  "    HAVING COUNT(DISTINCT MONTH(listing_date)) = 12"
                  ") "
                  "AND a.artist_id IN ("
                  "    SELECT artist_id "
                  "    FROM Artwork "
                  "    WHERE category = 'Sculpture'"
                  ");";

    if (mysql_query(conn, query)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);
    printf("Artists with sculptures and listings in all months of 2023:\n");
    while ((row = mysql_fetch_row(res)) != NULL) {
        printf("Artist: %s\n", row[0]);
    }

    mysql_free_result(res);
    mysql_close(conn);
}

int main() {
    get_artists_with_sculpture_2023();
    return 0;
}
