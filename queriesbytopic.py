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
	cur.execute("select topic from eighteentable where topic = 'Health Status'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Arthritis'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Disability'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Alcohol'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Oral Health'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Asthma'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Mental Health'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Cancer'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Cardiovascular Disease'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Chronic Obstructive Pulmonary Disease'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Tobacco'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Nutrition, Physical Activity, and Weight Status'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Diabetes'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Cognitive Health and Caregiving'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Social Determinants of Health'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Immunization'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Maternal Health'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Sleep'")
	result = cur.fetchone()
	cur.execute("select topic from eighteentable where topic = 'Diabetes'")
	result = cur.fetchone()
	

# Queries for 2019 table
	cur.execute("select topic from nineteentable where topic = 'Health Status'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Arthritis'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Disability'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Alcohol'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Oral Health'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Asthma'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Mental Health'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Cancer'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Cardiovascular Disease'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Chronic Obstructive Pulmonary Disease'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Tobacco'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Nutrition, Physical Activity, and Weight Status'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Diabetes'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Cognitive Health and Caregiving'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Social Determinants of Health'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Immunization'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Maternal Health'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Sleep'")
	result = cur.fetchone()
	cur.execute("select topic from nineteentable where topic = 'Diabetes'")
	result = cur.fetchone()


# Queries for 2020 table
	cur.execute("select topic from twentytable where topic = 'Health Status'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Arthritis'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Disability'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Alcohol'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Oral Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Asthma'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Mental Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Cancer'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Cardiovascular Disease'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Chronic Obstructive Pulmonary Disease'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Tobacco'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Nutrition, Physical Activity, and Weight Status'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Diabetes'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Cognitive Health and Caregiving'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Social Determinants of Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Immunization'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Maternal Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Sleep'")
	result = cur.fetchone()
	cur.execute("select topic from twentytable where topic = 'Diabetes'")
	result = cur.fetchone()


# Queries for 2021 table
	cur.execute("select topic from twentyonetable where topic = 'Health Status'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Arthritis'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Disability'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Alcohol'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Oral Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Asthma'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Mental Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Cancer'")
	result1 = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Cardiovascular Disease'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Chronic Obstructive Pulmonary Disease'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Tobacco'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Nutrition, Physical Activity, and Weight Status'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Diabetes'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Cognitive Health and Caregiving'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Social Determinants of Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Immunization'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Maternal Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Sleep'")
	result = cur.fetchone()
	cur.execute("select topic from twentyonetable where topic = 'Diabetes'")
	result = cur.fetchone()

# Queries for 2022 table
	cur.execute("select topic from twentytwotable where topic = 'Health Status'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Arthritis'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Disability'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Alcohol'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Oral Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Asthma'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Mental Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Cancer'")
	result1 = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Cardiovascular Disease'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Chronic Obstructive Pulmonary Disease'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Tobacco'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Nutrition, Physical Activity, and Weight Status'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Diabetes'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Cognitive Health and Caregiving'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Social Determinants of Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Immunization'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Maternal Health'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Sleep'")
	result = cur.fetchone()
	cur.execute("select topic from twentytwotable where topic = 'Diabetes'")
	result = cur.fetchone()


	print(result1)

	cur.close()
	conn.close()


query_db()	