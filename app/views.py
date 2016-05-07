from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

@app.route('/hello')
def hello():
    user = {'nickname': 'Peter'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Victor 2'},
            'body': 'It\' cool learning Flask!'
        }
    ]
    return render_template('hello.html',
                           title='Page ingine ya hello!',
                           user=user,
                           posts=posts)


@app.route('/about')
def index():
    user = {'nickname': 'Peter'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': {'nickname': 'victor'}, 
            'body': 'Python is cool too!' 
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

""" return render_template('about.html',
                           title='About',
                           user=user,
                           posts=posts)
"""
