# HW2 - Flask/Jinja Templates

**Important** This is an individual assignment.

## Learn

For examples of how to use templates with Flask, refer to the [sample
code covered in class](https://github.com/tu-isd/examples). The
templating language we’re using is called Jinja. Find details on Jinja
at [its main web page](http://jinja.pocoo.org/).

## Construct

1.  ~~Create a base HTML template called `base.html`. Be sure to store
    this template in the `templates` directory of your assignment.~~
2. ~~Your base template should have a block (i.e., `{% block ... %} ... {% endblock %}`) for~~
    -  ~~Page title in the `<head>` element~~
    -  ~~Page content in the `<body>` element.~~
3.  ~~Create another HTML template called `letters.html`. This template
    should~~
    -   ~~Inherit from (`extend`) the `base.html` template, and override
        both `block`s defined there.~~
    -   ~~Expect to receive a list of values from its view function as a
        context variable called `letters`.~~
    -   ~~Display each element of `letters` as an item (`<li>...</li>`) in
        an ordered list (`<ol>...</ol>`)~~
    -   ~~Set the page title to the value `List of Letters`.~~
4.  ~~Create a new view function called `letters`. The function should~~
    -   ~~Be trigged by a web browser opening the route `/letters`.~~
    -   ~~Construct a list consisting of the names of the first four
        letters of the Greek alphabet: `alpha`, `beta`, `gamma`, and
        `delta`.~~
    -   ~~Render the `letters.html` template, passing it the list of Greek
        letter names as a context variable.~~

## Verify

1.  Run the development web server
2.  Navigate to `http://127.0.0.1:5000/letters`
3.  Check that the list of letters appears in the browser.

## Submit

Commit your updated HTML file to Git and push it to Github. Be sure to
start your commit comment with `READY FOR GRADING` in your final
submission of the assignment. 
