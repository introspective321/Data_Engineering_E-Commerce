#include <stdio.h>
#include <stdlib.h>
#include <mysql/mysql.h>

void get_buyers_oil_paintings_2022() {
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    conn = mysql_init(NULL);
    if (!mysql_real_connect(conn, "localhost", "your_username", "your_password", "art_platform", 0, NULL, 0)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    char *query = "SELECT DISTINCT u.username "
                  "FROM User u "
                  "JOIN `Order` o ON u.user_id = o.buyer_id "
                  "JOIN OrderItem oi ON o.order_id = oi.order_id "
                  "JOIN Artwork aw ON oi.artwork_id = aw.artwork_id "
                  "WHERE aw.category = 'Oil Painting' "
                  "AND YEAR(o.order_date) = 2022;";

    if (mysql_query(conn, query)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);
    printf("Buyers who purchased oil paintings in 2022:\n");
    while ((row = mysql_fetch_row(res)) != NULL) {
        printf("Buyer: %s\n", row[0]);
    }

    mysql_free_result(res);
    mysql_close(conn);
}

int main() {
    get_buyers_oil_paintings_2022();
    return 0;
}
