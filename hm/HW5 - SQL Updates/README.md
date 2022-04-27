# HW5 - Database Query

**Important**: This is an individual assignment.

## Questions
1. What do we need to validate for Year? (Line 28)
   1. Does it need to be a date object or forced to be an integer? (this is what i'm doing rn)
2. In db.py where are the values coming in for the query statement (Line 23)
3. Lines 46 and 43 (In the lab we used the email data to verify the form. What do we use here?)
4. Create a Trip Report page: A route to the view function. --> I made a button, does that work?

#ToDo
* make the trip-form.html and make sure it works


## Create a database

~~You will use the same database that you created in the last assignment
(*SQL Queries*). Check the `README` file from that assignment for
complete details. You are welcome to use any SQL you wrote for that
assignment (e.g., `CREATE TABLE` statements).~~

## Create an Add Trip form

~~Using [WTForms](http://wtforms.readthedocs.org/en/latest/), create a
form that allows you to enter all the data for a `trip`
(_not_ a `student` or `student_trip`!).~~

1.  Include appropriate validators
~~2.  For the `semester` field of the form, create a drop-down list using
    the WTForms `SelectField`.~~

Here is an example of using a `SelectField`. See also [the WTForms
documentation](http://wtforms.readthedocs.org/en/latest/fields.html#wtforms.fields.SelectField).

    class AddTripForm(Form):
        # Other fields
        semester = SelectField('Semester', choices=[('fall', 'Fall'), ('jterm', 'Interterm'), ... )]) 
                                                    ^a list of twopols

Note that each entry in the `choices` array is a Python *tuple* (kind of
like an array) whose first element is the value that will be sent in the
`POST` request and whose second element is what will be displayed 
to the user in the web page.

## Create an Add Trip database function

~~Write a function in your `db.py` file that allows you to insert a new
trip into the database. It should take one parameter for each column in
the trip table.~~


## Write an Add Trip view function

Create a view function that processes the add trip form. It should:

~~1.  Use the form you defined above
~~2.  Handle both GET and POST requests
~~3.  Have a meaningful function name
~~4.  Be accessible from a meaningful URL
~~5.  Invoke the database function defined above, passing in the values of
    each form field
~~6.  Flash messages to tell the user of any errors
~~7.  Flash a message when a new trip is added successfully
~~8.  When a trip is added successfully, redirect the user to the Trip
    Report page (below). Be sure to use `url_for` appropriately.~~

Don't forget about the class examples 
available on GitHub.

## Create a Trip Report page

Create a complete web page that displays all the trips currently in the database. 
You will use this page to verify that trips are added successfully. 
The implementation of this page will be similar to the page displayed in the previous homework (only simpler!). 
You will have to define:

~~1. A database function that fetches and returns the entire contents of
   the `trip` table~~
~~2. A template that displays the result of the database query~~
~~3. A view function that runs the database function and renders the
   template with the data retrieved from the trip table~~
~~4. A route to the view function.~~