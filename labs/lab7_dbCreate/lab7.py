from flask import Flask, render_template, g, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, InputRequired, EqualTo


import db # if error, right-click parent directory "mark directory as" "sources root"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret Unguessable Key'


@app.before_request #open database
def before_request():
    db.open_db_connection() #opens the database connection before it is sent to the server (has nothing to do with the function above)

#Mitch gets a text from roller about cleaning his car. Before sending the response Mitch will check his schedule


@app.teardown_request #after request
def teardown_request(exception):
    db.close_db_connection()
#After the request is sent tear down the connection

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/accounts')
def all_accounts():
                        #you may have to specify the scheme by saying schemeName.table
    g.cursor.execute('SELECT * FROM account ORDER BY name') #curser was defined in db.py
    #telling the curser object to run the code on the object and it has a place to store it. Thats why we don't have to
    #set it to a variable right away
    results = g.cursor.fetchall() #this is how we get the information that the .execute
    #                   ^this gets everything

    return render_template('all-accounts.html', accounts=results)


class MemberForm(FlaskForm): #class object with a parameter
    #this class inharits all the attributes that are given in FlaskForm
    email = StringField('Email', validators=[Email()]) #they expect a list
    first_name = StringField('First Name', validators=[Length(min=1, max=40)])
    last_name = StringField('Last Name', validators=[Length(min=1, max=40)])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Save Member')


@app.route('/members/create', methods=['GET', 'POST']) #POST -> we are exepting information that the user gives
def create_member():

    member_form = MemberForm() #<-Referencing the instance of the MemberForm
                               #member_form = MemberForm <- referencing the entire object of MemberForm

    # The validate_on_submit() method checks for two conditions.
    # 1. If we're handling a GET request, it returns false,
    #    and we fall through to render_template(), which sends the empty form.
    # 2. Otherwise, we're handling a POST request, so it runs the validators on the form,
    #    and returns false if any fail, so we also fall through to render_template()
    #    which renders the form and shows any error messages stored by the validators.
    if member_form.validate_on_submit():
        member = db.find_member(member_form.email.data) #this is the member that you find


        if member is not None:
            flash("Member {} already exists".format(member_form.email.data))
                                            #
        else:
            rowcount = db.create_member(member_form.email.data,
                                        member_form.first_name.data,
                                        member_form.last_name.data,
                                        member_form.password.data)

            if rowcount == 1:
                flash("Member {} created".format(member_form.email.data))
                return redirect(url_for('index'))
            else:
                flash("New member not created")

    # We will get here under any of the following conditions:
    # 1. We're handling a GET request, so we render the (empty) form.
    # 2. We're handling a POST request, and some validator failed, so we render the
    #    form with the same values so that the member can try again. The template
    #    will extract and display the error messages stored on the form object
    #    by the validators that failed.
    # 3. The email entered in the form corresponds to an existing member.
    #    The template will render an error message from the flash.
    # 4. Something happened when we tried to update the database (rowcount != 1).
    #    The template will render an error message from the flash.
    return render_template('member-form.html', form=member_form)


app.run(debug=True) #have at the end of your code or you will have bad day

'''
##Questions to look up in the future
    - why to get to a path do we use a dot instead of a dash, comma, etc? (reference lines 32 and 33)
        - these are objects and we can access it through the dot   
    - is it bad to always use a path? Ex) public.account and hw4.trip
'''