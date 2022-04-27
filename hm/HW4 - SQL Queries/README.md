# HW4 - SQL Queries

**Important** This is an individual assignment.

## General Instructions

-   Be sure to make use of the sample code on GitHub.
-   All functions that access the database should be stored in the
    `db.py` file. Refer to the sample application for examples.
-   HTML templates should extend a `base.html`

You should have received an email that contains the details
for connecting to the database.
You will need this information to carry out these instructions. 


## Connect to your Database from PyCharm

Follow these instructions if you are using PyCharm as
your IDE (Integrated Development Environment).

~~1. Open the *Database* tool window (**View > Tool Windows > Database**)~~
~~1. Click the `+` button, and select **Data Source > PostgreSQL**. The *Data
    Sources and Drivers* window should appear.~~
~~1. Fill in fields as follows:~~
   ~~- **Name**: any text you would like to identify your database~~
   ~~- **Host**: host name from email sent previously~~
   ~~- **Database**: database name from email~~
   ~~- **User**: user name from email~~
  ~~- **Password**: password from email~~
~~1.If anything but **PostgreSQL** appears for the **Driver:**,
   look for an install link near the bottom of the window;
   click to install the Postgres driver.~~
~~1. Click **Test Connection**. If you have configured everything
   properly, you should shortly see a message saying *Successful*.~~
~~1. Click *OK* to close the *Data Sources and Drivers* window.
   You should see an entry for your new data source
   in the **Database** tool window.~~

## Connect to your database from Python

You must also include the database configuration
you received by email in your `db.py` file.
Refer to the sample code on GitHub
for an example of setting up the configuration
string that you pass to the `psycopg2` driver.


Schema
======

~~Create a schema with the following database tables. You may use the
Database features of PyCharm to create them 
(**View menu > Tool Windows > Database**) 
or write SQL `CREATE TABLE` statements directly (refer to the
code example on GitHub for examples).~~

~~Table `student`.~~
---------------

~~This table contains relevant information about students who will be
going on one or more trips.~~

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><code>Column</code></p></td>
<td><p><code>Type</code></p></td>
<td><p>Notes</p></td>
</tr>
<tr class="even">
<td><p><code>id</code></p></td>
<td><p><code>INTEGER</code></p></td>
<td><p>Primary key, auto increment</p></td>
</tr>
<tr class="odd">
<td><p><code>first_name</code></p></td>
<td><p><code>VARCHAR(30)</code></p></td>
<td><p>Required (<code>NOT NULL</code>)</p></td>
</tr>
<tr class="even">
<td><p><code>last_name</code></p></td>
<td><p><code>VARCHAR(30)</code></p></td>
<td><p>Required (<code>NOT NULL</code>)</p></td>
</tr>
<tr class="odd">
<td><p><code>class</code></p></td>
<td><p><code>VARCHAR(10)</code></p></td>
<td><p>Sufficiently large to store one of 
    <code>freshman</code>, <code>sophomore</code>, <code>junior</code>, or <code>senior</code></p></td>
</tr>
</tbody>
</table>

~~Table `trip`.~~
------------

~~This table contains data on available trips.~~

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><code>Column</code></p></td>
<td><p><code>Type</code></p></td>
<td><p>Notes</p></td>
</tr>
<tr class="even">
<td><p><code>id</code></p></td>
<td><p><code>INTEGER</code></p></td>
<td><p>Primary key, auto increment</p></td>
</tr>
<tr class="odd">
<td><p><code>destination</code></p></td>
<td><p><code>VARCHAR(100)</code></p></td>
<td><p>Destination of trip (e.g., <code>Chiang Mai, Thailand</code>)</p></td>
</tr>
<tr class="even">
<td><p><code>year</code></p></td>
<td><p><code>INTEGER</code></p></td>
<td><p>Year of trip</p></td>
</tr>
<tr class="odd">
<td><p><code>semester</code></p></td>
<td><p><code>VARCHAR(10)</code></p></td>
<td><p>Sufficient to store of 
    <code>fall</code>, <code>interterm</code>, <code>spring</code>, or <code>spring break</code></p></td>
</tr>
</tbody>
</table>

~~Table `student_trip`.~~
--------------------

~~This table is an associative table that permits a many-to-many
relatinship between students and trips. As usual for an associative
table, `student_id` and `trip_id` should be part of a composite primary
key for the table, and are also foreign keys to the `student` and `trip`
tables, respectively.~~

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><code>Column</code></p></td>
<td><p><code>Type</code></p></td>
<td><p>Notes</p></td>
</tr>
<tr class="even">
<td><p><code>student_id</code></p></td>
<td><p><code>INTEGER</code></p></td>
<td><p>Part of the composite primary key, and a foreign key to the <code>id</code> field of the <code>student</code> table</p></td>
</tr>
<tr class="odd">
<td><p><code>trip_id</code></p></td>
<td><p><code>INTEGER</code></p></td>
<td><p>Part of the composite primary key, and a foreign key to the <code>id</code> field of the <code>trip</code> table</p></td>
</tr>
</tbody>
</table>

Sample Data
===========

~~Create sample data as follows:~~

~~1.  At least three students in the `student` table
~~1.  At least two trips in the `trip` table
~~1.  At least two students per trip in the `student_trip` table.~~

~~As with schema creation, you may use PyCharm tools to populate these
tables from the **Table Editor** in the PyCharm Database view, 
or you may write SQL `INSERT` statements directly.~~

Trip Page
=========

~~Create a Flask web application that includes the following:~~

~~- a route (`/trips`)
~~- view function (`trip_report`)
~~- HTML page (`trip-report.html`)
~~- database function (`db.trip_report`)~~

~~Your application should render (create and display)
a page showing the details of all trips in the database.~~ 

~~Add some styling to the `base.html` and `trip-report.html`
templates (e.g., using Bootstrap as demonstrated in class
and shown in the sample code on GitHub).~~

Trip details should be formatted as an HTML table
containing the following columns:

~~- Trip destination
~~- Trip semester
~~- Trip year
~~- Student first name
~~- Student last name
~~- Student class~~

~~The table should contain one row for each student-trip combination 
in the `student_trip` table. 
Your database function will have to include a`SELECT` statement 
that joins together properly the three tables in the database.~~
