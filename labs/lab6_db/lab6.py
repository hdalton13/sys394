import psycopg2
import psycopg2.extras
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
#hey jinga run ur stuff


@app.route('/accounts')
def all_accounts():

    data_source_name = "dbname=hdalton user=hdalton password=hdalton host=roller.cse.taylor.edu"
#   ^this is one giant string ^this is the insecure way to do it: often times you make a separate file and read that in here

    connection = psycopg2.connect(data_source_name)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) #dictionary cursor (next, all)
    #^this is comming back as a dictionary

    cursor.execute('SELECT * FROM account')
    #^try running this on our connection
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('all-accounts.html', accounts=results)


app.run(debug=True)