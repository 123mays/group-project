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
            SELECT *,
                CASE
                    WHEN stratificationid1 IN %s THEN 'Age'
                    WHEN stratificationid1 IN %s THEN 'Sex'
                    WHEN stratificationid1 IN %s THEN 'Race'
                END AS stratification_category
            FROM {table}
            WHERE year = %s
            AND topic = %s
            AND stratificationid1 IN %s
            AND stratificationid2 = %s
            AND locationdesc = %s
        """).format(table=sql.Identifier(table_name))

        # Combine the stratification criteria
        stratifications = [selected_age, selected_sex, selected_race]

        # Execute the query
        cur.execute(query, (tuple(selected_age), tuple(selected_sex), tuple(selected_race), selected_year, selected_topic, tuple(stratifications), selected_grade, selected_location))
        rows = cur.fetchall()

        # Convert rows to a list of dictionaries and create separate columns for age, sex, and race
        data = []
        for row in rows:
            row_dict = dict((cur.description[i][0], value) for i, value in enumerate(row))
            if row_dict['stratificationid1'] == selected_age:
                row_dict['Age'] = selected_age
            if row_dict['stratificationid1'] == selected_sex:
                row_dict['Sex'] = selected_sex
            if row_dict['stratificationid1'] == selected_race:
                row_dict['Race'] = selected_race
            data.append(row_dict)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        data = []

    finally:
        if conn:
            cur.close()
            conn.close()

    return data

# Example usage
data = query_db("2020", "18 - 44y", "Male", "White", "10th", "Idaho", "Cancer")
print(data)