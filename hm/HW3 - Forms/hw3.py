from flask import Flask, session, redirect, url_for, render_template, flash,request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Email, Length, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seceret key for session application'

class registerForm(FlaskForm):
    valid_pword = []
    valid_pword.append(Length(min=8))
    valid_pword.append(Regexp(r'.*[A-Za-z]', message="Must have at least one letter"))
    valid_pword.append(Regexp(r'.*[0-9]', message="Must have at least one digit"))
    valid_pword.append(Regexp(r'.*[.!?,:;-_]', message="Must have at least one punctuation character"))

    valid_flname =[]
    valid_flname.append(Length(min=5))

    firstN = StringField('First Name', validators=valid_flname)
    lastN = StringField('Last Name', validators=valid_flname)
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=valid_pword)
    confirmP = PasswordField('Password confirmation', validators=valid_pword)
    remember = BooleanField('Remember me on this machine')
    submit = SubmitField('Log In')

def authenticate_user(email, pword):

    fake_user_database = {}
    fake_user_database['ds@cse.taylor.edu'] = 'Pa$$word123'
    fake_user_database['bnroller@taylor.edu'] = 'Gr3atteach!'
    fake_user_database['example@gmail.com'] = 'password12!'

    if email in fake_user_database:
        if fake_user_database[email] == pword:
            return True

    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods= ['GET','POST'])
def register():

    register_form = registerForm()

    if register_form.validate_on_submit():
        if register_form.password.data != register_form.confirmP.data:
            flash('Passwords do not match')
        else:
            #This is where I am storing the user information in the Flask session object
            session['firstN'] = register_form.firstN.data
            session['lastN'] = register_form.lastN.data
            session['email'] = register_form.email.data
            session['remember'] = register_form.remember.data

            flash('User Registered in')
            return redirect(url_for('confirmation')) #this is the redirection
    return render_template('register.html', form=register_form)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/logout')
def logout():
    session.pop('firstN', None)
    session.pop('lastN', None)
    session.pop('email', None)
    session.pop('remember', None)

    flash('Logged out')
    return redirect(url_for('index'))

app.run(debug=True)
