from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def verifySpaceAndLength(text):
    result = False
    space=text.find(' ')
    if space > -1:
        result=True
    elif len(text) < 3 or len(text) > 20:
        result=True
    return result

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error1=""
    error2=""
    error3=""
    error4=""

    if username=="":
        error1="That's not a valid username"
    elif verifySpaceAndLength(username):
        error1="That's not a valid username"

    if password=="":
        error2="That's not a valid password"
    elif verifySpaceAndLength(password):
        error2="That's not a valid password"

    if verify!=password:
        error3="Passwords don't match"
    
    if email!="":
        at=email.find('@')
        dot=email.find('.')
        space=email.find(' ')
        if at == -1 or dot == -1:
            error4="That's not a valid email"
        elif at > dot:
            error4="That's not a valid email"
        
        if verifySpaceAndLength(email):
            error4="That's not a valid email"

    if error1=="" and error2=="" and error3=="" and error4=="":
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', error1=error1, error2=error2, error3=error3, error4=error4, username=username, email=email)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html')

app.run()