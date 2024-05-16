from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_year_options():
    years = ['2018', '2019','2020','2021', '2022']
    html = "".join([f'<option value="{year}">{year}</option>\n' for year in years])
    return html

def get_age_options():
    ages = ['0-18', '19-35', '36-50', '51-65', '65+']
    html = "".join([f'<option value="{age}">{age}</option>\n' for age in ages])
    return html

def get_disease_options():
    conn = psycopg2.connect(
        host="localhost",
        port=5221,
        database="neiroukhm",
        user="neiroukhm",
        password="spring847eyebrow"
    )
    cur = conn.cursor()
    query = "SELECT DISTINCT disease FROM topic ORDER BY topic"
    cur.execute(query)
    rows = cur.fetchall()
    html = "".join([f'<option value="{row[0]}">{row[0]}</option>\n' for row in rows])
    conn.close()
    return html

def get_other_options():
    options = ['Option1', 'Option2', 'Option3']
    html = "".join([f'<option value="{option}">{option}</option>\n' for option in options])
    return html

@app.route('/test')
def welcome():
    year_options = get_year_options()
    age_options = get_age_options()
    disease_options = get_disease_options()
    other_options = get_other_options()

    return render_template(
        "homepage.html", 
        YearOptions=year_options, 
        AgeOptions=age_options, 
        DiseaseOptions=disease_options, 
        OtherOptions=other_options
    )

if __name__ == '__main__':
    my_port = 5221
    app.run(host='0.0.0.0', port=my_port)
