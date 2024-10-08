#include <mysql.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    clock_t start_time, end_time;
    double cpu_time_used;

    start_time = clock();

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
    if (mysql_query(conn, "SELECT u.username FROM User u LEFT JOIN `Order` o ON u.user_id = o.buyer_id WHERE o.order_id IS NULL;")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }

    res = mysql_use_result(conn);

    // Output usernames
    printf("Users with no purchases:\n");
    while ((row = mysql_fetch_row(res)) != NULL)
        printf("Username: %s\n", row[0]);

    // Close connection
    mysql_free_result(res);
    mysql_close(conn);

    end_time = clock();
    cpu_time_used = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    printf("Execution time in C: %.6f seconds\n", cpu_time_used);

    return 0;
}
