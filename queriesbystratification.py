import psycopg2


def query_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5217,
        database="knopk",
        user="knopk",
        password="pencil597smile")
    cur = conn.cursor()



# Queries for 2018 table
	cur.execute("select stratificationcategory1 from eighteentable where tratificationategory1 = 'Overall'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from eighteentable where tratificationategory1 = 'Age'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from eighteentable where tratificationategory1 = 'Sex'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from eighteentable where tratificationategory1 = 'Race/Ethnicity'")
	result = cur.fetchone()

# Queries for 2019 table
	cur.execute("select stratificationcategory1 from nineteentable where tratificationategory1 = 'Overall'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from nineteentable where tratificationategory1 = 'Age'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from nineteentable where tratificationategory1 = 'Sex'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from eighteentable where tratificationategory1 = 'Race/Ethnicity'")
	result = cur.fetchone()

# Queries for 2020 table
	cur.execute("select stratificationcategory1 from twentytable where tratificationategory1 = 'Overall'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentytable where tratificationategory1 = 'Age'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentytable where tratificationategory1 = 'Sex'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentytable where tratificationategory1 = 'Race/Ethnicity'")
	result = cur.fetchone()

# Queries for 2021 table
	cur.execute("select stratificationcategory1 from twentyonetable where tratificationategory1 = 'Overall'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentyonetable where tratificationategory1 = 'Age'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentyonetable where tratificationategory1 = 'Sex'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentyonetable where tratificationategory1 = 'Race/Ethnicity'")
	result = cur.fetchone()

# Queries for 2022 table
	cur.execute("select stratificationcategory1 from twentytwotable where tratificationategory1 = 'Overall'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentytwotable where tratificationategory1 = 'Age'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentytwotable where tratificationategory1 = 'Sex'")
	result = cur.fetchone()
	cur.execute("select stratificationcategory1 from twentytwotable where tratificationategory1 = 'Race/Ethnicity'")
	result = cur.fetchone()
	cur.close()
	conn.close()

query_db()