import psycopg2
from psycopg2 import sql, Error

def query_db(selected_year, selected_age, selected_sex, selected_race, selected_grade, selected_location, selected_topic):
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="akeelh",
            user="akeelh",
            password="spring482farm"
        )
        cur = conn.cursor()

        # Determine the table to query based on the year
        if selected_year == "2020":
            table_name = "twentytable"
        elif selected_year == "2018":
            table_name = "eighteentable"
        elif selected_year == "2019":
            table_name = "nineteentable"
        elif selected_year == "2021":
            table_name = "twentyonetable"
        else:
            table_name = "twentytwotable"

        # Build the query dynamically
        query = sql.SQL("""
            SELECT * FROM {table}
            WHERE year = %s
            AND topic = %s
            AND (stratificationid1 = %s OR stratificationid1 = %s OR stratificationid1 = %s)
            AND stratificationid1 = %s
            AND locationdesc = %s
        """).format(table=sql.Identifier(table_name))

        # Execute the query
        cur.execute(query, (selected_year, selected_topic, selected_age, selected_sex, selected_race, selected_grade, selected_location))
        rows = cur.fetchall()

        # Convert rows to a list of dictionaries
        data = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        data = []

    finally:
        if conn:
            cur.close()
            conn.close()

    return data

# Example usage
 data = query_db("2020", "Age", "Sex", "Race/Ethnicity", "Grade", "Location", "Topic")
 print(data)
