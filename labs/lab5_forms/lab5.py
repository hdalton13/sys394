from flask import Flask, session, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Email, Length, Regexp


app = Flask(__name__) #I want this file to access everything through the name app
app.config['SECRET_KEY'] = 'secret key for session application'

#What the difference between a class and def?
# a class provide a means of bundling data and functionality together ()

class LoginForm(FlaskForm):
#^structure ^called LoginForm
#information below is both a function and data
    valid_pword = []
    valid_pword.append(Length(min=8))
    valid_pword.append(Regexp(r'.*[A-Za-z]', message="Must have at least one letter"))
    valid_pword.append(Regexp(r'.*[0-9]', message="Must have at least one digit"))
    valid_pword.append(Regexp(r'.*[!@#$%^&*_+=]', message="Must have at least one special character"))

    #these are validators --> we use validators to make sure we are getting what we are expection
    email = StringField('Email', validators=[Email()])
    #       ^This is establishing you need a string data type: This is somewhere where you enter a string
    #                               ^We are making a list right at this spot and we are
    password = PasswordField('Password', validators=valid_pword)
    #                                       ^passing in a list that we already created
    remember = BooleanField('Remember me on this machine')
    submit = SubmitField('Log In')

#Error: Install 'email_validator' for email validation support
#We can install email-validator the same way we did flask-wtf
# or go to the terminal at the bottom left of the and type pip install email-validator
# Pip --> is a package installer

def authenticate_user(email, pword): #this is where the username and password are in the database

    fake_user_database = {}
    fake_user_database['ds@cse.taylor.edu'] = 'Pa$$word123'
    fake_user_database['bnroller@taylor.edu'] = 'Gr3atteach!'

    if email in fake_user_database:
        if fake_user_database[email] == pword:
            return True

    return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():

        if not authenticate_user(login_form.email.data, login_form.password.data):
            flash('Username and password combination invalid')
        else:
            session['email'] = login_form.email.data
            session['remember'] = login_form.remember.data

            flash('User logged in')
            return redirect(url_for('index'))

    return render_template('login.html', form=login_form)


@app.route('/logout')
def logout():

    session.pop('email', None)
    session.pop('remember', None)

    flash('Logged out')
    return redirect(url_for('index'))


app.run(debug=True)