from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/browse')
def browse_page():
    return render_template('browse.html')

@app.route('/movies/<moviename>')
def watch_page():
    return render_template('movie.html')
