# This is a Flask web application that connects to a PostgreSQL database to retrieve and display data based on user-selected filters.
# It provides dropdown options for filtering data and displays results based on these selections.

from flask import Flask, render_template, request
import psycopg2
from psycopg2 import sql, Error
import sys

app = Flask(__name__)

def get_year_options():
    years = ['2018', '2019', '2020', '2021', '2022']
    return "".join([f'<option value="{year}">{year}</option>\n' for year in years])

def get_age_options():
    ages = ['4m - 5y', '1 - 5y', '6 - 9y', '6 - 11y', '6 - 14y', '10 - 13y', '12 - 17y', '18 - 44y', '0 - 44y', 'Age >= 65y']
    return "".join([f'<option value="{age}">{age}</option>\n' for age in ages])

def get_sex_options():
    sexes = ['Male', 'Female']
    return "".join([f'<option value="{sex}">{sex}</option>\n' for sex in sexes])

def get_race_ethnicity_options():
    races = ['White', 'Black or African American', 'American Indian or Alaska Native', 'Asian', 'Native Hawaiian or Other Pacific Islander', 'Hispanic or Latino']
    return "".join([f'<option value="{race}">{race}</option>\n' for race in races])

def get_grade_options():
    grades = ['10th', '11th', '12th']
    return "".join([f'<option value="{grade}">{grade}</option>\n' for grade in grades])

def get_location_options():
    states = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
        'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
        'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
        'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
        'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ]
    return "".join([f'<option value="{state}">{state}</option>\n' for state in states])

def get_topic_options():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="akeelh",
            user="akeelh",
            password="spring482farm"
        )
        cur = conn.cursor()
        query = """
            SELECT DISTINCT topic FROM twentytable
            UNION
            SELECT DISTINCT topic FROM eighteentable
            UNION
            SELECT DISTINCT topic FROM nineteentable
            UNION
            SELECT DISTINCT topic FROM twentyonetable
            UNION
            SELECT DISTINCT topic FROM twentytwotable
            ORDER BY topic
        """
        cur.execute(query)
        rows = cur.fetchall()
        html = "".join([f'<option value="{row[0]}">{row[0]}</option>\n' for row in rows])
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        html = '<option value="">Error loading data</option>\n'
    finally:
        if conn:
            cur.close()
            conn.close()
    return html

@app.route('/test', methods=['GET'])
def welcome():
    dropdown_options = {
        'YearOptions': get_year_options(),
        'AgeOptions': get_age_options(),
        'SexOptions': get_sex_options(),
        'RaceEthnicityOptions': get_race_ethnicity_options(),
        'GradeOptions': get_grade_options(),
        'LocationOptions': get_location_options(),
        'TopicOptions': get_topic_options()
    }
    return render_template("homepage.html", **dropdown_options)

@app.route('/results', methods=['POST'])
def results():
    selected_year = request.form.get('year')
    selected_age = request.form.get('age')
    selected_sex = request.form.get('sex')
    selected_race = request.form.get('race')
    selected_grade = request.form.get('grade')
    selected_location = request.form.get('location')
    selected_topic = request.form.get('topic')

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

    data = []
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="akeelh",
            user="akeelh",
            password="spring482farm"
        )
        cur = conn.cursor()
        
        query = sql.SQL("""
            SELECT * FROM {table}
            WHERE year = %s
            AND topic = %s
            AND ( (stratification1 = %s) OR (stratification1 = %s) OR (stratification1 = %s) OR (stratification1 = %s) )
            AND locationdesc = %s
        """).format(table=sql.Identifier(table_name))
        
        cur.execute(query, (selected_year, selected_topic, selected_age, selected_sex, selected_race, selected_grade, selected_location))
        rows = cur.fetchall()

        data = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        data = []

    finally:
        if conn:
            cur.close()
            conn.close()

    return render_template("results.html", results=data)

if __name__ == '__main__':
    my_port = 5221
    app.run(host='0.0.0.0', port=my_port)
