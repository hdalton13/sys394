'''by:Heather Dalton'''
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret Unguessable Key'

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/base')
def base():
    return render_template('test.html')

@app.route('/letters')
def letters():
    x = ['alpha','beta','gamma','delta']
    return render_template('letters.html', letters=x)


if __name__ == '__main__':
    app.run(debug=True)