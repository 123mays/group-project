from flask import Flask, render_template
import psycopg2
from psycopg2 import sql, Error
import sys

app = Flask(__name__)

def get_year_options():
    years = ['2018', '2019', '2020', '2021', '2022']
    html = "".join([f'<option value="{year}">{year}</option>\n' for year in years])
    return html

def get_age_options():
    ages = ['0-18', '19-35', '36-50', '51-65', '65+']
    html = "".join([f'<option value="{age}">{age}</option>\n' for age in ages])
    return html

def get_disease_options():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="akeelh",
            user="akeelh",
            password="spring482farm"
    
        )
        cur = conn.cursor()
        query = "SELECT DISTINCT disease FROM topic ORDER BY disease"
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

@app.route('/test')
def welcome():
    year_options = get_year_options()
    age_options = get_age_options()
    disease_options = get_disease_options()

    return render_template(
        "homepage.html", 
        YearOptions=year_options, 
        AgeOptions=age_options, 
        DiseaseOptions=disease_options
    )

if __name__ == '__main__':
    my_port = 5221
    app.run(host='0.0.0.0', port=my_port)
