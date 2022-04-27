from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, FloatField
from wtforms.validators import Email, Length, InputRequired, EqualTo, DataRequired, NumberRange

import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret Unguessable Key'


@app.before_request
def before_request():
    db.open_db_connection()


@app.teardown_request
def teardown_request(exception):
    db.close_db_connection()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/trips')
def all_trips():
    return render_template("all-trips.html", trips=db.all_trips())


class TripForm(FlaskForm):
    destination = StringField('Destination', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    semester = SelectField('Semester', choices=[('fall','Fall'),('jterm','Interterm'),('spring','Spring'),('summer','Summer')])
                        #First value of tuple is what is sent in the Post, 2nd value is what the user sees
    submit = SubmitField('Save Trip')


@app.route('/trip/create', methods=['GET', 'POST'])
def create_trip():

    trip_form = TripForm()

    if trip_form.validate_on_submit():

            rowcount = db.create_trip(trip_form.destination.data,
                                        trip_form.year.data,
                                        trip_form.semester.data)

            if rowcount == 1:
                flash("Trip {} created".format(trip_form.destination.data))
                return redirect(url_for('all_trips'))
            else:
                flash("New member not created")

    return render_template('trip-form.html', form=trip_form)


app.run(debug=True)
