# Forms and Sessions

**This is an individual assignment.**

Review
======

Review the information on Flask forms found in the class samples:

-   [Simple forms](https://github.com/tu-isd/class-examples/tree/master/02a%20-%20sessions%20(simple))
-   [WT Forms](https://github.com/tu-isd/class-examples/tree/master/02b%20-%20sessions%20(WT%20Forms))

Take note of the following documentation:

- [WT Forms](http://wtforms.readthedocs.io/en/latest/index.html)
    (generic WT Forms documentation)
    -   [Information on specific field types](http://wtforms.readthedocs.io/en/latest/fields.html)
    -   [Details on validators](http://wtforms.readthedocs.io/en/latest/validators.html)
-   [Flask WT Forms](https://flask-wtf.readthedocs.io/en/stable/) (Flask
    interface to WT Forms)
-   [Styling forms with Bootstrap](https://getbootstrap.com/docs/4.0/components/forms)

Install
=======

~~In your development environment, you’ll need to install `Flask-WTF` in
the same way that you installed `Flask` initially.~~

~~As a reminder if you’re using PyCharm:~~

~~1.  Open **Preferences** (Mac) or **File &gt; Settings** (Windows)~~
~~2.  Navigate to **Project &gt; Project Interpreter**~~
~~3.  Click the **`+`** button and search for `Flask-WTF`.~~
~~4.  Select `Flask-WTF` and click `Install Package`.~~

Construct
=========

~~Construct a Flask application that conforms to the following requirements.~~

~~The application provides a new-user registration page at the URL
`/register`.~~

~~The page allows the user to submit:~~

-   ~~First name~~
-   ~~Last name~~
-   ~~E-mail address~~
-   ~~Password~~
-   ~~Password confirmation~~

~~The application implements a view function called `register` that can
handle both a~~

~~-   `GET` request that returns the initial, empty registration form~~
~~-   `POST` request that processes a submitted form~~

~~Use WT Forms to create your registration form. The form should include
the following validations:~~

~~1. First name and last name must be at least five characters in length~~
~~2.E-mail address must be valid~~
~~4. Password must be at least eight characters long and must contain at
    least one letter, one digit, and one punctuation character.~~
~~5. Password and password confirmation fields must match exactly~~

~~If any validation criteria fail, the application should redisplay the
form together with error information. The error message should detail
each validation failure. For example, if the first name is too short,
the password and its validation don’t match, and the e-mail address is
formatted improperly, the error message should be similar to~~

    There are errors in your registration form:
~~    * First name is too short (must be at least five characters)~~
~~    * Password and confirmation don't match~~
~~    * E-mail address doesn't look valid~~

When the registration form satisfies all the validation criteria:

~~1.  Store the user information in the Flask `session` object.~~
~~2.  Redirect the user to a confirmation page with url `/confirmation`
    *using browser redirection*.~~

~~The confirmation page should display the user’s first name, last name,
and email address (using the `session` object).~~

Verify
======

~~1.  Run the Flask development web server~~ --> this is in the bottom where the code runs
~~2.  Test all possible validation errors detailed above. Be sure the
    proper error message(s) are displayed for each type of validation.~~
~~3.  Test that a form with all valid fields results in the display of the
    confirmation page.~~

Submit
======

Commit your updated HTML file to Git and push it to Github.

Start your Git commit comment with `READY FOR GRADING` in your final
submission of the assignment.
