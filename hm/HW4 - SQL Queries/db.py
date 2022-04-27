import psycopg2
import psycopg2.extras
from flask import Flask, render_template


app = Flask(__name__)

def trip_report():
    # ^this is a view function
    data_source_name = "dbname=hdalton user=hdalton password=hdalton host=roller.cse.taylor.edu"

    connection = psycopg2.connect(data_source_name)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)  # dictionary cursor (next, all)

    cursor.execute('''SELECT * FROM hw4.trip
        inner join hw4.student_trip on trip.id = student_trip.trip_id
        inner join hw4.student on student.id = student_trip.student_id''')
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return results