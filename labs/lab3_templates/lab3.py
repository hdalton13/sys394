from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret Unguessable Key'

'''the @ sign is a decorator: it modifies a function'''
@app.route('/')
def hello_world():
    return render_template('hello.html')
'''send to the surver and then follows this function to the new location'''

@app.route('/base')
def base():
    return render_template('test.html')

@app.route('/name')
def hello_name():
    return render_template('hello-name.html', name='Fred Ziffle')

'''
What are we getting from the surver? --> route == function, /comments == , def == tye the function to that root, 
    fake_comment == a list of dictionaries with many key value pairs, { }== python dictionary, [] == python list, key:value pairs
'''
@app.route('/comments')
def comments():
    fake_comments = [ { 'who': 'wesley',
                        'what': 'As you wish!'},
                      { 'who': 'vincini',
                        'what': 'Inconceivable'} ]
    return render_template('comments.html', comments=fake_comments)
'''Why is the vaiable name comments=? --> it uses a ginga template file that the language HTML knows'''

if __name__ == '__main__':
    app.run(debug=True)


'''You need to tell the surver a method so that it knows the actions it wants to take'''