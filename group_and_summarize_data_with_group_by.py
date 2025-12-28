import sqlite3

def group_and_summarize_data_with_group_by():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #1
    query = "SELECT category, COUNT(*) AS total_products FROM products GROUP BY category"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    group_and_summarize_data_with_group_by()