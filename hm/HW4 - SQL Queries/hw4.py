from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from flask import Flask, render_template

import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trips')
def trip_report():
    results= db.trip_report()

    return render_template('trip-report.html', trips=results)

app.run(debug=True)
