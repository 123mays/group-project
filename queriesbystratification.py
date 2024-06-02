import psycopg2

def query_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akeelh",
        user="akeelh",
        password="spring482farm"
    )
    cur = conn.cursor()

    # Queries for 2018 table
    cur.execute("select stratificationcategory1 from eighteentable where stratificationcategory1 = 'Overall'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from eighteentable where stratificationcategory1 = 'Age'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from eighteentable where stratificationcategory1 = 'Sex'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from eighteentable where stratificationcategory1 = 'Race/Ethnicity'")
    result = cur.fetchone()
    print(result)

    # Queries for 2019 table
    cur.execute("select stratificationcategory1 from nineteentable where stratificationcategory1 = 'Overall'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from nineteentable where stratificationcategory1 = 'Age'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from nineteentable where stratificationcategory1 = 'Sex'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from nineteentable where stratificationcategory1 = 'Race/Ethnicity'")
    result = cur.fetchone()
    print(result)

    # Queries for 2020 table
    cur.execute("select stratificationcategory1 from twentytable where stratificationcategory1 = 'Overall'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentytable where stratificationcategory1 = 'Age'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentytable where stratificationcategory1 = 'Sex'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentytable where stratificationcategory1 = 'Race/Ethnicity'")
    result = cur.fetchone()
    print(result)

    # Queries for 2021 table
    cur.execute("select stratificationcategory1 from twentyonetable where stratificationcategory1 = 'Overall'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentyonetable where stratificationcategory1 = 'Age'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentyonetable where stratificationcategory1 = 'Sex'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentyonetable where stratificationcategory1 = 'Race/Ethnicity'")
    result = cur.fetchone()
    print(result)

    # Queries for 2022 table
    cur.execute("select stratificationcategory1 from twentytwotable where stratificationcategory1 = 'Overall'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentytwotable where stratificationcategory1 = 'Age'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentytwotable where stratificationcategory1 = 'Sex'")
    result = cur.fetchone()
    print(result)
    cur.execute("select stratificationcategory1 from twentytwotable where stratificationcategory1 = 'Race/Ethnicity'")
    result = cur.fetchone()
    print(result)

    cur.close()
    conn.close()

query_db()
