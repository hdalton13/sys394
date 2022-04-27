from flask import g
import psycopg2
import psycopg2.extras


data_source_name = "dbname=hdalton user=hdalton password=hdalton host=roller.cse.taylor.edu"


def open_db_connection():
    #we are saving connection and curser at the application context; this means anywhere we use g we can access these variables
    #this can be dangerouse becasue then anyone can access these variables
    g.connection = psycopg2.connect(data_source_name) #before I make any response I need to make a connection
    g.cursor = g.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


def close_db_connection():
    g.cursor.close()
    g.connection.close()


def find_member(memberEmail):
    #the code below helps prevent SQL injection --> But How?
    query = """
    SELECT m.email, m.first_name, m.last_name, p.file_path
    FROM member AS m
       LEFT OUTER JOIN photo AS p ON m.email = p.member_email 
    WHERE email = %(emailParam)s
    """             #^this is where a layer of protection to make sure SQL injection
                    #it make sure people can't insert any SQL requests and sanatizes the data
                    #%()s --> means we are expecting a string
    g.cursor.execute(query, {'emailParam': memberEmail}) #sanitates and runs the statement; looks for a
    return g.cursor.fetchone()


def create_member(email, first_name, last_name, password):

    query = '''
    INSERT INTO member (email, first_name, last_name, password)
    VALUES (%(email)s, %(first)s, %(last)s, %(pass)s)
    '''

    g.cursor.execute(query, {'email': email, 'first': first_name, 'last': last_name, 'pass': password})
    g.connection.commit() #push the changes to the database
    return g.cursor.rowcount #a double check to make sure the commit actually worked
                        #^this returns the number of rows