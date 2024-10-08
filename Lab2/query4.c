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
    if (mysql_query(conn, "SELECT DISTINCT u.username FROM User u JOIN `Order` o ON u.user_id = o.buyer_id JOIN OrderItem oi ON o.order_id = oi.order_id JOIN Artwork aw ON oi.artwork_id = aw.artwork_id WHERE aw.category = 'Oil Painting' AND YEAR(o.order_date) = 2022;")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);

    // Output usernames
    printf("Buyers who purchased oil paintings in 2022:\n");
    while ((row = mysql_fetch_row(res)) != NULL)
        printf("Username: %s\n", row[0]);

    // Close connection
    mysql_free_result(res);
    mysql_close(conn);

    return 0;
}
