import psycopg2
from psycopg2 import sql, Error

def test_database_connection():
    print("Starting database connection test...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="akeelh",
            user="akeelh",
            password="spring482farm"
        )
        print("Connection established successfully.")
        cur = conn.cursor()
        query = """
            SELECT * FROM (
                SELECT * FROM twentytable
                UNION
                SELECT * FROM eighteentable
                UNION
                SELECT * FROM nineteentable
                UNION
                SELECT * FROM twentyonetable
                UNION
                SELECT * FROM twentytwotable
            ) AS combined
            WHERE year = %s
            AND (stratification1 = %s
            OR stratification1 = %s
            OR stratification1 = %s
            OR stratification1 = %s)
            AND locationdesc = %s
            AND topic = %s
        """
        cur.execute(query, ('2020', '18 - 44y', 'Male', 'White', '10th', 'California', 'Diabetes'))
        print("Query executed successfully.")
        rows = cur.fetchall()
        print("Query results:")
        for row in rows:
            print(row)
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")

'''
if __name__ == '__main__':
    test_database_connection()
'''

test_database_connection()
