from flask import Flask, render_template, session, request, redirect, url_for
#Session --> "a temporary and interactive information interchange between two or more communicating devices,
#               or between a computer and user. A session is established at a certain point in time, and then
#               ‘torn down’ - brought to an end - at some later point."
# allow us to remember things
# uses the cookies to store data
    #Ex) (Stateful Communication) When login in, the server wants to remember who is doing the requests

app = Flask(__name__)
#__name__ tells something to use this current file

app.config['SECRET_KEY'] = 'super secret key' #in reality the variable should be auto generated
#a session key==session id(see power point) informs us who is using the session

@app.route('/')
def index():

    if 'user' in session:
        return render_template("member.html")
    else:
        return render_template("guest.html")

    #return render_template('guest.html', message='You are not logged in')


@app.route('/signup', methods=['GET', 'POST']) #you can only get one request at a time
def sign_up():

    if request.method == 'POST': #We are expecting some sort of data with POST

        session['user'] = {} #We want to make an empty user variable
        session['user']['name'] = request.form['name'] #In that empty user varable we want to add the name recieved from the form
        session['user']['email'] = request.form['email']

        return redirect(url_for('index')) #if the surver is still listening the browser will redirect to a different page
        # (if server setting are turned on it will ask to make sure you want to redirect)
        # (from the server, browser please, give ,e index again)

    else: #This takes in any GET request given
        return render_template("signup.html")


@app.route('/memberarea')
def memberarea():
    return render_template("memberarea.html")


@app.route('/logout')
def log_out():
    # Remove username from session if present
    session.pop('user', None) #works like a stack (First on, Last off) --> pops the most recent on
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)