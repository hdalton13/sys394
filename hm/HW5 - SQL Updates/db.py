from flask import g
import psycopg2
import psycopg2.extras

data_source_name = "dbname=hdalton user=hdalton password=hdalton host=roller.cse.taylor.edu"


def open_db_connection():
    g.connection = psycopg2.connect(data_source_name)
    g.cursor = g.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


def close_db_connection():
    g.cursor.close()
    g.connection.close()


def all_trips():

    query = """
    SELECT * FROM hw4.trip
    """

    g.cursor.execute(query)
    return g.cursor.fetchall()

def create_trip(destination, year, semester):

    query = '''
    INSERT INTO hw4.trip (destination, year, semester)
    VALUES (%(destination)s, %(year)s, %(semester)s)
    '''

    g.cursor.execute(query, {'destination': destination, 'year': year, 'semester': semester})
    g.connection.commit()
    return g.cursor.rowcount