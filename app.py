from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World! from Home Page<br/> \ '\
    '<a href="/about">About</a><br/>'\
    '<a href="/user/mynameis a Fake">Fake User Profile</a>'
    #return '<h1 style="color: red">Hello, World!</h1>'

#-----------
    #return '<h1 style="-webkit-background-clip: text; color: transparent; background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red);">Hello, World!</h1>'

@app.route('/about')
def about():
    return "This is an about page:)"
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)